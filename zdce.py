#!/usr/bin/env python3
import os
import argparse
import torch
from torch.utils.data import DataLoader
from torchvision import transforms, datasets

# 1) Custom op registration
from pytorch_nndct.utils import register_custom_op
import model as zmod


@register_custom_op(op_type="tensor_mul", attrs_list=["iterations"])
def custom_mul(ctx, x, x_r, iterations):
    # element-wise multiplication
    return torch.mul(x,x_r)

class ZeroDCEQ(zmod.enhance_net_nopool):
    def __init__(self, scale_factor=8, iterations=8):
        super().__init__(scale_factor)
        self.iterations = iterations

    def forward(self, x):
        # x_r: the per-pixel curve from the original network
        x_r = super().forward(x)  # shape [N,3,H,W]
        # now apply LE‑curve for `iterations` steps using custom op
        enhanced = x
        for _ in range(self.iterations):
            # square: enhanced * enhanced
            x_sq = custom_mul(enhanced, enhanced,1)
            diff = x_sq - enhanced
            alpha = custom_mul(x_r, diff,1)
            enhanced = enhanced + alpha
        return enhanced
    


# 3) Data loaders (batch_size=1, normalize [0,1])
def get_loader(data_dir):
    tf = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),            # maps to [0,1]
    ])
    ds = datasets.ImageFolder(data_dir, transform=tf)
    return DataLoader(ds, batch_size=1, shuffle=False)


# 4) Main entrypoint
def main():
    parser = argparse.ArgumentParser(
        description="Zero-DCE Quant/Test/Float + export xmodel"
    )
    parser.add_argument("--calib_dir",   default = 'data/calib/',
                        help="Folder of calibration images")
    parser.add_argument("--test_dir",    default= '/data/test/',
                        help="Folder of test images")
    parser.add_argument("--model_path",  default='Epoch99.pth' ,
                        help="Path to trained `enhance_net_nopool` weights (.pth)")
    parser.add_argument("--xmodel_out",  default="./quantize_result",
                        help="Directory to save exported .xmodel")
    parser.add_argument("--mode",        default="calib",
                        choices=["float","calib","test"],
                        help="float / calib / test")
    parser.add_argument("--iterations",  default=8, type=int,
                        help="Number of LE‑curve iterations")
    parser.add_argument("--deploy", action="store_true",
                        help="Also export .xmodel in test mode")
    
    parser.add_argument(
    "--inspect",
    action="store_true",
    help="Run Vitis‑AI Inspector on the model before quantization")
    parser.add_argument(
        "--target",
        default="DPUCZDX8G_ISA1_B4096",
        help="DPU target IP for Inspector (e.g. DPUCZDX8G_ISA1_B4096)")

    args = parser.parse_args()
    

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
  


    # Instantiate and load weights
    net = ZeroDCEQ(scale_factor=8, iterations=args.iterations).to(device).eval()
    net.load_state_dict(torch.load(args.model_path, map_location=device))

    # Prepare a dummy sample for tracing
    sample = torch.randn(1, 3, 512, 512)
    
   

    
          # Optional: run Vitis‑AI Inspector
    if args.inspect:
        from pytorch_nndct import Inspector
        inspector = Inspector(args.target)
        print(f"=> Inspector on {args.target}")
        inspector.inspect(
            net,
            (sample,),
            device=device,
            output_dir=os.path.join(args.xmodel_out, "inspect"),
            image_format="png"
        )
        print("=> Inspector done")

    # Create quantizer
    from pytorch_nndct.apis import torch_quantizer
    quantizer = torch_quantizer(args.mode, net, sample, device=device)
    qnet = quantizer.quant_model

    # Calibration step
    if args.mode == "calib":
        loader = get_loader(args.calib_dir)
        with torch.no_grad():
            for img, _ in loader:
                img = img.to(device)
                _ = qnet(img)  # run forward to collect stats
        quantizer.export_quant_config()
        print("Calibration complete. Quant config exported.")

    # Float evaluation or quantized test
    if args.mode in ("float", "test"):
        loader = get_loader(args.test_dir)
        print(f"Running {args.mode} inference on {len(loader)} images...")
        with torch.no_grad():
            for img, _ in loader:
                img = img.to(device)
                enhanced, curve = qnet(img)
                # you can compute metrics here if desired

    # Export xmodel for deployment
    if args.mode == "test" and args.deploy:
        os.makedirs(args.xmodel_out, exist_ok=True)
        quantizer.export_xmodel(deploy_check=False,
                                path=args.xmodel_out)
        print(f".xmodel files written to {args.xmodel_out}")

    print("Done.")
    
    
if __name__ == "__main__":
    main()
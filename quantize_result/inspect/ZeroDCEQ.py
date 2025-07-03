# GENETARED BY NNDCT, DO NOT EDIT!

import torch
from torch import tensor
import pytorch_nndct as py_nndct

class ZeroDCEQ(py_nndct.nn.NndctQuantModel):
    def __init__(self):
        super(ZeroDCEQ, self).__init__()
        self.module_0 = py_nndct.nn.Module('nndct_const') #ZeroDCEQ::4428
        self.module_1 = py_nndct.nn.Module('nndct_const') #ZeroDCEQ::4430
        self.module_2 = py_nndct.nn.Input() #ZeroDCEQ::input_0
        self.module_3 = py_nndct.nn.Interpolate() #ZeroDCEQ::ZeroDCEQ/input.1
        self.module_4 = py_nndct.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=3, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv1]/Conv2d[depth_conv]/input.3
        self.module_5 = py_nndct.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv1]/Conv2d[point_conv]/input.5
        self.module_6 = py_nndct.nn.ReLU(inplace=True) #ZeroDCEQ::ZeroDCEQ/ReLU[relu]/input.7
        self.module_7 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv2]/Conv2d[depth_conv]/input.9
        self.module_8 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv2]/Conv2d[point_conv]/input.11
        self.module_9 = py_nndct.nn.ReLU(inplace=True) #ZeroDCEQ::ZeroDCEQ/ReLU[relu]/input.13
        self.module_10 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv3]/Conv2d[depth_conv]/input.15
        self.module_11 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv3]/Conv2d[point_conv]/input.17
        self.module_12 = py_nndct.nn.ReLU(inplace=True) #ZeroDCEQ::ZeroDCEQ/ReLU[relu]/input.19
        self.module_13 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv4]/Conv2d[depth_conv]/input.21
        self.module_14 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv4]/Conv2d[point_conv]/input.23
        self.module_15 = py_nndct.nn.ReLU(inplace=True) #ZeroDCEQ::ZeroDCEQ/ReLU[relu]/2676
        self.module_16 = py_nndct.nn.Cat() #ZeroDCEQ::ZeroDCEQ/input.25
        self.module_17 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv5]/Conv2d[depth_conv]/input.27
        self.module_18 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv5]/Conv2d[point_conv]/input.29
        self.module_19 = py_nndct.nn.ReLU(inplace=True) #ZeroDCEQ::ZeroDCEQ/ReLU[relu]/2718
        self.module_20 = py_nndct.nn.Cat() #ZeroDCEQ::ZeroDCEQ/input.31
        self.module_21 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv6]/Conv2d[depth_conv]/input.33
        self.module_22 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv6]/Conv2d[point_conv]/input.35
        self.module_23 = py_nndct.nn.ReLU(inplace=True) #ZeroDCEQ::ZeroDCEQ/ReLU[relu]/2760
        self.module_24 = py_nndct.nn.Cat() #ZeroDCEQ::ZeroDCEQ/input.37
        self.module_25 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv7]/Conv2d[depth_conv]/input.39
        self.module_26 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv7]/Conv2d[point_conv]/2801
        self.module_27 = py_nndct.nn.Hardsigmoid(inplace=False) #ZeroDCEQ::ZeroDCEQ/2802
        self.module_28 = py_nndct.nn.Module('nndct_elemwise_mul') #ZeroDCEQ::ZeroDCEQ/4429
        self.module_29 = py_nndct.nn.Add() #ZeroDCEQ::ZeroDCEQ/input
        self.module_30 = py_nndct.nn.Interpolate() #ZeroDCEQ::ZeroDCEQ/UpsamplingBilinear2d[upsample]/x_r
        self.module_31 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4306
        self.module_32 = py_nndct.nn.Sub() #ZeroDCEQ::ZeroDCEQ/diff.1
        self.module_33 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4310
        self.module_34 = py_nndct.nn.Add() #ZeroDCEQ::ZeroDCEQ/enhanced.1
        self.module_35 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4314
        self.module_36 = py_nndct.nn.Sub() #ZeroDCEQ::ZeroDCEQ/diff.3
        self.module_37 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4318
        self.module_38 = py_nndct.nn.Add() #ZeroDCEQ::ZeroDCEQ/enhanced.3
        self.module_39 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4322
        self.module_40 = py_nndct.nn.Sub() #ZeroDCEQ::ZeroDCEQ/diff.5
        self.module_41 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4326
        self.module_42 = py_nndct.nn.Add() #ZeroDCEQ::ZeroDCEQ/enhanced.5
        self.module_43 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4330
        self.module_44 = py_nndct.nn.Sub() #ZeroDCEQ::ZeroDCEQ/diff.7
        self.module_45 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4334
        self.module_46 = py_nndct.nn.Add() #ZeroDCEQ::ZeroDCEQ/enhanced.7
        self.module_47 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4338
        self.module_48 = py_nndct.nn.Sub() #ZeroDCEQ::ZeroDCEQ/diff.9
        self.module_49 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4342
        self.module_50 = py_nndct.nn.Add() #ZeroDCEQ::ZeroDCEQ/enhanced.9
        self.module_51 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4346
        self.module_52 = py_nndct.nn.Sub() #ZeroDCEQ::ZeroDCEQ/diff.11
        self.module_53 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4350
        self.module_54 = py_nndct.nn.Add() #ZeroDCEQ::ZeroDCEQ/enhanced.11
        self.module_55 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4354
        self.module_56 = py_nndct.nn.Sub() #ZeroDCEQ::ZeroDCEQ/diff.13
        self.module_57 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4358
        self.module_58 = py_nndct.nn.Add() #ZeroDCEQ::ZeroDCEQ/enhanced
        self.module_59 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4362
        self.module_60 = py_nndct.nn.Sub() #ZeroDCEQ::ZeroDCEQ/diff
        self.module_61 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/4366
        self.module_62 = py_nndct.nn.Add() #ZeroDCEQ::ZeroDCEQ/4369

    @py_nndct.nn.forward_processor
    def forward(self, *args):
        output_module_0 = self.module_0(data=2.0, dtype=torch.float, device='cuda')
        output_module_1 = self.module_1(data=-1.0, dtype=torch.float, device='cuda')
        output_module_2 = self.module_2(input=args[0])
        output_module_3 = self.module_3(input=output_module_2, size=None, scale_factor=[0.125,0.125], mode='bilinear', align_corners=False)
        output_module_3 = self.module_4(output_module_3)
        output_module_3 = self.module_5(output_module_3)
        output_module_3 = self.module_6(output_module_3)
        output_module_7 = self.module_7(output_module_3)
        output_module_7 = self.module_8(output_module_7)
        output_module_7 = self.module_9(output_module_7)
        output_module_10 = self.module_10(output_module_7)
        output_module_10 = self.module_11(output_module_10)
        output_module_10 = self.module_12(output_module_10)
        output_module_13 = self.module_13(output_module_10)
        output_module_13 = self.module_14(output_module_13)
        output_module_13 = self.module_15(output_module_13)
        output_module_16 = self.module_16(dim=1, tensors=[output_module_10,output_module_13])
        output_module_16 = self.module_17(output_module_16)
        output_module_16 = self.module_18(output_module_16)
        output_module_16 = self.module_19(output_module_16)
        output_module_20 = self.module_20(dim=1, tensors=[output_module_7,output_module_16])
        output_module_20 = self.module_21(output_module_20)
        output_module_20 = self.module_22(output_module_20)
        output_module_20 = self.module_23(output_module_20)
        output_module_24 = self.module_24(dim=1, tensors=[output_module_3,output_module_20])
        output_module_24 = self.module_25(output_module_24)
        output_module_24 = self.module_26(output_module_24)
        output_module_24 = self.module_27(output_module_24)
        output_module_24 = self.module_28(input=output_module_24, other=output_module_0)
        output_module_24 = self.module_29(input=output_module_24, other=output_module_1, alpha=1)
        output_module_24 = self.module_30(input=output_module_24, size=None, scale_factor=[8.0,8.0], mode='bilinear', align_corners=True)
        output_module_31 = self.module_31(output_module_2,output_module_2,1)
        output_module_31 = self.module_32(input=output_module_31, other=output_module_2, alpha=1)
        output_module_33 = self.module_33(output_module_24,output_module_31,1)
        output_module_34 = self.module_34(input=output_module_2, other=output_module_33, alpha=1)
        output_module_35 = self.module_35(output_module_34,output_module_34,1)
        output_module_35 = self.module_36(input=output_module_35, other=output_module_34, alpha=1)
        output_module_37 = self.module_37(output_module_24,output_module_35,1)
        output_module_38 = self.module_38(input=output_module_34, other=output_module_37, alpha=1)
        output_module_39 = self.module_39(output_module_38,output_module_38,1)
        output_module_39 = self.module_40(input=output_module_39, other=output_module_38, alpha=1)
        output_module_41 = self.module_41(output_module_24,output_module_39,1)
        output_module_42 = self.module_42(input=output_module_38, other=output_module_41, alpha=1)
        output_module_43 = self.module_43(output_module_42,output_module_42,1)
        output_module_43 = self.module_44(input=output_module_43, other=output_module_42, alpha=1)
        output_module_45 = self.module_45(output_module_24,output_module_43,1)
        output_module_46 = self.module_46(input=output_module_42, other=output_module_45, alpha=1)
        output_module_47 = self.module_47(output_module_46,output_module_46,1)
        output_module_47 = self.module_48(input=output_module_47, other=output_module_46, alpha=1)
        output_module_49 = self.module_49(output_module_24,output_module_47,1)
        output_module_50 = self.module_50(input=output_module_46, other=output_module_49, alpha=1)
        output_module_51 = self.module_51(output_module_50,output_module_50,1)
        output_module_51 = self.module_52(input=output_module_51, other=output_module_50, alpha=1)
        output_module_53 = self.module_53(output_module_24,output_module_51,1)
        output_module_54 = self.module_54(input=output_module_50, other=output_module_53, alpha=1)
        output_module_55 = self.module_55(output_module_54,output_module_54,1)
        output_module_55 = self.module_56(input=output_module_55, other=output_module_54, alpha=1)
        output_module_57 = self.module_57(output_module_24,output_module_55,1)
        output_module_58 = self.module_58(input=output_module_54, other=output_module_57, alpha=1)
        output_module_59 = self.module_59(output_module_58,output_module_58,1)
        output_module_59 = self.module_60(input=output_module_59, other=output_module_58, alpha=1)
        output_module_61 = self.module_61(output_module_24,output_module_59,1)
        output_module_62 = self.module_62(input=output_module_58, other=output_module_61, alpha=1)
        return output_module_62

# GENETARED BY NNDCT, DO NOT EDIT!

import torch
from torch import tensor
import pytorch_nndct as py_nndct

class ZeroDCEQ(py_nndct.nn.NndctQuantModel):
    def __init__(self):
        super(ZeroDCEQ, self).__init__()
        self.module_0 = py_nndct.nn.Module('nndct_const') #ZeroDCEQ::1384
        self.module_1 = py_nndct.nn.Module('nndct_const') #ZeroDCEQ::1388
        self.module_2 = py_nndct.nn.Module('nndct_const') #ZeroDCEQ::1386
        self.module_3 = py_nndct.nn.Input() #ZeroDCEQ::input_0
        self.module_4 = py_nndct.nn.Interpolate() #ZeroDCEQ::ZeroDCEQ/input.1
        self.module_5 = py_nndct.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=3, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv1]/Conv2d[depth_conv]/input.3
        self.module_6 = py_nndct.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv1]/Conv2d[point_conv]/input.5
        self.module_7 = py_nndct.nn.ReLU(inplace=True) #ZeroDCEQ::ZeroDCEQ/ReLU[relu]/input.7
        self.module_8 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv2]/Conv2d[depth_conv]/input.9
        self.module_9 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv2]/Conv2d[point_conv]/input.11
        self.module_10 = py_nndct.nn.ReLU(inplace=True) #ZeroDCEQ::ZeroDCEQ/ReLU[relu]/input.13
        self.module_11 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv3]/Conv2d[depth_conv]/input.15
        self.module_12 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv3]/Conv2d[point_conv]/input.17
        self.module_13 = py_nndct.nn.ReLU(inplace=True) #ZeroDCEQ::ZeroDCEQ/ReLU[relu]/input.19
        self.module_14 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv4]/Conv2d[depth_conv]/input.21
        self.module_15 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv4]/Conv2d[point_conv]/input.23
        self.module_16 = py_nndct.nn.ReLU(inplace=True) #ZeroDCEQ::ZeroDCEQ/ReLU[relu]/1154
        self.module_17 = py_nndct.nn.Cat() #ZeroDCEQ::ZeroDCEQ/input.25
        self.module_18 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv5]/Conv2d[depth_conv]/input.27
        self.module_19 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv5]/Conv2d[point_conv]/input.29
        self.module_20 = py_nndct.nn.ReLU(inplace=True) #ZeroDCEQ::ZeroDCEQ/ReLU[relu]/1196
        self.module_21 = py_nndct.nn.Cat() #ZeroDCEQ::ZeroDCEQ/input.31
        self.module_22 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv6]/Conv2d[depth_conv]/input.33
        self.module_23 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv6]/Conv2d[point_conv]/input.35
        self.module_24 = py_nndct.nn.ReLU(inplace=True) #ZeroDCEQ::ZeroDCEQ/ReLU[relu]/1238
        self.module_25 = py_nndct.nn.Cat() #ZeroDCEQ::ZeroDCEQ/input.37
        self.module_26 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv7]/Conv2d[depth_conv]/input.39
        self.module_27 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ZeroDCEQ::ZeroDCEQ/CSDN_Tem[e_conv7]/Conv2d[point_conv]/1279
        self.module_28 = py_nndct.nn.Hardsigmoid(inplace=False) #ZeroDCEQ::ZeroDCEQ/1280
        self.module_29 = py_nndct.nn.Module('nndct_elemwise_mul') #ZeroDCEQ::ZeroDCEQ/1385
        self.module_30 = py_nndct.nn.Add() #ZeroDCEQ::ZeroDCEQ/input
        self.module_31 = py_nndct.nn.Interpolate() #ZeroDCEQ::ZeroDCEQ/UpsamplingBilinear2d[upsample]/x_r
        self.module_32 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/1292
        self.module_33 = py_nndct.nn.Module('nndct_elemwise_mul') #ZeroDCEQ::ZeroDCEQ/1389
        self.module_34 = py_nndct.nn.Add() #ZeroDCEQ::ZeroDCEQ/diff
        self.module_35 = py_nndct.nn.Module('tensor_mul') #ZeroDCEQ::ZeroDCEQ/1310
        self.module_36 = py_nndct.nn.Add() #ZeroDCEQ::ZeroDCEQ/1325

    @py_nndct.nn.forward_processor
    def forward(self, *args):
        output_module_0 = self.module_0(data=2.0, dtype=torch.float, device='cpu')
        output_module_1 = self.module_1(data=-1.0, dtype=torch.float, device='cpu')
        output_module_2 = self.module_2(data=-1.0, dtype=torch.float, device='cpu')
        output_module_3 = self.module_3(input=args[0])
        output_module_4 = self.module_4(input=output_module_3, size=None, scale_factor=[0.125,0.125], mode='bilinear', align_corners=False)
        output_module_4 = self.module_5(output_module_4)
        output_module_4 = self.module_6(output_module_4)
        output_module_4 = self.module_7(output_module_4)
        output_module_8 = self.module_8(output_module_4)
        output_module_8 = self.module_9(output_module_8)
        output_module_8 = self.module_10(output_module_8)
        output_module_11 = self.module_11(output_module_8)
        output_module_11 = self.module_12(output_module_11)
        output_module_11 = self.module_13(output_module_11)
        output_module_14 = self.module_14(output_module_11)
        output_module_14 = self.module_15(output_module_14)
        output_module_14 = self.module_16(output_module_14)
        output_module_17 = self.module_17(dim=1, tensors=[output_module_11,output_module_14])
        output_module_17 = self.module_18(output_module_17)
        output_module_17 = self.module_19(output_module_17)
        output_module_17 = self.module_20(output_module_17)
        output_module_21 = self.module_21(dim=1, tensors=[output_module_8,output_module_17])
        output_module_21 = self.module_22(output_module_21)
        output_module_21 = self.module_23(output_module_21)
        output_module_21 = self.module_24(output_module_21)
        output_module_25 = self.module_25(dim=1, tensors=[output_module_4,output_module_21])
        output_module_25 = self.module_26(output_module_25)
        output_module_25 = self.module_27(output_module_25)
        output_module_25 = self.module_28(output_module_25)
        output_module_25 = self.module_29(input=output_module_25, other=output_module_0)
        output_module_25 = self.module_30(input=output_module_25, other=output_module_2, alpha=1)
        output_module_25 = self.module_31(input=output_module_25, size=None, scale_factor=[8.0,8.0], mode='bilinear', align_corners=True)
        output_module_32 = self.module_32(output_module_3,output_module_3)
        output_module_33 = self.module_33(input=output_module_3, other=output_module_1)
        output_module_32 = self.module_34(input=output_module_32, other=output_module_33, alpha=1)
        output_module_25 = self.module_35(output_module_25,output_module_32)
        output_module_36 = self.module_36(input=output_module_3, other=output_module_25, alpha=1)
        return output_module_36

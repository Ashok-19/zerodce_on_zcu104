# GENETARED BY NNDCT, DO NOT EDIT!

import torch
from torch import tensor
import pytorch_nndct as py_nndct

class enhance_net_nopool(py_nndct.nn.NndctQuantModel):
    def __init__(self):
        super(enhance_net_nopool, self).__init__()
        self.module_0 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4427
        self.module_1 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4431
        self.module_2 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4437
        self.module_3 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4443
        self.module_4 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4449
        self.module_5 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4455
        self.module_6 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4461
        self.module_7 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4467
        self.module_8 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4473
        self.module_9 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4479
        self.module_10 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4475
        self.module_11 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4469
        self.module_12 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4463
        self.module_13 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4457
        self.module_14 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4451
        self.module_15 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4445
        self.module_16 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4439
        self.module_17 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4433
        self.module_18 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4429
        self.module_19 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4435
        self.module_20 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4441
        self.module_21 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4447
        self.module_22 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4453
        self.module_23 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4459
        self.module_24 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4465
        self.module_25 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4471
        self.module_26 = py_nndct.nn.Module('nndct_const') #enhance_net_nopool::4477
        self.module_27 = py_nndct.nn.Input() #enhance_net_nopool::input_0
        self.module_28 = py_nndct.nn.Module('nndct_clamp') #enhance_net_nopool::enhance_net_nopool/input.1
        self.module_29 = py_nndct.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=3, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv1]/Conv2d[depth_conv]/input.3
        self.module_30 = py_nndct.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv1]/Conv2d[point_conv]/input.5
        self.module_31 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/ReLU[relu]/input.7
        self.module_32 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv2]/Conv2d[depth_conv]/input.9
        self.module_33 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv2]/Conv2d[point_conv]/input.11
        self.module_34 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/ReLU[relu]/input.13
        self.module_35 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv3]/Conv2d[depth_conv]/input.15
        self.module_36 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv3]/Conv2d[point_conv]/input.17
        self.module_37 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/ReLU[relu]/input.21
        self.module_38 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv4]/Conv2d[depth_conv]/input.23
        self.module_39 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv4]/Conv2d[point_conv]/input.25
        self.module_40 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/ReLU[relu]/2714
        self.module_41 = py_nndct.nn.Cat() #enhance_net_nopool::enhance_net_nopool/input.29
        self.module_42 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv5]/Conv2d[depth_conv]/input.31
        self.module_43 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv5]/Conv2d[point_conv]/input.33
        self.module_44 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/ReLU[relu]/2761
        self.module_45 = py_nndct.nn.Cat() #enhance_net_nopool::enhance_net_nopool/input.37
        self.module_46 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv6]/Conv2d[depth_conv]/input.39
        self.module_47 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv6]/Conv2d[point_conv]/input.41
        self.module_48 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/ReLU[relu]/2803
        self.module_49 = py_nndct.nn.Cat() #enhance_net_nopool::enhance_net_nopool/input.43
        self.module_50 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv7]/Conv2d[depth_conv]/input
        self.module_51 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #enhance_net_nopool::enhance_net_nopool/CSDN_Tem[e_conv7]/Conv2d[point_conv]/2844
        self.module_52 = py_nndct.nn.Sigmoid() #enhance_net_nopool::enhance_net_nopool/2845
        self.module_53 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4428
        self.module_54 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4430
        self.module_55 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/x_r
        self.module_56 = py_nndct.nn.Module('nndct_clamp') #enhance_net_nopool::enhance_net_nopool/2855
        self.module_57 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4234
        self.module_58 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4434
        self.module_59 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4238
        self.module_60 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4239
        self.module_61 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/x.45
        self.module_62 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4242
        self.module_63 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4436
        self.module_64 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4246
        self.module_65 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4438
        self.module_66 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4250
        self.module_67 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4251
        self.module_68 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4440
        self.module_69 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4255
        self.module_70 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4256
        self.module_71 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/x.47
        self.module_72 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4259
        self.module_73 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4442
        self.module_74 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4263
        self.module_75 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4444
        self.module_76 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4267
        self.module_77 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4268
        self.module_78 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4446
        self.module_79 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4272
        self.module_80 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4273
        self.module_81 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/x.49
        self.module_82 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4276
        self.module_83 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4448
        self.module_84 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4280
        self.module_85 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4450
        self.module_86 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4284
        self.module_87 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4285
        self.module_88 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4452
        self.module_89 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4289
        self.module_90 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4290
        self.module_91 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/x.51
        self.module_92 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4293
        self.module_93 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4454
        self.module_94 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4297
        self.module_95 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4456
        self.module_96 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4301
        self.module_97 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4302
        self.module_98 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4458
        self.module_99 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4306
        self.module_100 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4307
        self.module_101 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/x.53
        self.module_102 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4310
        self.module_103 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4460
        self.module_104 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4314
        self.module_105 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4462
        self.module_106 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4318
        self.module_107 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4319
        self.module_108 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4464
        self.module_109 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4323
        self.module_110 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4324
        self.module_111 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/x.55
        self.module_112 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4327
        self.module_113 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4466
        self.module_114 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4331
        self.module_115 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4468
        self.module_116 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4335
        self.module_117 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4336
        self.module_118 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4470
        self.module_119 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4340
        self.module_120 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4341
        self.module_121 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/x.57
        self.module_122 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4344
        self.module_123 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4472
        self.module_124 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4348
        self.module_125 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4474
        self.module_126 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4352
        self.module_127 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4353
        self.module_128 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4476
        self.module_129 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4357
        self.module_130 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4358
        self.module_131 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/x
        self.module_132 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4361
        self.module_133 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4478
        self.module_134 = py_nndct.nn.ReLU(inplace=False) #enhance_net_nopool::enhance_net_nopool/4365
        self.module_135 = py_nndct.nn.Module('nndct_elemwise_mul') #enhance_net_nopool::enhance_net_nopool/4480
        self.module_136 = py_nndct.nn.Add() #enhance_net_nopool::enhance_net_nopool/4369

    @py_nndct.nn.forward_processor
    def forward(self, *args):
        output_module_0 = self.module_0(data=2.0, dtype=torch.float, device='cuda')
        output_module_1 = self.module_1(data=0.5, dtype=torch.float, device='cuda')
        output_module_2 = self.module_2(data=-1.0, dtype=torch.float, device='cuda')
        output_module_3 = self.module_3(data=-1.0, dtype=torch.float, device='cuda')
        output_module_4 = self.module_4(data=-1.0, dtype=torch.float, device='cuda')
        output_module_5 = self.module_5(data=-1.0, dtype=torch.float, device='cuda')
        output_module_6 = self.module_6(data=-1.0, dtype=torch.float, device='cuda')
        output_module_7 = self.module_7(data=-1.0, dtype=torch.float, device='cuda')
        output_module_8 = self.module_8(data=-1.0, dtype=torch.float, device='cuda')
        output_module_9 = self.module_9(data=-1.0, dtype=torch.float, device='cuda')
        output_module_10 = self.module_10(data=-1.0, dtype=torch.float, device='cuda')
        output_module_11 = self.module_11(data=-1.0, dtype=torch.float, device='cuda')
        output_module_12 = self.module_12(data=-1.0, dtype=torch.float, device='cuda')
        output_module_13 = self.module_13(data=-1.0, dtype=torch.float, device='cuda')
        output_module_14 = self.module_14(data=-1.0, dtype=torch.float, device='cuda')
        output_module_15 = self.module_15(data=-1.0, dtype=torch.float, device='cuda')
        output_module_16 = self.module_16(data=-1.0, dtype=torch.float, device='cuda')
        output_module_17 = self.module_17(data=-1.0, dtype=torch.float, device='cuda')
        output_module_18 = self.module_18(data=-1.0, dtype=torch.float, device='cuda')
        output_module_19 = self.module_19(data=-1.0, dtype=torch.float, device='cuda')
        output_module_20 = self.module_20(data=-1.0, dtype=torch.float, device='cuda')
        output_module_21 = self.module_21(data=-1.0, dtype=torch.float, device='cuda')
        output_module_22 = self.module_22(data=-1.0, dtype=torch.float, device='cuda')
        output_module_23 = self.module_23(data=-1.0, dtype=torch.float, device='cuda')
        output_module_24 = self.module_24(data=-1.0, dtype=torch.float, device='cuda')
        output_module_25 = self.module_25(data=-1.0, dtype=torch.float, device='cuda')
        output_module_26 = self.module_26(data=-1.0, dtype=torch.float, device='cuda')
        output_module_27 = self.module_27(input=args[0])
        output_module_27 = self.module_28(input=output_module_27, min=0.0, max=1.0)
        output_module_29 = self.module_29(output_module_27)
        output_module_29 = self.module_30(output_module_29)
        output_module_29 = self.module_31(output_module_29)
        output_module_32 = self.module_32(output_module_29)
        output_module_32 = self.module_33(output_module_32)
        output_module_32 = self.module_34(output_module_32)
        output_module_35 = self.module_35(output_module_32)
        output_module_35 = self.module_36(output_module_35)
        output_module_35 = self.module_37(output_module_35)
        output_module_38 = self.module_38(output_module_35)
        output_module_38 = self.module_39(output_module_38)
        output_module_38 = self.module_40(output_module_38)
        output_module_41 = self.module_41(dim=1, tensors=[output_module_35,output_module_38])
        output_module_41 = self.module_42(output_module_41)
        output_module_41 = self.module_43(output_module_41)
        output_module_41 = self.module_44(output_module_41)
        output_module_45 = self.module_45(dim=1, tensors=[output_module_32,output_module_41])
        output_module_45 = self.module_46(output_module_45)
        output_module_45 = self.module_47(output_module_45)
        output_module_45 = self.module_48(output_module_45)
        output_module_49 = self.module_49(dim=1, tensors=[output_module_29,output_module_45])
        output_module_49 = self.module_50(output_module_49)
        output_module_49 = self.module_51(output_module_49)
        output_module_49 = self.module_52(output_module_49)
        output_module_49 = self.module_53(input=output_module_49, other=output_module_0)
        output_module_49 = self.module_54(input=output_module_49, other=output_module_18, alpha=1)
        output_module_49 = self.module_55(input=output_module_49, other=output_module_1)
        output_module_56 = self.module_56(input=output_module_49, min=-1.0, max=1.0)
        output_module_57 = self.module_57(input=output_module_27, other=output_module_27)
        output_module_58 = self.module_58(input=output_module_27, other=output_module_17)
        output_module_57 = self.module_59(input=output_module_57, other=output_module_58, alpha=1)
        output_module_60 = self.module_60(input=output_module_56, other=output_module_57)
        output_module_61 = self.module_61(input=output_module_27, other=output_module_60, alpha=1)
        output_module_61 = self.module_62(output_module_61)
        output_module_63 = self.module_63(input=output_module_61, other=output_module_19, alpha=1)
        output_module_63 = self.module_64(output_module_63)
        output_module_63 = self.module_65(input=output_module_63, other=output_module_2)
        output_module_66 = self.module_66(input=output_module_61, other=output_module_63, alpha=1)
        output_module_67 = self.module_67(input=output_module_66, other=output_module_66)
        output_module_68 = self.module_68(input=output_module_66, other=output_module_16)
        output_module_67 = self.module_69(input=output_module_67, other=output_module_68, alpha=1)
        output_module_70 = self.module_70(input=output_module_56, other=output_module_67)
        output_module_71 = self.module_71(input=output_module_66, other=output_module_70, alpha=1)
        output_module_71 = self.module_72(output_module_71)
        output_module_73 = self.module_73(input=output_module_71, other=output_module_20, alpha=1)
        output_module_73 = self.module_74(output_module_73)
        output_module_73 = self.module_75(input=output_module_73, other=output_module_3)
        output_module_76 = self.module_76(input=output_module_71, other=output_module_73, alpha=1)
        output_module_77 = self.module_77(input=output_module_76, other=output_module_76)
        output_module_78 = self.module_78(input=output_module_76, other=output_module_15)
        output_module_77 = self.module_79(input=output_module_77, other=output_module_78, alpha=1)
        output_module_80 = self.module_80(input=output_module_56, other=output_module_77)
        output_module_81 = self.module_81(input=output_module_76, other=output_module_80, alpha=1)
        output_module_81 = self.module_82(output_module_81)
        output_module_83 = self.module_83(input=output_module_81, other=output_module_21, alpha=1)
        output_module_83 = self.module_84(output_module_83)
        output_module_83 = self.module_85(input=output_module_83, other=output_module_4)
        output_module_86 = self.module_86(input=output_module_81, other=output_module_83, alpha=1)
        output_module_87 = self.module_87(input=output_module_86, other=output_module_86)
        output_module_88 = self.module_88(input=output_module_86, other=output_module_14)
        output_module_87 = self.module_89(input=output_module_87, other=output_module_88, alpha=1)
        output_module_90 = self.module_90(input=output_module_56, other=output_module_87)
        output_module_91 = self.module_91(input=output_module_86, other=output_module_90, alpha=1)
        output_module_91 = self.module_92(output_module_91)
        output_module_93 = self.module_93(input=output_module_91, other=output_module_22, alpha=1)
        output_module_93 = self.module_94(output_module_93)
        output_module_93 = self.module_95(input=output_module_93, other=output_module_5)
        output_module_96 = self.module_96(input=output_module_91, other=output_module_93, alpha=1)
        output_module_97 = self.module_97(input=output_module_96, other=output_module_96)
        output_module_98 = self.module_98(input=output_module_96, other=output_module_13)
        output_module_97 = self.module_99(input=output_module_97, other=output_module_98, alpha=1)
        output_module_100 = self.module_100(input=output_module_56, other=output_module_97)
        output_module_101 = self.module_101(input=output_module_96, other=output_module_100, alpha=1)
        output_module_101 = self.module_102(output_module_101)
        output_module_103 = self.module_103(input=output_module_101, other=output_module_23, alpha=1)
        output_module_103 = self.module_104(output_module_103)
        output_module_103 = self.module_105(input=output_module_103, other=output_module_6)
        output_module_106 = self.module_106(input=output_module_101, other=output_module_103, alpha=1)
        output_module_107 = self.module_107(input=output_module_106, other=output_module_106)
        output_module_108 = self.module_108(input=output_module_106, other=output_module_12)
        output_module_107 = self.module_109(input=output_module_107, other=output_module_108, alpha=1)
        output_module_110 = self.module_110(input=output_module_56, other=output_module_107)
        output_module_111 = self.module_111(input=output_module_106, other=output_module_110, alpha=1)
        output_module_111 = self.module_112(output_module_111)
        output_module_113 = self.module_113(input=output_module_111, other=output_module_24, alpha=1)
        output_module_113 = self.module_114(output_module_113)
        output_module_113 = self.module_115(input=output_module_113, other=output_module_7)
        output_module_116 = self.module_116(input=output_module_111, other=output_module_113, alpha=1)
        output_module_117 = self.module_117(input=output_module_116, other=output_module_116)
        output_module_118 = self.module_118(input=output_module_116, other=output_module_11)
        output_module_117 = self.module_119(input=output_module_117, other=output_module_118, alpha=1)
        output_module_120 = self.module_120(input=output_module_56, other=output_module_117)
        output_module_121 = self.module_121(input=output_module_116, other=output_module_120, alpha=1)
        output_module_121 = self.module_122(output_module_121)
        output_module_123 = self.module_123(input=output_module_121, other=output_module_25, alpha=1)
        output_module_123 = self.module_124(output_module_123)
        output_module_123 = self.module_125(input=output_module_123, other=output_module_8)
        output_module_126 = self.module_126(input=output_module_121, other=output_module_123, alpha=1)
        output_module_127 = self.module_127(input=output_module_126, other=output_module_126)
        output_module_128 = self.module_128(input=output_module_126, other=output_module_10)
        output_module_127 = self.module_129(input=output_module_127, other=output_module_128, alpha=1)
        output_module_130 = self.module_130(input=output_module_56, other=output_module_127)
        output_module_131 = self.module_131(input=output_module_126, other=output_module_130, alpha=1)
        output_module_131 = self.module_132(output_module_131)
        output_module_133 = self.module_133(input=output_module_131, other=output_module_26, alpha=1)
        output_module_133 = self.module_134(output_module_133)
        output_module_133 = self.module_135(input=output_module_133, other=output_module_9)
        output_module_136 = self.module_136(input=output_module_131, other=output_module_133, alpha=1)
        return (output_module_136,output_module_49)

# RnnU-Net 中的残差编码器预设
框架预设时，请引用我们最近关于3D医学图像分割中严格验证需求的论文：

Isensee, F. * , Wald, T. * , Ulrich, C. * , Baumgartner, M. * , Roy, ​​S., Maier-Hein, K. † , Jaeger, P. † (2024)。nnU-Net 再探：呼吁在 3D 医学图像分割中进行严格验证。arXiv 预印本 arXiv:2404.09556。

*: 共同第一作者
† : 共同最后作者
> Isensee, F.<sup>* </sup>, Wald, T.<sup>* </sup>, Ulrich, C.<sup>* </sup>, Baumgartner, M.<sup>* </sup>, Roy, S., Maier-Hein, K.<sup>†</sup>, Jaeger, P.<sup>†</sup> (2024). nnU-Net Revisited: A Call for Rigorous Validation in 3D Medical Image Segmentation. arXiv preprint arXiv:2404.09556.

*: shared first authors\
<sup>†</sup>: shared last authors

[PAPER LINK](https://arxiv.org/pdf/2404.09556.pdf)


自我们参加 KiTS2019 以来，nnU-Net 就已经支持残差编码器 UNet，但一直没有引起广泛关注。随着我们新的 nnUNetResEncUNet 预定推出，这一情况将发生改变 🙌！
特别是在 KiTS2023 和 AMOS2022 等大数据集上，它们提供了改进的分割性能！

|                        | BTCV  | ACDC  | LiTS  | BraTS | KiTS  | AMOS  |  VRAM |  RT | Arch. | nnU |
|------------------------|-------|-------|-------|-------|-------|-------|-------|-----|-------|-----|
|                        | n=30  | n=200 | n=131 | n=1251| n=489 | n=360 |       |     |       |     |
| nnU-Net (org.) [1]     | 83.08 | 91.54 | 80.09 | 91.24 | 86.04 | 88.64 |  7.70 |  9  |  CNN  | Yes |
| nnU-Net ResEnc M       | 83.31 | 91.99 | 80.75 | 91.26 | 86.79 | 88.77 |  9.10 |  12 |  CNN  | Yes |
| nnU-Net ResEnc L       | 83.35 | 91.69 | 81.60 | 91.13 | 88.17 | 89.41 | 22.70 |  35 |  CNN  | Yes |
| nnU-Net ResEnc XL      | 83.28 | 91.48 | 81.19 | 91.18 | 88.67 | 89.68 | 36.60 |  66 |  CNN  | Yes |
| MedNeXt L k3 [2]       | 84.70 | 92.65 | 82.14 | 91.35 | 88.25 | 89.62 | 17.30 |  68 |  CNN  | Yes |
| MedNeXt L k5 [2]       | 85.04 | 92.62 | 82.34 | 91.50 | 87.74 | 89.73 | 18.00 | 233 |  CNN  | Yes |
| STU-Net S [3]          | 82.92 | 91.04 | 78.50 | 90.55 | 84.93 | 88.08 |  5.20 |  10 |  CNN  | Yes |
| STU-Net B [3]          | 83.05 | 91.30 | 79.19 | 90.85 | 86.32 | 88.46 |  8.80 |  15 |  CNN  | Yes |
| STU-Net L [3]          | 83.36 | 91.31 | 80.31 | 91.26 | 85.84 | 89.34 | 26.50 |  51 |  CNN  | Yes |
| SwinUNETR [4]          | 78.89 | 91.29 | 76.50 | 90.68 | 81.27 | 83.81 | 13.10 |  15 |   TF  | Yes |
| SwinUNETRV2 [5]        | 80.85 | 92.01 | 77.85 | 90.74 | 84.14 | 86.24 | 13.40 |  15 |   TF  | Yes |
| nnFormer [6]           | 80.86 | 92.40 | 77.40 | 90.22 | 75.85 | 81.55 |  5.70 |  8  |   TF  | Yes |
| CoTr [7]               | 81.95 | 90.56 | 79.10 | 90.73 | 84.59 | 88.02 |  8.20 |  18 |   TF  | Yes |
| No-Mamba Base          | 83.69 | 91.89 | 80.57 | 91.26 | 85.98 | 89.04 |  12.0 |  24 |  CNN  | Yes |
| U-Mamba Bot [8]        | 83.51 | 91.79 | 80.40 | 91.26 | 86.22 | 89.13 | 12.40 |  24 |  Mam  | Yes |
| U-Mamba Enc [8]        | 82.41 | 91.22 | 80.27 | 90.91 | 86.34 | 88.38 | 24.90 |  47 |  Mam  | Yes |
| A3DS SegResNet [9,11]  | 80.69 | 90.69 | 79.28 | 90.79 | 81.11 | 87.27 | 20.00 |  22 |  CNN  |  No |
| A3DS DiNTS [10, 11]    | 78.18 | 82.97 | 69.05 | 87.75 | 65.28 | 82.35 | 29.20 |  16 |  CNN  |  No |
| A3DS SwinUNETR [4, 11] | 76.54 | 82.68 | 68.59 | 89.90 | 52.82 | 85.05 | 34.50 |  9  |   TF  |  No |

结果取自我们的论文（见上文），报告的目标是每个数据集上 5 折交叉验证计算的 Dice 分数。所有模型都从头开始训练。

RT: 训练运行时间（在1x Nvidia A100 PCIe 40GB上测量）
VRAM: 训练期间使用的GPU显存，如nvidia-smi所报告
Arch.: CNN = 卷积神经网络；TF = 变压器；Mam = Mamba
nnU: 该架构是否在nnU-Net框架中进行集成和测试（由我们或原作者）

## 如何使用新预先

我们提供了三个新的预设，每个预设针对各自的GPU显存和计算预算：

- `nnU-Net ResEnc M` : 类似于标准UNet配置的GPU预算。其中具有9-11GB显存的GPU。训练时间：A100上约12小时
- `nnU-Net ResEnc L` : 需要具有24GB显存的GPU。训练时间：A100上约35小时
- `nnU-Net ResEnc XL` : 需要具有40GB显存的GPU。训练时间：A100上约66小时

### **:👉 我们推荐 nnU-Net ResEnc L 作为新的默认nnU-Net配置！👈**

新的预设使用方式如下（M/L/XL = 任选一个！）：

1. 在运行实验计划和预处理时指定所需的配置： `nnUNetv2_plan_and_preprocess -d DATASET -pl nnUNetPlannerResEnc(M/L/XL)`。
- 这些计划器使用与`标准2d和3d_fullres配置相同的预处理数据文件夹`，因为预处理数据是相同的。只有3d_lowres不同，并将保存在不同文件夹，以允许所有配置共存！
- 如果您`只计划运行3d_fullres/2d`，并且您已经预处理了，您可以直接运行 `nnUNetv2_plan_experiment -d DATASET -pl nnUNetPlannerResEnc(M/L/XL)`来避免重新预处理！
```bash
nnUNetv2_plan_and_preprocess -d DATASET -pl nnUNetPlannerResEnc(M/L/XL)
nnUNetv2_plan_experiment -d DATASET -pl nnUNetPlannerResEnc(M/L/XL)
```
nnUNetv2_plan_and_preprocess -d DATASET -pl nnUNetPlannerResEncL
nnUNetv2_plan_experiment -d DATASET -pl nnUNetPlannerResEncL

2. 现在，只需在运行`nnUNetv2_train`，`nnUNetv2_predict`等时指定正确的计划。[所有nnU-Net命令的接口都是一致的]：`-p nnUNetResEncUNet(M/L/XL)Plans`

新预设的训练结果将永远留在心里，不会覆盖标准nnU-Net结果！ 所以封面，尽管尝试吧！
```bash
验证数据集完整性：
nnUNetv2_plan_and_preprocess -d 510 --verify_dataset_integrity

使用新预设进行实验计划和预处理：
nnUNetv2_plan_and_preprocess -d 505 -pl nnUNetPlannerResEncM
nnUNetv2_plan_and_preprocess -d 510 -pl nnUNetPlannerResEncL

运行实验计划（如果已完成预处理）：
nnUNetv2_plan_experiment -d 505 -pl nnUNetPlannerResEncM
nnUNetv2_plan_experiment -d 510 -pl nnUNetPlannerResEncL

训练模型：
nnUNetv2_train -d 510 -c CONFIGURATION -p nnUNetResEncUNetLPlans

进行预测：
nnUNetv2_predict -i INPUT_FOLDER -o OUTPUT_FOLDER -d 510 -c CONFIGURATION -p nnUNetResEncUNetLPlans

- CONFIGURATION：具体的配置（如 2d、3d_fullres 等）。
- INPUT_FOLDER：预测时的输入文件夹。
- OUTPUT_FOLDER：预测结果的输出文件夹。
```

## 超越预设扩展ResEnc nnU-Net

 预先与`ResEncUNetPlanner`两个区别在于：
- 它们为企业`gpu_memory_target_in_gb`带来了新的挑战，并产生了严重的成本支出
- 它们可以修改订单大小的上限0.05（=在一个批次不能覆盖整个数据集的超过5%的税率之前）

从一开始就应该让生活更轻松，并标准化配置供人们进行基准测试。您可以轻松调整GPU内存目标以匹配您的GPU，并预计超过40GB的GPU内存。

那么这个问题在于[Dataset003_Liver]上其中包括[80GB VRAM]的示例：

`nnUNetv2_plan_experiment -d 3 -pl nnUNetPlannerResEncM -gpu_memory_target 80 -overwrite_plans_name nnUNetResEncUNetPlans_80G`

只需按照上述方法使用`-p nnUNetResEncUNetPlans_80G`！运行上述示例将产生一个警告并注明以非标准`gpu_memory_target_in_gb`运行`nnUNetPlannerM`”。
这里可以忽略这个警告。 在处理[VRAM]目标时总是使用`-overwrite_plans_name NEW_PLANS_NAME`更改计划标识符，并为预设计划庆贺！

为什么不使用`ResEncUNetPlanner`->因为那个仍然有5%的利息！


### 源自多个GPU

在内核的多个GPU中，不要只为`nnUNetv2_plan_experiment`指定组合的[VRAM]，它可以为一个GPU提供预期的大小过大，无法被单个GPU处理。

最好让此命令`针对一个GPU的VRAM预算运行`，然后手动编辑计划文件以增加批量大小。

可以使用配置继承在生成的计划JSON文件的配置字典中，添加以下条目：

```json
        "3d_fullres_bsXX": {
            "inherits_from": "3d_fullres",
            "batch_size": XX
        },
```
其中 XX 是新的批处理大小。如果3d_fullres在一个GPU上的批处理大小为 2，而您计划里面的8个GPU，则将新批处理大小设为 2x8=16！

然后，可以使用 nnU-Net 的多GPU设置训练新配置：

```bash
nnUNetv2_train DATASETID 3d_fullres_bsXX FOLD -p nnUNetResEncUNetPlans_80G -num_gpus 8
```

## Proposing a new segmentation method? Benchmark the right way!
When benchmarking new segmentation methods against nnU-Net, we encourage to benchmark against the residual encoder 
variants. For a fair comparison, pick the variant that most closely matches the GPU memory and compute 
requirements of your method!


## References
 [1] Isensee, Fabian, et al. "nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation." Nature methods 18.2 (2021): 203-211.\
 [2] Roy, Saikat, et al. "Mednext: transformer-driven scaling of convnets for medical image segmentation." International Conference on Medical Image Computing and Computer-Assisted Intervention. Cham: Springer Nature Switzerland, 2023.\
 [3] Huang, Ziyan, et al. "Stu-net: Scalable and transferable medical image segmentation models empowered by large-scale supervised pre-training." arXiv preprint arXiv:2304.06716 (2023).\
 [4] Hatamizadeh, Ali, et al. "Swin unetr: Swin transformers for semantic segmentation of brain tumors in mri images." International MICCAI Brainlesion Workshop. Cham: Springer International Publishing, 2021.\
 [5] He, Yufan, et al. "Swinunetr-v2: Stronger swin transformers with stagewise convolutions for 3d medical image segmentation." International Conference on Medical Image Computing and Computer-Assisted Intervention. Cham: Springer Nature Switzerland, 2023.\
 [6] Zhou, Hong-Yu, et al. "nnformer: Interleaved transformer for volumetric segmentation." arXiv preprint arXiv:2109.03201 (2021).\
 [7] Xie, Yutong, et al. "Cotr: Efficiently bridging cnn and transformer for 3d medical image segmentation." Medical Image Computing and Computer Assisted Intervention–MICCAI 2021: 24th International Conference, Strasbourg, France, September 27–October 1, 2021, Proceedings, Part III 24. Springer International Publishing, 2021.\
 [8] Ma, Jun, Feifei Li, and Bo Wang. "U-mamba: Enhancing long-range dependency for biomedical image segmentation." arXiv preprint arXiv:2401.04722 (2024).\
 [9] Myronenko, Andriy. "3D MRI brain tumor segmentation using autoencoder regularization." Brainlesion: Glioma, Multiple Sclerosis, Stroke and Traumatic Brain Injuries: 4th International Workshop, BrainLes 2018, Held in Conjunction with MICCAI 2018, Granada, Spain, September 16, 2018, Revised Selected Papers, Part II 4. Springer International Publishing, 2019.\
 [10] He, Yufan, et al. "Dints: Differentiable neural network topology search for 3d medical image segmentation." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2021.\
 [11] Auto3DSeg, MONAI 1.3.0, [LINK](https://github.com/Project-MONAI/tutorials/tree/ed8854fa19faa49083f48abf25a2c30ab9ac1c6b/auto3dseg)


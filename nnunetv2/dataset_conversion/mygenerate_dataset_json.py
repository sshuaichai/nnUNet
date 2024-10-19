from typing import Tuple
from batchgenerators.utilities.file_and_folder_operations import save_json, join

def generate_dataset_json(output_folder: str,
                          channel_names: dict,
                          labels: dict,
                          num_training_cases: int,
                          num_test_cases: int,
                          file_ending: str,
                          regions_class_order: Tuple[int, ...] = None,
                          dataset_name: str = None, reference: str = None, release: str = None, license: str = None,
                          description: str = None,
                          overwrite_image_reader_writer: str = None, **kwargs):
    """
    在输出文件夹中生成 dataset.json 文件

    channel_names:
        通道名称必须将索引映射到通道名称，例如：
        {
            0: 'T1',
            1: 'CT'
        }
        请注意，通道名称可能会影响归一化方案！！请在文档中了解更多信息。

    labels:
        这将告诉 nnU-Net 期望什么标签。重要的是：这也将决定是否使用基于区域的训练。
        示例普通标签：
        {
            'background': 0,
            'left atrium': 1,
            'some other label': 2
        }
        示例基于区域的训练：
        {
            'background': 0,
            'whole tumor': (1, 2, 3),
            'tumor core': (2, 3),
            'enhancing tumor': 3
        }

        请记住，nnU-Net 期望标签的值是连续的！nnU-Net 也期望 0 是背景！

    num_training_cases: 用于仔细检查所有案例是否都存在！

    num_test_cases: 用于记录测试集的案例数量！

    file_ending: 需要正确找到文件。重要！文件扩展名必须在图像和分割之间匹配！

    dataset_name, reference, release, license, description: 不用于 nnU-Net，只是为了完整性和提醒这是很重要的！

    overwrite_image_reader_writer: 如果需要为数据集使用特定的 IO 类，可以从 BaseReaderWriter 派生，放置在 nnunet.imageio 中，并在此处按名称引用

    kwargs: 这里放的任何内容都将放置在 dataset.json 中

    """
    has_regions: bool = any([isinstance(i, (tuple, list)) and len(i) > 1 for i in labels.values()])
    if has_regions:
        assert regions_class_order is not None, f"You have defined regions but regions_class_order is not set. " \
                                                f"You need that."
    # 通道名称需要字符串作为键
    keys = list(channel_names.keys())
    for k in keys:
        if not isinstance(k, str):
            channel_names[str(k)] = channel_names[k]
            del channel_names[k]

    # 标签需要整数作为值
    for l in labels.keys():
        value = labels[l]
        if isinstance(value, (tuple, list)):
            value = tuple([int(i) for i in value])
            labels[l] = value
        else:
            labels[l] = int(labels[l])

    dataset_json = {
        'channel_names': channel_names,  # 以前称为 'modality'。我不喜欢这个名字，所以现在是 channel_names。接受它吧。
        'labels': labels,
        'numTraining': num_training_cases,
        'numTest': num_test_cases,
        'file_ending': file_ending,
    }

    if dataset_name is not None:
        dataset_json['name'] = dataset_name
    if reference is not None:
        dataset_json['reference'] = reference
    if release is not None:
        dataset_json['release'] = release
    if license is not None:
        dataset_json['licence'] = license
    if description is not None:
        dataset_json['description'] = description
    if overwrite_image_reader_writer is not None:
        dataset_json['overwrite_image_reader_writer'] = overwrite_image_reader_writer
    if regions_class_order is not None:
        dataset_json['regions_class_order'] = regions_class_order

    dataset_json.update(kwargs)

    save_json(dataset_json, join(output_folder, 'dataset.json'), sort_keys=False)

# 调用函数生成 dataset.json 文件
output_folder = r"F:\nnUNet_raw\Dataset520_Rib"
channel_names = {
    0: "CT"  # 假设你的图像类型是CT
}
labels = {
    "background": 0,
    "rib_fracture": 1,
}
num_training_cases = 20
num_test_cases = 10
file_ending = ".nii.gz"
dataset_name = "Rib Fracture Dataset"
description = "This dataset contains rib fracture annotations for training nnU-Net models."

generate_dataset_json(output_folder, channel_names, labels, num_training_cases, num_test_cases, file_ending, dataset_name=dataset_name, description=description)

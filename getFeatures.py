# @Author   : 919106840638肖林航
# @time     : 2021/10/09 上午10:23
# @Software : PyCharm

import os

import h5py
import numpy as np
from VGGNET import VGGNet

path = "dataset/"
print("数据集：")
print(os.listdir(path))


# 获取数据集所有图片
def getAllPics(path):
    image_paths = []
    # 获取dataset/下所有数据集文件夹
    folders = os.listdir(path)
    # 遍历每个数据集
    for folder in folders:
        # print(folder)
        # 获取该数据集下所有子文件夹
        folders_1 = os.listdir(os.path.join(path, folder))
        # 遍历每个子文件夹
        for folder_1 in folders_1:
            # 获取所有子文件夹下所有文件
            ls = os.listdir(os.path.join(path, folder + "/", folder_1))
            # 遍历所有文件
            for image_path in ls:
                # 如果是.jpg格式才收录
                if image_path.endswith('jpg'):
                    # 路径连接
                    image_path = os.path.join(path, folder + "/", folder_1 + "/", image_path)
                    # print("正在获取图片   "+image_path)
                    # 存储
                    image_paths.append(image_path)
    # 返回所有图片列表
    return image_paths


# # 获取所有图片
img_list = getAllPics(path)
print("图片总数量：" + len(img_list).__str__() + "张")
print("--------------------------------------------------")
print(" 开始提取特征......   ")
print("--------------------------------------------------")

features = []
names = []

model = VGGNet()
for i, img_path in enumerate(img_list):
    norm_feat = model.get_feat(img_path)
    img_name = img_path
    features.append(norm_feat)
    names.append(img_name)
    print("正在提取图像特征：第 %d 张 , 共 %d 张......." % ((i + 1), len(img_list)) + img_name)

feats = np.array(features)
# print(feats)
# 用于存储提取特征的文件
output = "index.h5"

print("--------------------------------------------------")
print(" 正在将提取到的特征数据存储到文件中......")
print("--------------------------------------------------")

h5f = h5py.File(output, 'w')
h5f.create_dataset('dataset_1', data=features)
h5f.create_dataset('dataset_2', data=np.string_(names))
h5f.close()

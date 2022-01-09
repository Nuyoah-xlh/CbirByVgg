# 使用VGGNET16实现以图搜图-CBIR

​	题目选择：基于内容的图像检索-CBIR，为《媒体计算基础》课程的结课作品，另外一个早期的基于颜色特征、SIFT特征的图像检索系统项目：https://github.com/Nuyoah-xlh/CBIRBySiftAndColor

## 视频演示

项目的目录及运行测试视频地址： https://www.bilibili.com/video/BV1fQ4y1S7R5

## 项目结构

~~~bash
--/dataset          		#数据集存放目录
 --/101_ObjectCategories	#第一个数据集
  --/accordion				#第一个数据集的一个类别
   --image_0001.jpg			#第一个数据集下第一个类别的第一张图片
 ...
 --/256_ObjectCategories	#第二个数据集
  --/001.ak47				#第二个数据集的一个类别
   --001_0001.jpg			#第二个数据集下第一个类别的第一张图片
 ...
--/icon						#存放界面图标的目录
 --author.png				#目录下的一个图标
 ...
--/test_set					#用于测试的图像集
 --/external				#存放的是数据集外的图像，主要为百度搜集
  --1.jpg					
  ...
 --/inside					#存放的是数据集内的图像
  --1.jpg
  ...
--app.py					#程序入口文件
--getFeatures.py			#提取数据集所有VGG图像特征
--search.py					#用于搜索的处理文件
--SelectAndSearch.py		#选择图像并进行搜索的文件
--VGGNET.py					#VGG的类文件，用于构造VGG模型并进行特征提取
--index.h5					#存放提取到的所有特征及其关系
--README.md					#项目说明文件
--requirements.txt			#项目依赖说明文件，可执行此文件下载项目所需要的包
~~~

## 数据集

### 网盘下载

​	4个数据集全部压缩在一起，并上传百度网盘

​	链接：https://pan.baidu.com/s/1dDo7lMZoek9KCpcJeKvehA 

​	提取码：y235

### 官网下载

**（1）Caltech256数据集**

[地址1](https://drive.google.com/file/d/1r6o0pSROcV1_VwT4oSjA2FBUSCWGuxLK/view?usp=sharing)		[地址2](http://www.vision.caltech.edu/Image_Datasets/Caltech256/)

**（2）Caltech101数据集**

[地址1](https://drive.google.com/file/d/137RyRjvTBkBiIfeYBNZBtViDHQ6_Ewsp/view?usp=sharing)		[地址2](http://www.vision.caltech.edu/Image_Datasets/Caltech101/)

**（3）The Oxford Buildings Dataset数据集**

[地址](https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/oxbuild_images.tgz)

**（4）动物数据集**

[地址](https://www.kaggle.com/iamsouravbanerjee/animal-image-dataset-90-different-animals)（可能需要注册/登录）

## 快速开始

​	项目使用了4个数据集，并已提取完所有特征，可直接运行。cmd下运行方法：

~~~
pip install -r requirements.txt				#导入项目所需依赖
python app.py								#运行项目入口文件
~~~

**注意：**如果你想要更改或者重构数据集，你需要执行`python getFeatures.py`重新提取特征后，再执行`python app.py`运行。


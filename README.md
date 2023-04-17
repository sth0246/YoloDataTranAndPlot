# YoloDataTranAndPlot
车牌数据集（CCPD）转换YOLOv5数据集脚本，和YOLOv5 utils的plot修改文件，使其输出目标位置和图片
#### 本仓库用于记录HENU大三上学期课程创新项目实践（车牌识别）
实验指导书中使用了opencv和svm分别对图像预处理、定位和字符识别。我负责的是车牌预处理部分，由于在上学期（大二下）参加的比赛中使用到了yolov5和MediaPipe等深度学习框架，于是我在简单调研后使用了[CCPD2019数据集](https://github.com/detectRecog/CCPD)的base级别中的3000（自己电脑真不行，，，，3000张100轮训练跑了8个小时）张进行车牌预处理和车牌定位。
#### 本文仓库主要内容是CCPD转换YOLOv5数据集的插件和输出目标位置和图片的plots源码，这部分文件在utils目录下。

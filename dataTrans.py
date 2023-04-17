# -*- coding: utf-8 -*-
# @Time    : 2022/10/17 16:37
# @Author  : sth0246
# @File    : dataTrans.py
# @Description : 用于将CCPD数据集转换为YOLO数据集，使用前修改各个路径即可train_weight为训练集占比
from PIL import Image, ImageDraw, ImageFont
import os
import cv2


train_weight = 0.8

all_file_path_list = []

def get_all(cwd):
    count = 0
    get_dir = os.listdir(cwd)
    for i in get_dir:
        # count+=1
        # if count >= 10:
        #     break
        sub_dir = os.path.join(cwd, i)
        if os.path.isdir(sub_dir):
            get_all(sub_dir)

        else:
            all_file_path_list.append(i)
get_all('F:\yolo\carID\mydata')
# print(all_file_path_list)
# print(len(all_file_path_list))

def main( imgpath , staus):
    # 图像路径
    # 图像名
    imgname = os.path.basename(imgpath).split('.')[0]
#    print('imgname'+imgname)
    img = cv2.imread('mydata/'+imgpath)
#    print(img.shape)

    # 根据图像名分割标注
    _, _, box, points, label, brightness, blurriness = imgname.split('-')

    # --- 边界框信息
    box = box.split('_')
    box = [list(map(int, i.split('&'))) for i in box]
   # print(box)
    weight = img.shape[1]
    height = img.shape[0]
    x_min = box[0][0]
    x_max = box[1][0]
    y_min = box[0][1]
    y_max = box[1][1]
    x = (x_min+x_max)/(2*weight)
    y = (y_min+y_max)/(2*height)
    w = (x_max-x_min)/weight
    h = (y_max-y_min)/height
    # print(str(x_min)+' '+str(x_max)+' '+str(y_min)+' '+str(y_max))
    # print('shape'+str(weight)+str(height))
    if(staus == 'train'):
        cv2.imwrite('VOCdata/images/train/'+str(imgpath),img)
        tmp = open('VOCdata/labels/train/'+imgpath[0:-4]+'.txt','w+')
        tmp.writelines('0 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h))
        tmp.close()
    else:
        cv2.imwrite('VOCdata/images/val/'+str(imgpath), img)
        tmp = open('VOCdata/labels/val/' + imgpath[0:-4] + '.txt', 'w+')
        tmp.writelines('0 ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h))
        tmp.close()

    # # --- 关键点信息
    # points = points.split('_')
    # points = [list(map(int, i.split('&'))) for i in points]
    # # 将关键点的顺序变为从左上顺时针开始
    # points = points[-2:]+points[:2]
    #
    # # --- 读取车牌号
    # label = label.split('_')
    # # 省份缩写
    # province = provincelist[int(label[0])]
    # # 车牌信息
    # words = [wordlist[int(i)] for i in label[1:]]
    # # 车牌号
    # label = province+''.join(words)
    #
    # # --- 图片可视化
    #ImgShow(imgpath, box, points, label)
t = 0
for i in all_file_path_list:
    t+=1
    print('正在处理'+str(t)+'/'+str(len(all_file_path_list))+'张照片')
    if(t+1) <= train_weight*(len(all_file_path_list)+1):
        main(i,'train')
    else:
        main(i,'val')

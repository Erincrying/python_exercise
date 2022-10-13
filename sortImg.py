#!/usr/bin/env python3
# -*- coding:utf8 -*-

import os
import shutil

class getNewFileList():
    def __init__(self):
        self.path = 'F:/data/dlqx/datasets/test_imgs/kodak/'  #表示需要命名处理的文件夹目录，复制地址后注意反斜杠
        self.new_img_folder = "F:/data/dlqx/datasets/test_imgs/sortKodak"
        self.imgNum = 10

    def sortFile(self):
        originalList = os.listdir(self.path)   #获取文件路径
        # print(originalList, 'originalList') # 图片名称，kodim20.png
        # 拼接全路径
        newList = list()
        for imgName in originalList:
          itemPath  = self.path + imgName
          newList.append(itemPath)
        # print(newList,'newList') # path全称
        # 给文件中的图片按从大到小进行排序
        sort_list = list()
        sort_list = sorted(newList,key=lambda file: os.path.getsize(file),reverse=True)
        # print(sort_list, '排序后')
        # 复制到新文件夹
        for index in range(self.imgNum):
          # print(sort_list[index], 'sort_list[index]')
          shutil.copy(sort_list[index], self.new_img_folder)
                

if __name__ == '__main__':
    demo = getNewFileList()
    demo.sortFile()
    


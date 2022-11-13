# -*- coding: utf-8 -*-
# weibifan 2016-11-12
# 执行外部程序，并获得程序结果

import sys
import os
from subprocess import *
#基本思路：读入文件夹下的每个文件，调用java程序处理，将屏幕输出结果保存到一个文件中
root_path = r"data"
write_file = r"triple\result.txt"
fw = open(write_file,"w")
cmd_base="java  CoNLL2Triple "
#包括文件及目录
files = os.listdir(root_path)
##print files
index = 0
for file in files:
  #打印指示
  if not index % 1000: print(index) 
  index = index + 1
  #执行程序
  file_path = root_path +"\\"+  file
  name,ext =os.path.splitext(file)
  cmd = cmd_base + file_path + " " + name
  #print cmd
  f = Popen(cmd, shell = True, stdout = PIPE).stdout 
  #逐行处理屏幕输出
  line = f.readline()
  while line:
    fw.write(line)
    line = f.readline()
fw.close()
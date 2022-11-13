# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:28:05 2016

@author: wei
"""
#==============================================================================
# 基本库
#1、随机数
#2、NumPy
#3、Image processing
#==============================================================================
import numpy as np

b_shp = (2,)
rng = np.random.RandomState(23455)
b=np.asarray(
  rng.uniform(low=-.5, high=.5, size=b_shp),
  dtype=input.dtype)
  

#==============================================================================
# 多维数组 不是 矩阵（2d数组）
# 缺省情况下并不使用矩阵运算，如果你希望对数组进行矩阵运算的话，可以调用相应的函数。
#==============================================================================


#==============================================================================
# SciPy
#==============================================================================
from scipy import misc
import pylab as pl


myi = misc.lena()

pl.imshow(myi)

type(myi)

misc.imsave('lena.png', myi)
lena = misc.imread('lena.png')

#==============================================================================
# PIL （Python Imaging Library）
#==============================================================================
from PIL import Image
import numpy as np


# open random image of dimensions 639x516
img = Image.open('lenna.jpg')
#应 RGB
print img.format, img.size, img.mode
# OUT : JPEG (256, 256) RGB

img.show()
#img （256，256，3）
imga = np.asarray(img, dtype='float64') / 256.

# put image in 4D tensor of shape (1, 3, height, width)
img_ = imga.swapaxes(0, 2).swapaxes(1, 2)
img4d = imga.swapaxes(0, 2).swapaxes(1, 2).reshape(1, 3, 256, 256)


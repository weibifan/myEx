# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:11:07 2016

@author: Administrator
"""

#==============================================================================
# 
#==============================================================================
from scipy import misc
import pylab as pl


myi = misc.lena()

pl.imshow(myi)

type(myi)

misc.imsave('lena.png', myi)
lena = misc.imread('lena.png')


#==============================================================================
# 
#==============================================================================
import scipy as sp
import numpy as np
from scipy import signal
a = [[1,2,3],[3,4,5]]
b = [[2,3,4],[4,5,6]]
#先对b旋转180
c = signal.convolve2d(a,b,'full','wrap')
#mode=full 表示扩展式，结果=a的长度+（b的长度-1）
#mode=valid 比a小，只计算b落入a之中的，结果=a的长度-（b的长度-1）
#mode=same  与a相同

#boundary=wrap  a进行平铺（平移）
#boundary=fill  使用0值填充
#boundary=symm  a进行对称平铺
c1 = signal.convolve2d(a,b,'full','symm')

d = np.array([[80,80,74,80,80],\
    [68,68,62,68,68],\
    [80,80,74,80,80]])
np.assert_array_equal(c,d)


#==============================================================================
# 
#==============================================================================
import matplotlib.pyplot as plt
from scipy import signal
lena=misc.lena()  #二维数组，512*512矩阵
image = misc.lena().astype(np.float32)

#laplacian核
laplacian = np.array([[0,1,0], [1,-4,1], [0,1,0]], dtype=np.float32)

deriv2 = signal.convolve2d(image,laplacian,mode='same',boundary='symm')

plt.figure()
plt.imshow(image)
plt.title('Original image')
plt.show()

plt.figure()
plt.imshow(deriv2)
plt.title('Output of spline edge filter')
plt.show()



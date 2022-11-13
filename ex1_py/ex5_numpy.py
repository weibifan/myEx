# -*- coding: utf-8 -*-
"""
Created on Tue May 03 08:46:30 2016

@author: wei

Python numpy 矩阵及自动扩展

d1 =numpy.array([1,2,3])  (3L,)  是一个行向量
在spyder显示时显示成列向量


"""

#%%

import numpy

#%%

# list 与 array 列向量只对array有效，list没有行列的概念
c0 = [1,2]
c1 = [1,2,3] #list 不是array
d1 =numpy.array([1,2,3])
print d1.shape #(3L,)  是一个行向量，但是在spyder中显示为列向量。

c2 = numpy.array([[1],[2],[3]])
print c2.shape #(3L, 1L)  是一个矩阵，但是只有一列

c3 =numpy.array( [[1,2,3]])
print c3.shape #(1L, 3L)  是一个矩阵，但是只有一行

c4 = numpy.ones((5)) ;
print c4.shape  (3L,) 

#%%
''' numpy 自动扩展：不同维度的加运算
向量+标量：
矩阵+向量：分为按行，按列
矩阵+标量：
'''
a = numpy.array([[1,2,3],[4,5,6],[7,8,9]])

myadd= a + d1  #d1按行向量扩展
myadd2 =a + c1 

myadd3= a + c2
myadd4=a + c3

myadd5=a + 10



#myadd6 =a + c0  #编译错误

#%%
b_shp = (2,3)
rng = numpy.random.RandomState(23455)
b=numpy.asarray(
  rng.uniform(low=0, high=.5, size=b_shp),dtype='float32')


#%%

          
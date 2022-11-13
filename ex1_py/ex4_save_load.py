# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 20:37:53 2016

@author: Administrator
"""

#==============================================================================
# 
#==============================================================================
# 数据加载与保存
# 1）text 方式,numpy.savetxt()
# 2）bin方式，numpy.save()
# 3）压缩的bin方式，需要cPickle包


import cPickle, gzip, numpy

#%%
# Load the dataset
f = gzip.open('mnist.pkl.gz', 'rb')
ds=cPickle.load(f) 
#ds是三个元素的tuple，分别为train_set, valid_set, test_set
train_set, valid_set, test_set = ds
#train_set 2个元素的tuple，第1个元素是二维数组，每行一个图片，共28*28=784列
#                         第2个元素是1维数组，针对每行是0-9之间的一个值
#train_set 5万，valid_set是1万，test_set是1万

f.close()

a = train_set[0][1].reshape(28,28)  #可以作为图片显示
a = numpy.reshape(train_set[0][1],(28,28))

#%%

import numpy as np
#==============================================================================
# 
# 多维数组 不是 矩阵（2d数组）
#缺省情况下并不使用矩阵运算，如果你希望对数组进行矩阵运算的话，可以调用相应的函数。
#==============================================================================
fname="array/Wiki_property_text/property.txt"
delimiter=" "
mymatrix=np.loadtxt(fname,dtype=np.float,delimiter=delimiter)
mymatrix2=np.asmatrix(mymatrix)
mymatrix2.shape




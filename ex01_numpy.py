# -*- coding: utf-8 -*-
# weibifan 2022-10-1
# 广播机制，broadcasting semantics --- Nympy及PyTorch所独有

import numpy as np

# Numpy中的数组shape为（m,）说明它是一个一维数组，没有向量的概念。
# 在与矩阵进行矩阵乘法时，numpy会自动判断此时的一维数组应该取行向量还是列向量。

# a30_v13，0表示时数组。v13表示1行3列，也就是行向量。
a30_v13 = np.array([10, 20, 30])  # 没有向量的概念，显示时是行向量方式。
print("a1 shape=", a30_v13.shape) #(3,) 形式像个列向量，但是不是。

a33 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  #矩阵，2重list，shape为(3,3)
test = a33 + a30_v13 #广播时，只能按行扩展，且不能自动转换。
print(test)
'''
[[11 22 33]
 [14 25 36]
 [17 28 39]]
'''

# 数组只能按行进行扩展，无法自动转换为列向量。
a34 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11,12] ])

test3= a34 + a30_v13 #无法进行广播
print(test3)

# 如果想让数组进行列传播，需要将数组转化为列向量。


# ===================================================
a31 = np.array([[1], [2], [3]]) #只有1列的二维矩阵
print("a31=",a31.shape)
test2= a30_v13 + a31  #双向传播，a1按行传播，a31按列传播，然后相加
print(test2)
'''
[[11 21 31]
 [12 22 32]
 [13 23 33]]
'''
# ===================================================

# 数组shape为（m,），只能按行传播，如果想按列传播，需要先转换为列向量。
a2 = np.expand_dims(a30_v13, 1) #只有1列的二维矩阵
print("a2 shape=", a2.shape) #(3,1)

#x与a2相同
x = np.array([[10], [20], [30]]) #只有1列的二维矩阵
print("x=",x.shape)  #(3,1)

test = a33 + a2 #按列扩展
print(test)

test4 = a34 + a2 #按列扩展
print(test4)

a2x = np.expand_dims(a30_v13, 0) #只有1行的二维矩阵
print("a2 shape=", a2x.shape) #(1,3)
print("inner product=", a2x * a2x) #内积不分向量和数组，只要长度相同就按要素相乘。

# 构造一个向量：第1步构建一个数组，第2步将数组转化为列向量或行向量。
a3 = np.arange(10) #数组
print("vector=", a3.shape)

a4 = np.expand_dims(a3, 1)
print("vector=", a4.shape)

# 内积=按元素相乘，长度相同就行。不用区分数组还是向量，不用对向量进行转置。
b=a3 * a3;
print("b=", b)


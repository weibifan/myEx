# -*- coding: utf-8 -*-
# weibifan 2022-10-1
# 广播机制，broadcasting semantics --- Nympy及PyTorch所独有

import numpy as np

# Numpy中的数组shape为（m,）说明它是一个一维数组，没有向量的概念。
# 在与矩阵进行矩阵乘法时，numpy会自动判断此时的一维数组应该取行向量还是列向量。

a33 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

a1 = np.array([10,20,30])  # 没有向量的概念，显示时是行向量方式。
print("a1 shape=", a1.shape) #(3,)

test = a33 + a1 #广播时，按行扩展
print(test)

a2 = np.expand_dims(a1, 1) #只有1列的二维矩阵
print("a2 shape=", a2.shape) #(3,1)

#x与a2相同
x = np.array([[10], [20], [30]]) #只有1列的二维矩阵
print("x=",x.shape)

test = a33 + a2 #按列扩展
print(test)

# 构造一个向量
a3 = np.arange(10) #数组
print("vector=", a3.shape)

a4 = np.expand_dims(a3, 1)
print("vector=", a4.shape)

# 内积=按元素相乘，不用对向量进行转置。
b=a3 * a3;
print("b=", b)

a34 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11,12] ])

test2=a34 + a1 #无法进行广播
print(test2)
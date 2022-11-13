# -*- coding: utf-8 -*-
'''
块注释
'''
#%%
name = ['sam', 'jimmy']

print 'hello'

#%%
# 基本数据类型
tup1=(9)  #是一个数值
tup2=(9,) #是一个list

#%%
lists = [x for x in range(10)]
print(lists)

#%%
import numpy

a=numpy.arange(15)  #a是narray
b=range(15)  #b是list

'''
做循环的时候，尽量使用xrange()函数
xrange与range的用法完全相同，但是 range() 返回的是一个列表，而xrange() 返回的是一个生成器。在返回很大的值的时候，使用xrange的性能比较好。
'''

#列表深复制
a = [1,2,3]
b = a[:]

#zip函数
a = [1,2,3]
b = [4,5,6]
zippend = zip(a,b)
# zippend = [(1,4),(2,5),(3,6)]
zip(*zippend)
# [(1,2,3),(4,5,6)]

#list像栈一样使用。
stack = [1,2,3]
# 先进元素4，5
stack.append(4)
stack.append(5)
# 先出元素5，4
stack.pop() # 删除元素5
stack.pop() # 删除元素4
stack 
# [1,2,3]


weibifan 2022-10-3  
Python语法，Python面向对象编程  

### Python 概述

Python是面向对象和面向过程混合 --- 类似于C++，但是借鉴了Java的GC  
1）通过构造函数创建对象，可能进行赋值。Java使用new创建对象。  
2）显式使用self指针，Java默认使用this  
3）大量使用类里面的static函数。 2种使用方法，①类名.func()，②对象.func()  
4）类后面的括号表示继承，Java是使用类后面的冒号  
5）名称空间（package）中大量函数，没有放到对象中。  
6）默认都是指针引用，自动构建对象，系统自动回收。要复制对象需要使用深拷贝。  
7）__xxx()__，表示预留函数，或者必须重载的函数。  
8）函数默认是值传递。  
9）使用冒号和缩进表示代码块，缩进={}。续行符(\)。
10）



面向对象编程：
- 构造函数def __init__(self) 是静态函数。   
- 支持多重继承，类似于java---使用interface

中文教程：https://github.com/jackfrued/Python-100-Days 不完整   
中文书：https://github.com/ethan-funny/explore-python   
https://pythonguidecn.readthedocs.io/zh/latest/  
https://python3-cookbook.readthedocs.io/zh_CN/latest/  
英文小抄：https://github.com/gto76/python-cheatsheet  

### 高效获得帮助
自带本地帮助，官方网站帮助，教学PPT,权威手册。使用内置函数获得package信息
Import nltk
Dir(nltk)
Help(nltk)

### 注释  中文注释问题需要设置UTF-8

多行注释（""")中识别unicode。  添加r，不在识别。   
\ 来实现多行语句。在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \  
字符串中 转义符 \ 指Unicode编码  
r''' '''
### lambda，yield

lambda：匿名函数， 类似于C++ inline函数  
方式1：
`sum = lambda arg1, arg2: arg1 + arg2`
方式2：等价于方式1。
`def sum(arg1, arg2):  
    return arg1 + arg2`

```python
sum = lambda arg1, arg2: arg1 + arg2
print(sum(10,20))  #输出30
```

yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数。  
带yield指令的函数，类似一个迭代类。  
iter = fun()  #该函数包含yield指令。这句生成一个iterator对象。  
iter.next() #使用该函数  

```python
def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return
```

### 函数：  默认是值传送

###  字符串格式化，s f b  % 等
r 指 raw，即 raw string，会自动将反斜杠转义，  
`print('\n')`       # 输出空行  
`print(r'\n')`     # 输出 \n  

%：1）取模 。2）format string，所有类型转化成字符串，然后拼接



### 标准库：sys，os，shutil，glob包    
内置模块(buildin)：函数有help(), type(), sorted(), sum(), len(), range(), reduce(), apply(), eval(), hash()等。

```python
import os
if not os.path.isdir('./.data'):
    os.mkdir('./.data')

import os
dir(os)
help(os)

import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')
```

### 基本数据类型及操作
- 列表（方括号） list[]  python的主力数据结构，索引为整数的字典。下标从0开始，动态增删，不同类型。
- 元组（圆括号） tuple ()  元组的元素不能修改。但是支持拼接。
- 字典（大括号） dict {}  json， 索引为字符串的list，jason。    类似于java的Map。  
dic = {'jay':'boy','may"':'girl'}
- 数组array：python的一个package，只能存放相同类型的元素。

tup1=(9)  是一个int值，只有一个元素9。数字表达式中有括号，比如(9+5)*6，此时括号内是一个值。  
tup2=(9,)，是一个元组，该元组里面只有一个元素9  
list1=[1] list  
list2=[1,] 也是list  

```python
list = ['Google', 'Runoob', 1997, 2000] #序号从0开始
del list[2] # 删除第3个元素。
list.append('Baidu') # 在末尾增加一个元素
list[1] = 'ByteDance' # 修改一个元素
list[2:4] #投影，第3，第4个要素，不包括第5个要素（不包括4对应要素）。
```
支持的操作：+（拼接），*（重复），in （元素判断）  ，列表的比较

import operator
operator.eq(list, list[1:]) 

索引（下标）和切片(x:y形式)：从0开始，可以是负值，表示逆序计算。可以操作列表，元组。
赋值：数组赋值，比如a，b=b,a  交换赋值
排序：

Ellipsis（省略号“...”）     
 1)用在切片中，针对多维数组，表示其他维度，要么是首尾之外的维度，要么是最后一个维度其他的维度。多维数组的索引为a[x,y,z]等，每个维度都可以用切片。
 2）续行。一行太长。


### with 关键字  用于异常处理，封装了 try…except…finally 编码范式，提高了易用性。   

```python
with open('./test_runoob.txt', 'w') as file:
    file.write('hello world !')
# with 关键字系统会自动调用 f.close() 方法， with 的作用等效于 try/finally 语句是一样的。

file = open('./test_runoob.txt', 'w')
try:
    file.write('hello world')
finally:
    file.close()
```

### 装饰符：@

### Import  import subprocess as xx，不推荐from subprocess import *
区别：
import subprocess：
1）只是引入该名称，使用该包内的内容（函数，常量，子包）必须要使用subprocess这个前缀。
比如：subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE).communicate()
2）可以使用缩写，比如：import subprocess as subp
from subprocess import *：表示引入subprocess内的所有内容，不需要再使用subprocess前缀了
比如：Popen(cmd, shell = True, stdout = PIPE).communicate()


### Jupyter-Notebook
C:\Anaconda2\Scripts目录下有jupyter-notebook.exe，然后双击
打开浏览器 http://localhost:8888  默认目录是C:\Anaconda2\Scripts

### 虚拟环境
Anaconda和Python安装包都会构建一个默认的虚拟环境，称为base，不指定时默然安装的各种包都在这个环境下。  
如果创建了虚拟环境，安装的包都是安装在这个虚拟环境下。所以需要一个虚拟环境启动的过程。  

Conda是一个开源包管理系统和环境管理系统，可在Windows、macOS和Linux上运行。  
在Windows上大部分时间都出错，不知道为啥。  

PyCharm支持不同的虚拟环境。  
在相同硬件下，只需要拷贝虚拟环境的目录就行。  
在不同硬件下，需要重新构建虚拟环境，比如某台机器配置有GPU加速卡。  

### 开发环境
Anaconda是一个免费开源的Python和R语言的发行版本，用于计算科学，  
Anaconda致力于简化包管理和部署。Anaconda的包使用软件包管理系统Conda进行管理。  

PyCharm

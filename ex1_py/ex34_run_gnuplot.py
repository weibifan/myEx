# Python调用gnuplot：原始方法，之间和gnuplot的shell交互
# 使用这种方法，只能调用splot，不能调用plot
import os, sys, traceback
import getpass
from threading import Thread
from subprocess import *

gnuplot_exe = r"D:\Download\gp440win32\gnuplot\binary\gnuplot.exe"
assert os.path.exists(gnuplot_exe), "gnuplot executable not found"
# a=[(10,2,30),(4,5,6),(10,8,9)]
# print a
# a.sort(key=lambda x:(x[0],-x[1]))
# print a
gnuplot = Popen(gnuplot_exe, stdin=PIPE).stdin
gnuplot.write("set term windows\n".encode())
gnuplot.write("set contour\n".encode())
gnuplot.write("set view 90,90\n".encode())
# gnuplot.write("splot \"-\" with lines\n".encode())
gnuplot.write("splot  x**2+y**2 \n".encode())
# gnuplot.write("splot  sin(y) \n".encode())

gnuplot.flush()
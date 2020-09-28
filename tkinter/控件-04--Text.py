#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-09-28 20:56:22
# Author : zijing (zijing412@163.com)
###################################################

# 常用方法
# delete(起始位置，[,终止位置])	删除指定区域文本
# get(起始位置，[,终止位置])	获取指定区域文本
# insert(位置，[,字符串]...)	将文本插入到指定位置
# see(位置)	在指定位置是否可见文本，返回布尔值
# index(标记)	返回标记所在的行和列
# mark_names()	返回所有标记名称
# mark_set(标记，位置)	在指定位置设置标记
# mark_unset(标记)	去除标记

# 上表位置的取值可为整数，浮点数或END（末尾），例如0.0表示第0列第0行

from tkinter import *
import time
import datetime

def gettime():
       s=str(datetime.datetime.now())+'\n'
       txt.insert(END,s)
       root.after(1000,gettime)  # 每隔1s调用函数 gettime 自身获取时间

root=Tk()
root.geometry('320x240')
txt=Text(root)
txt.pack()
gettime()
root.mainloop()
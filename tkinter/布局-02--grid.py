#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-09-22 20:23:14
# Author : zijing (zijing412@163.com)
###################################################
from tkinter import *

# grid()方法：是基于网格的布局
# 先虚拟一个二维表格，再在该表格中布局控件实例。
# 由于在虚拟表格的单元中所布局的控件实例大小不一，单元格也没有固定或均一的大小，
# 因此其仅用于布局的定位。
# pack()方法与grid()方法不能混合使用。

# grid()方法常用布局参数如下：
# column: 控件实例的起始列，最左边为第0列。
# columnspan: 控件实例所跨越的列数，默认为1列。
# ipadx,ipady: 控件实例所呈现区域内部的像素数，用来设置控件实例的大小。
# padx,pady: 控件实例所占据空间像素数，用来设置实例所在单元格的大小。
# row: 控件实例的起始行，最上面为第0行。
# rowspan: 控件实例的起始行数，默认为1行。

# 代码目标
# 用grid()方法排列标签，
# 设想有一个3x4的表格，
# 起始行、列序号均为0.
# 将标签lbred 至于第2列第0行；
# 将标签lbgreen置于第0列第1行；
# 将标签lbblue置于第1列起跨2列；第2行，占20像素宽。


root = Tk()

lbred = Label(root,text="Red",fg="Red",relief=GROOVE)
lbred.grid(column=2,row=0)
lbgreen = Label(root,text="绿色",fg="green",relief=GROOVE)
lbgreen.grid(column=0,row=1)
lbblue = Label(root,text="蓝",fg="blue",relief=GROOVE)
lbblue.grid(column=1,columnspan=2,ipadx=20,row=2)
root.mainloop()
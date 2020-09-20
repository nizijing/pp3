#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-09-20 14:59:53
# Author : zijing (zijing412@163.com)
###################################################

from tkinter import *

def test1(): 
    # 全部默认
    # 是一种简单的布局方法，如果不加参数的默认方式，将按布局语句的先后，以最小占用空间的方式自上而下地排列控件实例，并且保持控件本身的最小尺寸。
    root = Tk()

    lbred = Label(root,text="Red",fg="Red",relief=GROOVE)
    lbred.pack()
    lbgreen = Label(root,text="绿色",fg="green",relief=GROOVE)
    lbgreen.pack()
    lbblue = Label(root,text="蓝",fg="blue",relief=GROOVE)
    lbblue.pack()
    root.mainloop()

def test2():
    # 使用pack()方法可设置 fill、side 等属性参数。
    # 其中，参数fill 可取值：fill=X,fill=Y或fill=BOTH，
    # 分别表示允许控件向水平方向、垂直方向或二维伸展填充未被占用控件。
    # 参数 side 可取值：side=TOP(默认),LEFT,RIGHT,BOTTOM
    # 分别表示本控件实例的布局相对于下一个控件实例的方位

    root = Tk()

    lbred = Label(root,text="Red",fg="Red",relief=GROOVE)
    lbred.pack()
    lbgreen = Label(root,text="绿色",fg="green",relief=GROOVE)
    lbgreen.pack(side=RIGHT)
    lbblue = Label(root,text="蓝",fg="blue",relief=GROOVE)
    lbblue.pack(fill=X)
    root.mainloop()

test1()
test2()
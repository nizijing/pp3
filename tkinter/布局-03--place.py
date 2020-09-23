#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-09-23 20:59:51
# Author : zijing (zijing412@163.com)
###################################################
from tkinter import *

# place()方法：根据控件实例在父容器中的绝对或相对位置参数进行布局。其常用布局参数如下：
# x,y：控件实例在根窗体中水平和垂直方向上的其实位置（单位为像素）。注意，根窗体左上角为0,0,水平向右，垂直向下为正方向。
# relx,rely：控件实例在根窗体中水平和垂直方向上起始布局的相对位置。即相对于根窗体宽和高的比例位置，取值在0.0~1.0之间。
# height,width：控件实例本身的高度和宽度（单位为像素）。
# relheight,relwidth：控件实例相对于根窗体的高度和宽度比例，取值在0.0~1.0之间。

# 利用place()方法配合relx,rely和relheight,relwidth参数所得的到的界面可自适应根窗体尺寸的大小。
# place()方法与grid()方法可以混合使用。如下例子：利用place()方法排列消息（多行标签）。


root = Tk()
root.geometry('320x240')

msg1 = Message(root,text='''我的水平起始位置相对窗体 0.2，垂直起始位置为绝对位置 80 像素，我的高度是窗体高度的0.4，宽度是200像素''',relief=GROOVE)
msg1.place(relx=0.2,y=80,relheight=0.4,width=200)
root.mainloop()

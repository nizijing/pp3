#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-10-12 19:41:07
# Author : zijing (zijing412@163.com)
###################################################
# 滑块：(Scale) 是一种 直观地进行数值输入的交互控件，其主要属性见下表
# from_	起始值（最小可取值）
# lable	标签文字，默认为无
# length	滑块控件实例宽（水平方向）或 高（垂直方向），默认为100像素
# orient	滑块控件实例呈现方向，VERTCAL或HORIZONTAL(默认)
# repeatdelay	鼠标响应延时，默认为 300ms
# resolution	分辨精度，即最小值间隔
# sliderlength	滑块宽度，默认为30 像素
# state	状态，若设置 state=DISABLED,则滑块控件实例不可用
# tickinterval	标尺间隔，默认为0，若设置过小，则会重叠
# to	终止值(最大可取值)
# variable	返回数值类型，可为IntVar(整数)、DoubleVar(浮点数)、或 StringVar(字符串)
# width	控件实例本身的宽度，默认为15像素


# 滑块控件实例的主要方法比较简单，有 get()和set(值)，分别为取值和将滑块设在某特定值上。
# 滑块实例也可绑定鼠标左键释放事件<ButtoonRelease-1>,并在执行函数中添加参数event来实现事件响应。
# 例如：在一个窗体上设计一个200像素宽的水平滑块，取值范围为1.0~5.0，分辨精度为0.05，刻度间隔为 1，
# 用鼠标拖动滑块后释放鼠标可读取滑块值并显示在标签上。效果如下：

from tkinter  import  *

def show(event):
    s = '滑块的取值为' + str(var.get())
    lb.config(text=s)

root = Tk()
root.title('滑块实验')
root.geometry('320x180')
var=DoubleVar()
scl = Scale(root,orient=HORIZONTAL,length=200,from_=1.0,to=5.0,label='请拖动滑块',tickinterval=1,resolution=0.05,variable=var)
scl.bind('<ButtonRelease-1>',show)
scl.pack()

lb = Label(root,text='')
lb.pack()

root.mainloop()

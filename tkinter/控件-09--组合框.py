#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-10-10 18:16:33
# Author : zijing (zijing412@163.com)
###################################################
# 组合框：(Combobox) 实质上是带文本框的上拉列表框，
# 其功能也将是Python 的列表类型数据可视化呈现，并提供用户单选或多选所列条目以形成人机交互。
# 在图形化界面设计时，由于其具有灵活的界面，因此往往比列表框更受喜爱。
# 但该控件并不包含在 tkinter 模块中，而是与 TreeView、Progressbar、Separator等控件一同包含在tkinter 的子模块ttk中。
# 如果使用该控件，应先与from tkinter import ttk 语句引用ttk子模块
# 创建组合框实例： 实例名=Combobox(根对象,[属性列表]), 指定变量var=StringVar(),并设置实例属性 textvariable = var,values=[列表...]。
# 组合框控件常用方法有：获得所选中的选项值get()和获得所选中的选项索引current()。
# 例子：实现四则运算计算器，将两个操作数分别填入两个文本框后，通过选择组合框中的算法触发运算

from tkinter.ttk import *
from tkinter import *

def calc(event):
    a = float(t1.get())
    b = float(t2.get())
    dic = {0:a+b,1:a-b,2:a*b,3:a/b}
    c = dic[comb.current()]
    lbl.config(text=str(c))

root = Tk()
root.title('四则运算')
root.geometry('320x240')

t1 = Entry(root)
t1.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.1)

t2 = Entry(root)
t2.place(relx=0.5,rely=0.1,relwidth=0.2,relheight=0.1)

var = StringVar()

comb = Combobox(root,textvariable=var,values=['加','减','乘','除',])
comb.place(relx=0.1,rely=0.5,relwidth=0.2)
comb.bind('<<ComboboxSelected>>',calc)

lbl=Label(root,text='结果')
lbl.place(relx=0.5,rely=0.7,relwidth=0.2,relheight=0.3)

root.mainloop()
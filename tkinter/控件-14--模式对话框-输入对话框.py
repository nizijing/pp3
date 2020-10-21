#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-10-21 20:17:43
# Author : zijing (zijing412@163.com)
###################################################
# 输入对话框: 引用tkinter.simpledialog包
# 可弹出输入对话框，用以接收用户的简单输入
# 常用 askstring()、askfloat()和askfloat() 三种函数，分别用于接收字符串、整数和浮点数类型的输入


from tkinter.simpledialog import *

def xz():
    s=askstring('请输入','请输入一串文字')
    lb.config(text=s)

root = Tk()

lb = Label(root,text='')
lb.pack()
btn=Button(root,text='弹出输入对话框',command=xz)
btn.pack()
root.mainloop()

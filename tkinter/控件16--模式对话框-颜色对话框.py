#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-10-25 15:04:55
# Author : zijing (zijing412@163.com)
###################################################
# 引用tkinter.colorchooser包，可使用 askcolor()函数弹出模式颜色选择对话框，让用户可以个性化地设置颜色属性。
# 该函数的返回形式为包含RGB十进制浮点元组和RGB十六进制字符串的元组类型，
# 例如：“((135.527343.52734375,167.65234375,186.7265625)),'#87a7ba'”。
# 通常，可将其转换为字符串类型后，再截取以十六进制数表示的RGB颜色字符串用于为属性赋值。

from tkinter import *
import tkinter.colorchooser

def xz():
    color=tkinter.colorchooser.askcolor()
    colorstr=str(color)
    print('打印字符串%s 切掉后=%s' % (colorstr,colorstr[-9:-2]))
    lb.config(text=colorstr[-9:-2],background=colorstr[-9:-2])

root = Tk()

lb = Label(root,text='请关注颜色的变化')
lb.pack()
btn=Button(root,text='弹出颜色选择对话框',command=xz)
btn.pack()
root.mainloop()
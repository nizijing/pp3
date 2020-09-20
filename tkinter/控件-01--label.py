#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-09-20 14:39:43
# Author : zijing (zijing412@163.com)
###################################################
from tkinter import Tk, Label, SUNKEN

root = Tk()
lb = Label(root,text='我是第一个标签',\
    bg='#d3fbfb',\
    fg='red',\
    font=('华文新魏',32),\
    width=20,\
    height=2,\
    relief=SUNKEN)
lb.pack()
root.mainloop()

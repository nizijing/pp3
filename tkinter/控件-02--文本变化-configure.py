#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-09-24 19:22:37
# Author : zijing (zijing412@163.com)
###################################################
import tkinter
import time

def gettime():
    timestr = time.strftime("%H:%M:%S") # 获取当前的时间并转化为字符串
    lb.configure(text=timestr)   # 重新设置标签文本
    root.after(1000,gettime) # 每隔1s调用函数 gettime 自身获取时间

root = tkinter.Tk()
root.title('时钟')

lb = tkinter.Label(root,text='',fg='blue',font=("黑体",80))
lb.pack()
gettime()
root.mainloop()

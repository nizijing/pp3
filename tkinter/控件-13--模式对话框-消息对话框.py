#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-10-16 20:31:36
# Author : zijing (zijing412@163.com)
###################################################
# 模式对话框(Modal)：是相对于前面介绍的非模式窗体而言的，所弹出的对话框必须应答，在关闭之前无法操作其后面的其他窗体。
# 常见的模式对话框有消息对话框、输入对话框、文件选择对话框、颜色选择对话框等。

# 交互对话框
# 消息对话框: 引用 tkinter.messagebox 包，可使用消息对话框函数。
# 执行这些函数，可弹出模式消息对话框，并根据用户的响应但会一个布尔值。其通式为：消息对话框函数(<title=标题文本>,<message=消息文本>,[其他参数])

# tkinter.messagebox.showinfo(title='Hi', message='你好！')
# tkinter.messagebox.showwarning(title='Hi', message='警告！')
# tkinter.messagebox.showerror(title='Hi', message='出错了！') 
# tkinter.messagebox.askquestion(title='Hi', message='你好！')
#   返回'yes', 'no'：
# tkinter.messagebox.askyesno(title='Hi', message='你好！')
#   返回true、false
# tkinter.messagebox.askokcancel(title='Hi', message='你好！')
#   返回true、false

from tkinter import *
import tkinter.messagebox

def xz():
    answer=tkinter.messagebox.askokcancel('请选择','请选择确定或取消')
    if answer:
        lb.config(text='已确认')
    else:
        lb.config(text='已取消')

root = Tk()

lb = Label(root,text='')
lb.pack()
btn=Button(root,text='弹出对话框',command=xz)
btn.pack()
root.mainloop()

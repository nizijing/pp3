#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-10-15 19:38:56
# Author : zijing (zijing412@163.com)
###################################################
# 子窗体：用Toplevel可新建一个显示在最前面的子窗体，
# 其通式为： 字体实例名=Toplevel(根窗体)，
# 子窗体与根窗体类似，也可设置title、geomerty等属性，并在画布上布局其他控件。
# 如下的例子：在根窗体上创建菜单，触发创建一个新的窗体


from tkinter import *

def newwind():
    winNew = Toplevel(root)
    winNew.geometry('320x240')
    winNew.title('新窗体')
    lb2 = Label(winNew,text='我在新窗体上')
    lb2.place(relx=0.2,rely=0.2)
    btClose=Button(winNew,text='关闭',command=winNew.destroy)
    btClose.place(relx=0.7,rely=0.5)

root = Tk()
root.title('新建窗体实验')
root.geometry('320x240')

lb1 = Label(root,text='主窗体',font=('黑体',32,'bold'))
lb1.place(relx=0.2,rely=0.2)

mainmenu = Menu(root)
menuFile = Menu(mainmenu)
mainmenu.add_cascade(label='菜单',menu=menuFile)
menuFile.add_command(label='新窗体',command=newwind)
menuFile.add_separator()
menuFile.add_command(label='退出',command=root.destroy)

root.config(menu=mainmenu)
root.mainloop()
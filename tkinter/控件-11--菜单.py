#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-10-13 19:01:07
# Author : zijing (zijing412@163.com)
###################################################
# 菜单：(Menu)用于可视化地为一系列的命令分组，从而方便用户找到和触发执行这些命令。
# 这里Menu所实例化别的主要是菜单，其通式为
# 菜单实例名=Menu(根窗体)
# 菜单分组1=Menu(菜单实例名)
# 菜单实例名.add_cascade(<label=菜单分组1 显示文本>,<menu=菜单分组1>)
# 菜单分组1.add_command(<label=命令1文本>,<command=命令1函数名>)

# 其中较为常见的方法有：add_cascade()、add_command()和add_separator()，分别用于添加一个菜单分组、添加一条菜单命令和添加一条分割线。
# 利用Menu控件也可以创建快捷菜单（又称为上下文菜单）。
# 通常需要右击弹出的控件实例绑定鼠标右击响应事件<Button-3>,
# 并指向一个捕获event参数的自定义函数，
# 在该自定义函数中，将鼠标的触发位置event.x_root 和 event.y_root以post()方法传给菜单。


from tkinter import *

def new():
     s = '新建'
     lb1.config(text=s)

def ope():
     s = '打开'
     lb1.config(text=s)

def sav():
     s = '保存'
     lb1.config(text=s)

def cut():
     s = '剪切'
     lb1.config(text=s)

def cop():
     s = '复制'
     lb1.config(text=s)

def pas():
     s = '粘贴'
     lb1.config(text=s)

def popupmenu(event):
     mainmenu.post(event.x_root,event.y_root)

root = Tk()
root.title('菜单实验')
root.geometry('320x240')

lb1 = Label(root,text='显示信息',font=('黑体',32,'bold'))
lb1.place(relx=0.2,rely=0.2)

mainmenu = Menu(root)
menuFile = Menu(mainmenu)  # 菜单分组 menuFile
mainmenu.add_cascade(label="文件",menu=menuFile)
menuFile.add_command(label="新建",command=new)
menuFile.add_command(label="打开",command=ope)
menuFile.add_command(label="保存",command=sav)
menuFile.add_separator()  # 分割线
menuFile.add_command(label="退出",command=root.destroy)

menuEdit = Menu(mainmenu)  # 菜单分组 menuEdit
mainmenu.add_cascade(label="编辑",menu=menuEdit)
menuEdit.add_command(label="剪切",command=cut)
menuEdit.add_command(label="复制",command=cop())
menuEdit.add_command(label="粘贴",command=pas())

root.config(menu=mainmenu)
root.bind('Button-3',popupmenu) # 根窗体绑定鼠标右击响应事件
root.mainloop()
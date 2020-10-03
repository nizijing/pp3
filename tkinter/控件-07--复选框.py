#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-10-03 17:10:53
# Author : zijing (zijing412@163.com)
###################################################

# 复选框：(Checkbutton) 是为了返回多个选项值的交互控件，通常不直接触发函数的执行。
# 该控件除具有共有属性外，还具有显示文本（text）、返回变量（variable）、选中返回值（onvalue）和未选中默认返回值（offvalue）等重要属性。
# 返回变量variable=var 通常可以预先逐项分别声明变量的类型var=IntVar() (默认)或 var=StringVar(), 
# 在所调用的函数中方可分别调用 var.get()方法 取得被选中实例的 onvalue或offvalue值。
# 复选框实例通常还可分别利用 select()、deselect()和 toggle() 方法对其进行选中、清除选中和反选操作。


from tkinter import *
import tkinter

def run():
     if(CheckVar1.get()==0 and CheckVar2.get()==0 and CheckVar3.get()==0 and CheckVar4.get()==0):
         s = '您还没选择任何爱好项目'
     else:
         s1 = "足球" if CheckVar1.get()==1 else ""
         s2 = "篮球" if CheckVar2.get() == 1 else ""
         s3 = "游泳" if CheckVar3.get() == 1 else ""
         s4 = "田径" if CheckVar4.get() == 1 else ""
         s = "您选择了%s %s %s %s" % (s1,s2,s3,s4)
     lb2.config(text=s)

root = tkinter.Tk()
root.title('复选框')
lb1=Label(root,text='请选择您的爱好项目')
lb1.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()

ch1 = Checkbutton(root,text='足球',variable = CheckVar1,onvalue=1,offvalue=0)
ch2 = Checkbutton(root,text='篮球',variable = CheckVar2,onvalue=1,offvalue=0)
ch3 = Checkbutton(root,text='游泳',variable = CheckVar3,onvalue=1,offvalue=0)
ch4 = Checkbutton(root,text='田径',variable = CheckVar4,onvalue=1,offvalue=0)

ch1.pack()
ch2.pack()
ch3.pack()
ch4.pack()

btn = Button(root,text="OK",command=run)
btn.pack()

lb2 = Label(root,text='')
lb2.pack()
root.mainloop()
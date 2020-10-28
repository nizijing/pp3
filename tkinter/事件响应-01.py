#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-10-27 19:39:09
# Author : zijing (zijing412@163.com)
###################################################
# 用tkinter 可将用户事件与自定义函数绑定，用键盘或鼠标的动作事件来响应触发自定义函数的执行。其通式为：
# 控件实例.bind(<事件代码>,<函数名>)
# 其中，事件代码通常以半角小于号“<”和大于号“>” 界定，包括事件和按键等 2~3个部分，它们之间用减号分隔，常见事件代码见下表：
# 事件	事件代码	备注
# 单击鼠标左键	<ButtonPress-1>	可简写为<Button-1> 或 <1>
# 单击鼠标中键	<ButtonPress-2>	可简写为<Button-2> 或 <2>
# 单击鼠标右键	<ButtonPress-3>	可简写为<Button-3> 或 <3>
# 释放鼠标左键	<ButtonRelease-1>	---
# 释放鼠标中键	<ButtonRelease-2>	---
# 释放鼠标右键	<ButtonRelease-3>	---
# 按住鼠标左键移动	<B1-Motion>	---
# 按住鼠标中键移动	<B2-Motion>	---
# 按住鼠标右键移动	<B3-Motion>	---
# 转动鼠标滚轮	<MouseWheel>	---
# 双击鼠标左键	<Double-Button-1>	---
# 鼠标进入控件实例	<Enter>	注意与回车事件的区别
# 鼠标离开控件实例	<Leave>	---
# 键盘任意键	<Key>	---
# 字母和数字	< Key-字母>,例如<key-a>、<Key-A>	简写不带小于和大于号,例如:a,A和1等
# 回车	<Return>	<Tab>,<Shift>,<Control>(注意不能用<Ctrl>),<Alt>等类同
# 空格	<Space>	---
# 方向键	<Up> ,<Down>,<Left>,<Right>	---
# 功能键	<Fn>例如:<F1>等	---
# 组合键	键名之间以减号链接,例如<Control-k>,<Shift-6>,<Alt-Up>等	注意大小写

# 例如,将框架控件实例frame 绑定鼠标右键单击事件,调用自定义函数 myfunc()可表示为"frame.bind('<Button-3>',myfunc)",
# 注意: myfunc后面没有括号。
# 将控件实例绑定到键盘事件和部分光标不落在具体控件实例上的鼠标事件时，还需要设置该实例执行focus_set() 方法获得焦点，才能对事件持续响应。
# 例如： frame.focus_set()。所调用的自定义函数若需要利用鼠标或键盘的响应值，可将event作为参数，通过event的属性获取。
# event的属性见下表：

# event属性	意义
# x或y（注意是小写）	相对于事件绑定控件实例左上角的坐标值(像素)
# root_x或root_y（注意是小写）	相对于显示屏幕左上角的坐标值(像素)
# char	可显示的字符，若按键不可显示，则返回为空字符串
# keysysm	字符或字符型按键名，如：“a”或“Escape”
# keysysm_num	按键的十进制 ASCII 码值

from tkinter import *

def show(event):
    s=event.keysym
    lb.config(text=s)

root=Tk()
root.title('按键实验')
root.geometry('200x200')
lb=Label(root,text='请按键',font=('黑体',48))
lb.bind('<Key>',show)
lb.focus_set()
lb.pack()
root.mainloop()

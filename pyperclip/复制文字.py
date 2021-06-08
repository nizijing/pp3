#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-04 14:07:28
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
import pyperclip3
import pyperclip

def pclip3():
    pyperclip3.copy("hello clipboard3") # copy data to the clipboard
    cb_data = pyperclip3.paste() # retrieve clipboard contents 
    print(cb_data)

    pyperclip3.clear() # clears the clipboard contents
    assert not pyperclip3.paste()

def pclip():
    pyperclip.copy("hello clipboard") # copy data to the clipboard
    cb_data = pyperclip.paste() # retrieve clipboard contents 
    print(cb_data)

pclip()
pclip3()
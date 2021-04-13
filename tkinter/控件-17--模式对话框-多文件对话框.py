#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2021-04-13 15:04:55
# Author : zijing (zijing412@163.com)
###################################################

from tkinter import Tk ,filedialog
root=Tk()
root.withdraw()
cur=filedialog.askopenfilenames(filetypes=[('excel files', ('.xlsx', '.xls')), ('text files', '.txt'),('pythonfiles',('.py','.pyw'))])
if cur:
    print(cur)
else:
    print('你没有选择任何文件')
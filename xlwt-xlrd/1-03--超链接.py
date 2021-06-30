#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-09 11:48:36
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
import xlwt

workbook = xlwt.Workbook(encoding = 'utf-8')    # 实例化一个工作簿对象
worksheet = workbook.add_sheet('work_sheet')    # 获取工作表对象Worksheet
xstyle = xlwt.XFStyle()     # 实例化表格样式对象

# 设置行高
worksheet.row(0).height_mismatch = True
worksheet.row(0).height = 20 * 30  # 20是基数*30是行的高度
a_data = 'HYPERLINK("http://www.baidu.com";"baidu")'   # 要插入的网址，'baidu'是在Excel中显示的值。
worksheet.col(0).width = 256 * len(a_data) * 2 # 设置单元格宽度
worksheet.write(0,0, label = xlwt.Formula(a_data),style=xstyle)  # 插入超链接

# 保存数据到硬盘
workbook.save(r'result.xls')
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-09 11:02:28
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
# 这章节的主要内容可以参考xlwt包中ExcelFormula.py
import xlwt

workbook = xlwt.Workbook(encoding = 'utf-8')    # 实例化一个工作簿对象
worksheet = workbook.add_sheet('work_sheet')    # 获取工作表对象Worksheet
xstyle = xlwt.XFStyle()     # 实例化表格样式对象

for i in range(3):
    # 设置行高
    worksheet.row(i).height_mismatch = True
    worksheet.row(i).height = 20 * 30  # 20是基数*30是行的高度
    for j in range(3):
        # 向工作表中添加数据（参数对应 行, 列, 值，样式）
        worksheet.write(i,j, label = int(j)+1,style=xstyle)
# 设置行高
worksheet.row(3).height_mismatch = True
worksheet.row(3).height = 20 * 30  # 20是基数*30是行的高度
worksheet.write(3,0, label = xlwt.Formula('SUM(A1:A3)'),style=xstyle)  # 求和函数
worksheet.write(3,1, label = xlwt.Formula('B1*B2*B3'),style=xstyle)    # 求乘积
worksheet.write(3,2, label = xlwt.Formula('AVERAGE(C1:C3)'),style=xstyle)  # 求平均数

# 保存数据到硬盘
workbook.save(r'result.xls')
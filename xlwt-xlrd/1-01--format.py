#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-08 17:50:20
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
# 这章节的主要内容可以参考xlwt包中Formatting.py
import xlwt

def setFont():
    # 字体
    xfont = xlwt.Font()         
    xfont.height = 0x00C8       # 0x00C8 = 20 * 10  设置字体高度（20是基数不变，10是字号用于调整大小）
    xfont.italic = False        # 倾斜
    xfont.struck_out = False    # 剔除
    xfont.outline = False       # 
    xfont.shadow = False        # 阴影
    xfont.colour_index = 0x7FFF # 设置字体颜色
    xfont.bold = False          # 加粗
    xfont._weight = 0x0190      # 0x02BC gives bold font
    xfont.escapement = xfont.ESCAPEMENT_NONE
    xfont.underline = xfont.UNDERLINE_SINGLE_ACC    # 下划线
    xfont.family = xfont.FAMILY_NONE
    xfont.charset = xfont.CHARSET_SYS_DEFAULT
    xfont.name = 'Arial'        # 设置字体

    return xfont

def setAlignment():
    # 字体位置
    xalig = xlwt.Alignment()

    xalig.horz = xalig.HORZ_CENTER  # 字体水平居中
    xalig.vert = xalig.VERT_CENTER  # 字体垂直居中
    xalig.dire = xalig.DIRECTION_GENERAL        # 方向
    xalig.orie = xalig.ORIENTATION_NOT_ROTATED  # 旋转
    xalig.rota = xalig.ROTATION_0_ANGLE         # 旋转角度
    xalig.wrap = xalig.NOT_WRAP_AT_RIGHT
    xalig.shri = xalig.NOT_SHRINK_TO_FIT        # 自适应
    xalig.inde = 0
    xalig.merg = 0

    return xalig

def setBorders():
    # 边框
    xborder = xlwt.Borders()

    xborder.left   = xborder.NO_LINE
    xborder.right  = xborder.NO_LINE
    xborder.top    = xborder.NO_LINE
    xborder.bottom = xborder.NO_LINE
    xborder.diag   = xborder.NO_LINE

    xborder.left_colour   = 0x40
    xborder.right_colour  = 0x40
    xborder.top_colour    = 0x40
    xborder.bottom_colour = 0x40
    xborder.diag_colour   = 0x40

    xborder.need_diag1 = xborder.NO_NEED_DIAG1
    xborder.need_diag2 = xborder.NO_NEED_DIAG2

    return xborder

def setPattern():
    # 底纹
    xpattern = xlwt.Pattern()

    xpattern.pattern = xpattern.NO_PATTERN  # 是否有底纹
    xpattern.pattern_fore_colour = 0x40
    xpattern.pattern_back_colour = 0x41

    return xpattern


workbook = xlwt.Workbook(encoding = 'utf-8')    # 实例化一个工作簿对象
worksheet = workbook.add_sheet('work_sheet')    # 获取工作表对象Worksheet
xstyle = xlwt.XFStyle()     # 实例化表格样式对象

# 设置样式
xstyle.font = setFont()             # 设置字体样式
xstyle.alignment = setAlignment()   # 设置字体在单元格中的位置
xstyle.borders = setBorders()       # 设置边框
xstyle.pattern = setPattern()       # 设置底纹

for i in range(3):
    for j in range(3):
        # 向工作表中添加数据（参数对应 行, 列, 值，样式）
        worksheet.write(i,j, label = 'test_'+str(j),style=xstyle)

# 保存数据到硬盘
workbook.save(r'result.xls')

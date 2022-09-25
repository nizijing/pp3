#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2022-07-25 17:19:04
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################

FPS = 30

CELLSIZE = 35
MARGINLEFT = MARGINRIGHT = MARGINUP = MARGINDOWN = int(CELLSIZE / 2)  # 雷区上下左右的宽度

THISISMINE  = 9    # 表示该地区为地雷

FALGUNSWAAPED = 10 # 表示该地区没有被挖过
FLAGDANGER = 11    # 表示该地区插了一面旗子
FLAGUNKNOW = 12    # 表示该地区未知

FLAGSWAPPWD = 13   # 表示该地区已经被挖过
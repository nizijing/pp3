#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-30 13:44:40
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################

x = {'a' : 1}
y = {'x' : 4}
z = {**x, **y, 'h': 5}

print(z)
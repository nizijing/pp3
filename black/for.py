#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-30 13:49:41
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################


def demo():
    for i in range(4):
        print(i)
        if i > 2:
            return
    else:
        print('for end')

demo()
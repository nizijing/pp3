#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-30 14:17:55
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################

def oneStar(*parm):
    print(parm)

def twoStar(**parm):
    print(parm)

listDemo = [1, 2, 3]
dictDemo = {'a': 1, 'b': 2}

oneStar(listDemo)
oneStar(dictDemo)
oneStar(1,2)
twoStar(a=1, b=2)

def fix_demo(name, age, gender='男', *args, **kwds):
    print('姓名：%s，年龄：%d，性别：%s'%(name, age, gender))
    print(args)
    print(kwds)

fix_demo('xufive', 50, '男', 175, 75, math=99, english=90)


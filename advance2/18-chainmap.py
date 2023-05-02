#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   18-chainmap.py
@Time    :   2023/04/22 15:24:10
@Author  :   zijing
@Version :   1.0
@Site    :   https://none
@Desc    :   None
'''


# 这个教程的说明很好
# https://www.bilibili.com/video/BV1yY4y1G7hb/?spm_id_from=pageDriver&vd_source=bd80b80e13fabcec3b17eb9c1f62604f



from collections import ChainMap
m1 = {'a':1, 'b':2, 'c':3, 'd':4}
m2 = {'c':30, 'd':4, 'e':5, 'f':6}

cmap = ChainMap(m1, m2)
print(cmap, cmap['c'])

cmap['c'] = 4
print(cmap)

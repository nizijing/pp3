#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-11-26 22:33:57
# Author : zijing (zijing412@163.com)
###################################################
"""
Topic: 多值映射
Desc : 
"""

from collections import defaultdict


def multi_dict():
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)
    print(f"list: {d}")

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)
    print(f"set: {d}")

    d = {} # A regular dictionary
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)
    print(f"dict: {d}")

# 以上等效于
d = {}
if 'a' not in d:
    d['a'] = []

d['a'].append(1)
print(d)
multi_dict()

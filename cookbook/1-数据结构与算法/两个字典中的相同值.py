#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-11-26 22:46:33
# Author : zijing (zijing412@163.com)
###################################################
"""
Topic: 字典的集合操作
Desc : 
"""


def dict_commonality():
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    # Find keys in common
    print(a.keys() & b.keys())  # { 'x', 'y' }
    # Find keys in a that are not in b
    print(a.keys() - b.keys())  # { 'z' }
    # Find (key,value) pairs in common
    print(a.items() & b.items())  # { ('y', 2) }

    print(type(a.items()))

    for a, b in a.items():
        print(a, b)


if __name__ == '__main__':
    dict_commonality()
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-30 16:30:03
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
def wrapper(func):
    def inner_function():
        pass
    return inner_function

@wrapper
def with_wrapped():
    pass

def without_wrapped():
    pass

print(with_wrapped.__name__)
print(without_wrapped.__name__)

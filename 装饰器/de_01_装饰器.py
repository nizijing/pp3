#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-30 15:54:01
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
from time import time, sleep

def timer(func):
    def wrapper(*args,**kwds):
        t0 = time()
        ret = func(*args,**kwds)
        t1 = time()
        print('耗时%0.3f'%(t1-t0,))
        return ret
    return wrapper


@timer
def demo():
    sleep(1)
    return 12

print(demo())
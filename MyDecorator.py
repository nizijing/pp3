#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/9 11:11 
# @Author : zijing 
# @Site :  
# @File : MyDecorator.py 
# @Software: PyCharm

from time import time
from datetime import datetime


def show_run_time(func):
    def inner(*args, **kwargs):
        local_time = time()
        print(datetime.fromtimestamp(local_time), func.__name__, end=' ')
        result = func(*args, **kwargs)
        print('run {:.2f}s'.format(time() - local_time))
        return result
    return inner


def myDebug(func):
    def inner(*args, **kwargs):
        local_time = time()
        print(datetime.fromtimestamp(local_time), func.__name__)
        return func(*args, **kwargs)
    return inner

if __name__ == '__main__':
    pass
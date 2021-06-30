#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-30 16:15:16
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################

def say_hello(contry):
    def wrapper(func):
        def deco(*args, **kwargs):
            if contry == "china":
                print("你好! ", end = '')
            elif contry == "america":
                print('hello. ', end = '')
            else:
                return
            return func(*args, **kwargs)
        return deco
    return wrapper


@say_hello("china")
def xiaoming():
    return '小明'

# jack，美国人
@say_hello("america")
def jack():
    return 'jack'

print(xiaoming())
print(jack())
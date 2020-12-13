#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-12-13 19:46:07
# Author : zijing (zijing412@163.com)
###################################################
"""
Topic: 打印不合法文件名
Desc : 
"""
import os
import sys


def bad_filename(filename):
        return repr(filename)[1:-1]


def bad_filename2(filename):
    """完美方案"""
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')


def print_badfile(filename):
    try:
        print(filename)
    except UnicodeEncodeError:
        print('UnicodeEncodeError')
        print(bad_filename(filename))

    #files = os.listdir('.')
    #print(files)


if __name__ == '__main__':
    print_badfile('bäd.txt')
    print(bad_filename2('bäd.txt'))


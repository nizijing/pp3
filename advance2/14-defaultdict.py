#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   14-defaultdict.py
@Time    :   2023/04/22 14:53:51
@Author  :   zijing
@Version :   1.0
@Site    :   https://none
@Desc    :   None
'''

from collections import defaultdict 


def test():
    '''比较常见的一个用法'''
    d = defaultdict(list)
    d['first'].append('hello')
    d['first'].append('world')
    d['second'].append('hello')
    print(d)
    

def test1():
    '''统计一个字符串中各个字母出现的次数'''
    src = 'Thkfjskldfjsifasldfahijijkl'
    d = defaultdict(int)
    for c in src:
        d[c] += 1
    print(d)


def constant_factory(value):
    return lambda: value


def test2():
    '''以函数入参为默认值的字典'''
    d = defaultdict(constant_factory('<missing>'))
    d.update(name = 'Mike', action = 'ran')
    print('%(name)s %(action)s to %(unknow)s' % d)


test()
test1()
test2()
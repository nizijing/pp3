#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   30-nametuple.py
@Time    :   2023/04/22 16:39:17
@Author  :   zijing
@Version :   1.0
@Site    :   https://none
@Desc    :   https://www.bilibili.com/video/BV11U4y1X79t/?spm_id_from=333.788&vd_source=bd80b80e13fabcec3b17eb9c1f62604f
             mysql也可以使用这个方法优化
'''



from collections import namedtuple
import csv

def test1():
    Person = namedtuple('Person', ['name', 'age'])

    p1 = Person('zhangsan', 18)

    print(p1, p1.name, p1.age)


def test2():
    Person = namedtuple('Person',  ['name', 'age'])
    for person in map(Person._make,
        csv.reader(open('test.csv','r'))):
        print(person, person.name, person.age)


test1()
test2()

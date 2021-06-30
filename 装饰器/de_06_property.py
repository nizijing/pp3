#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-30 17:02:12
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
# 用@property装饰过的函数，会将一个函数定义成一个属性，属性的值就是该函数return的内容。
# 同时，会将这个函数变成另外一个装饰器。
# 就像后面我们使用的@age.setter和@age.deleter。
# @age.setter 使得我们可以使用XiaoMing.age = 25这样的方式直接赋值。
# @age.deleter 使得我们可以使用del XiaoMing.age这样的方式来删除属性。


class Student(object):
    def __init__(self, name):
        self.name = name
        self.name = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('输入不合法：年龄必须为数值!')
        if not 0 < value < 100:
            raise ValueError('输入不合法：年龄范围必须0-100')
        self._age=value

    @age.deleter
    def age(self):
        del self._age

xiaoming = Student("小明")

# 设置属性
xiaoming.age = 25

# 查询属性
xiaoming.age

# 删除属性
del xiaoming.age
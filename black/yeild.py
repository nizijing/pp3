#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-30 15:38:34
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################

# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器


listDemo = range(10)
list2 = range(3)
demo_iter = iter(listDemo)

for i in demo_iter:
    if i == 5:
        next(demo_iter) # 跳过6
    print(i)
else:
    print('第一次遍历完成，demo_iter内容为空')

for i in demo_iter:
    print(i)
else:
    print('没有用生成器生成迭代对象，第2次遍历不会有输出')
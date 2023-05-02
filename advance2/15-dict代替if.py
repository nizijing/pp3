#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   15-defaultdict.py
@Time    :   2023/04/22 15:10:36
@Author  :   zijing
@Version :   1.0
@Site    :   https://none
@Desc    :   None
'''

def calculate(var1, var2, operator):
    if operator == '+':
        return var1 + var2
    elif operator == '-':
        return var1 - var2
    elif operator == '*':
        return var1 * var2
    elif operator == '/':
        return var1 / var2
    else:
        return None

print(calculate(10,20,'+'))


# 用另一种方法实现
import operator as op
def calculate2(var1, var2, operator):
    operator_dict = {   '+': op.add,
                        '-': op.sub,
                        '*': op.mul,
                        '/': op.truediv}
    return operator_dict[operator](var1, var2)
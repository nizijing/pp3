#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-11-13 20:37:14
# Author : zijing (zijing412@163.com)
###################################################
# pandas.Series( data, index, dtype, copy)
# data  数据采取各种形式，如：ndarray，list，constants
# index 索引值必须是唯一的和散列的，与数据的长度相同。 默认np.arange(n)如果没有索引被传递。
# dtype dtype用于数据类型。如果没有，将推断数据类型
# copy  复制数据，默认为false。

import numpy as np
import pandas as pd
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)

s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[['a','c','d']])

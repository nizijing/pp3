#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   20-字典合并.py
@Time    :   2023/04/22 15:45:24
@Author  :   zijing
@Version :   1.0
@Site    :   https://none
@Desc    :   None
'''

dict1 = {'a': 1, 'b':2}
dict2 = {'a': 2, 'c':3}
dict3 = {'a': 3, 'd':4}

merged_dict = {
    **dict1,
    **dict2,
    **dict3
}

print(merged_dict)
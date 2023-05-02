#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   19-read_only_dict.py
@Time    :   2023/04/22 15:33:13
@Author  :   zijing
@Version :   1.0
@Site    :   https://none
@Desc    :   None
'''

from types import MappingProxyType

read_write_dict = {'name': 'mike', 'age':12}
read_only_dict = MappingProxyType(read_write_dict)
del read_write_dict

print(read_only_dict['name'])

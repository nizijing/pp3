#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   21-优雅地打印字典.py
@Time    :   2023/04/22 15:48:11
@Author  :   zijing
@Version :   1.0
@Site    :   https://none
@Desc    :   None
'''

from pprint import pprint
import json

dict1 = {'name': '小李', 'age': 20, 'high': 170, 'weight': 120, 
            'father': {'name': 'Mike', 'age': 44, 'high': 170, 'weight': 230}}
pprint(dict1, indent=4, sort_dicts=False)
print(json.dumps(dict1, indent=4, sort_keys=False, ensure_ascii=False))
print("%(name)s %(age)i %(high)i %(father)s" % dict1)

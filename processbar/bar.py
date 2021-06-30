#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-30 10:50:27
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
from time import sleep
mylist = range(10)


print('tqdm demo')
from tqdm import tqdm
for i in tqdm(mylist): 
    sleep(0.1)


print('alive_progress demo')
from alive_progress import alive_bar
with alive_bar(len(mylist)) as bar: 
    for i in mylist: 
        if i %2 == 1:
            bar() 
            sleep(1)


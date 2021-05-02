#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-05-02 15:20:33
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
from pynput import mouse

# The event listener will be running in this block
with mouse.Events() as events:
    for event in events:
        if event.button == mouse.Button.right:
            break
        else:
            print('Received event {}'.format(event))

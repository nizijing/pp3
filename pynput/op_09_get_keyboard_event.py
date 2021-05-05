#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-05-05 15:16:35
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
from pynput import keyboard

# The event listener will be running in this block
with keyboard.Events() as events:
    # Block at most one second
    event = events.get(1.0)
    if event is None:
        print('You did not press a key within one second')
    else:
        print('Received event {}'.format(event))
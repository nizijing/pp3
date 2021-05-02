#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-05-02 14:52:27
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
from pynput.mouse import Button, Controller

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(mouse.position))

# Set pointer position
mouse.position = (589, 387)
# print('Now we have moved it to {0}'.format(mouse.position))

# Move pointer relative to current position
# mouse.move(5, -5)

# Press and release
mouse.press(Button.left)
mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on macOS
# mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)
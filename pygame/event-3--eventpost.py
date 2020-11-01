#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-11-01 09:42:25
# Author : zijing (zijing412@163.com)
###################################################
# 为了产生事件，必须先造一个出来，然后再传递它：

import pygame
from pygame.locals import *

pygame.init()
my_event = pygame.event.Event(KEYDOWN, key=K_SPACE, mod=0, unicode=u' ')
pygame.event.post(my_event)
#你也可以像下面这样写，看起来比较清晰（但字变多了……）
my_event = pygame.event.Event(KEYDOWN, {"key":K_SPACE, "mod":0, "unicode":u' '})
pygame.event.post(my_event)

CATONKEYBOARD = USEREVENT+1
my_event = pygame.event.Event(CATONKEYBOARD, message="Bad cat!")
pygame.event.post(my_event)
 
#然后获得它
for event in pygame.event.get():
    if event.type == CATONKEYBOARD:
        print(event.message)
    if event.type == KEYDOWN:
        print(event)
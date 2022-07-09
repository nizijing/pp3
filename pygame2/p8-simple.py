#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2022-07-02 19:23:06
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello world")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exti()
    pygame.display.update()

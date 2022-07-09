#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2022-07-09 15:40:05
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
from turtle import right
import pygame, sys
from pygame.locals import *

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255,255,255)
catImg = pygame.image.load('sources/cat.png')
catx = 10
caty = 10
direction = 'right'
while True:
    # DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 230:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 0:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 0:
            direction = 'right'
    

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)

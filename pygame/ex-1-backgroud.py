#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-10-29 19:27:44
# Author : zijing (zijing412@163.com)
###################################################
# Pygame有很多的模块，下面是一张一览表：

# 模块名	功能
# pygame.cdrom	访问光驱
# pygame.cursors	加载光标
# pygame.display	访问显示设备
# pygame.draw	绘制形状、线和点
# pygame.event	管理事件
# pygame.font	使用字体
# pygame.image	加载和存储图片
# pygame.joystick	使用游戏手柄或者 类似的东西
# pygame.key	读取键盘按键
# pygame.mixer	声音
# pygame.mouse	鼠标
# pygame.movie	播放视频
# pygame.music	播放音频
# pygame.overlay	访问高级视频叠加
# pygame	就是我们在学的这个东西了……
# pygame.rect	管理矩形区域
# pygame.sndarray	操作声音数据
# pygame.sprite	操作移动图像
# pygame.surface	管理图像和屏幕
# pygame.surfarray	管理点阵图像数据
# pygame.time	管理时间和帧信息
# pygame.transform	缩放和移动图像

#!/usr/bin/env python

background_image_filename = 'pygame\\sources\\pic\\OIP.jpg'
mouse_image_filename = 'pygame\\sources\\pic\\pt.png'
#指定图像文件名称

import pygame
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
from sys import exit
#向sys模块借一个exit函数用来退出程序

pygame.init()
#初始化pygame,为使用硬件做准备

screen = pygame.display.set_mode((474, 307), 0, 32)
#创建了一个窗口
pygame.display.set_caption("Hello, World!")
#设置窗口标题

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#加载并转换图像

while True:
#游戏主循环

    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()

    screen.blit(background, (0,0))
    #将背景图画上去

    x, y = pygame.mouse.get_pos()
    #获得鼠标位置
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    #计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    #把光标画上去

    pygame.display.update()
    #刷新一下画面
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2022-07-25 17:18:44
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
import pygame, sys, itertools, random, numpy as np
from pygame.locals import *
from setting import *


class cMineSwapRender():
    def __init__(self):
        pygame.display.set_caption('Mine Sweep')
        self.load_img()
        self.init_game()


    def load_img(self):
        self.img0 = pygame.image.load('res/0.png')
        self.img1 = pygame.image.load('res/1.png')
        self.img2 = pygame.image.load('res/2.png')
        self.img3 = pygame.image.load('res/3.png')
        self.img4 = pygame.image.load('res/4.png')
        self.img5 = pygame.image.load('res/5.png')
        self.img6 = pygame.image.load('res/6.png')
        self.img7 = pygame.image.load('res/7.png')
        self.img8 = pygame.image.load('res/8.png')
        self.img9 = pygame.image.load('res/9.png')
        self.img10 = pygame.image.load('res/10.png')
        self.img11 = pygame.image.load('res/11.png')
        self.img12 = pygame.image.load('res/12.png')
        self.imgAgain = pygame.image.load('res/Again.png')
        self.imgCLOCK_ITEM = pygame.image.load('res/CLOCK_ITEM.png')
        self.imgClock = pygame.image.load('res/Clock.png')
        self.imgMineCount = pygame.image.load('res/MineCount.png')
        self.ico = pygame.image.load('res/MineSweep.ico')

    
    def init_game(self):
        self.mine_area_width = 10
        self.mine_area_height = 10
        self.mine_num = self.mine_flag = 10
        self.suround_idx = [[-1, -1], [0, -1], [1, -1],
                            [-1,  0],          [1,  0],
                            [-1,  1], [0,  1], [1,  1]
        ]
        assert self.mine_num < self.mine_area_width * self.mine_area_height, '雷的数量比雷区总数大'
        self.window_width = MARGINLEFT + self.mine_area_width * CELLSIZE + MARGINRIGHT
        self.window_height = MARGINUP + self.mine_area_height * CELLSIZE + MARGINDOWN
        self.displaysurf = pygame.display.set_mode((self.window_width, self.window_height), 0, 32)
        self.cell_value  = np.zeros((self.mine_area_width, self.mine_area_height))
        self.cell_status = np.ones((self.mine_area_width, self.mine_area_height)) * 10
        self.cell_status_image = {
            0: self.img0, 1: self.img1, 2: self.img2, 3: self.img3, 4: self.img4, 
            5: self.img5, 6: self.img6, 7: self.img7, 8: self.img8, 9: self.img9,
            FALGUNSWAAPED: self.img10, FLAGDANGER: self.img11, FLAGUNKNOW: self.img12
            }
        

        for i in random.sample(range(0, (self.mine_area_width - 1) * (self.mine_area_height - 1)), self.mine_num):  # 生成 self.mine_num 个不同的随即数
            self.cell_value[int(i / 9)][i % 9] = THISISMINE

        for i, j in itertools.product(range(self.mine_area_width), range(self.mine_area_height)):
            if self.cell_value[i][j] == THISISMINE:
                self.calc_suround_num(i, j)
            self.draw_cell(i, j, self.img10)

        print(self.cell_value)


    def calc_suround_num(self, arrx, arry):
        # please rewrite it in child
        return


    def main(self):
        fpsClock = pygame.time.Clock()
        self.draw_all_mine()

        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if event.button == 1: # 鼠标左键
                        self.draw_mine_area_logic(mousex, mousey)
                    elif event.button == 3: # 鼠标右键
                        self.draw_flag_logic(mousex, mousey)
                elif event.type == QUIT:
                    pygame.init()
                    sys.exit()
            pygame.display.update()
            fpsClock.tick(FPS)


    def axis_to_arr(self, x, y):
        return int((x - MARGINLEFT) / CELLSIZE), int((y - MARGINUP) / CELLSIZE)


    def draw_mine_area_logic(self, x, y):
        arrx, arry = self.axis_to_arr(x, y)
        print(arrx, arry)


    def draw_flag_logic(self, x, y):
        arrx, arry = self.axis_to_arr(x, y)
        self.draw_cell(arrx, arry, self.img11)


    def draw_cell(self, arrx, arry, flag):
        self.displaysurf.blit(flag, (MARGINLEFT + arrx * CELLSIZE, MARGINUP + arry * CELLSIZE))


    def draw_all_mine(self):
        for i, j in itertools.product(range(self.mine_area_width), range(self.mine_area_height)):
            if self.cell_value[i][j] == THISISMINE:
                self.draw_cell(i, j, self.img9)



if __name__ == "__main__":
    mine_game = cMineSwapRender()
    mine_game.main()

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2022-07-10 17:15:34
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################

import pygame, sys, itertools
from pygame.locals import *
from setting import *
from minesweep_rander import cMineSwapRender


class cMineSwapLocig(cMineSwapRender):
    def draw_all(self):
        # draw_all, this is only use for test
        for arrx, arry in itertools.product(range(self.mine_area_width), range(self.mine_area_height)):
            self.draw_cell(arrx, arry, self.cell_status_image[self.cell_status[arrx][arry]])

    def draw_mine_area_logic(self, x, y):
        arrx, arry = self.axis_to_arr(x, y)
        if self.cell_status[arrx][arry] in (FLAGSWAPPWD, FLAGDANGER, FLAGUNKNOW):
            return
        elif self.cell_value[arrx][arry] == THISISMINE:
            self.game_over_logic()
        self.draw_after_sweep(arrx, arry)

    def you_win(self):
        print('you win!')


    def draw_after_sweep(self, arrx, arry):
        if self.cell_status[arrx][arry] in (FLAGDANGER, FLAGUNKNOW, FLAGSWAPPWD):
            return
        if self.cell_value[arrx][arry] == 0:
            self.draw_cell(arrx, arry, self.cell_status_image[self.cell_value[arrx][arry]])
            self.cell_status[arrx][arry] = FLAGSWAPPWD
            for (i, j) in self.suround_idx:
                if i + arry in (-1, self.mine_area_height) or j + arrx in (-1, self.mine_area_width):
                    continue
                self.draw_after_sweep(arrx + j, arry + i)
            return

        elif 0 < self.cell_value[arrx][arry] < self.mine_num - 1:
            self.draw_cell(arrx, arry, self.cell_status_image[self.cell_value[arrx][arry]])
        self.cell_status[arrx][arry] = FLAGSWAPPWD
        return


    def calc_suround_num(self, arrx, arry):
        for (i, j) in self.suround_idx:
            if i + arry in (-1, self.mine_area_height) or j + arrx in (-1, self.mine_area_width):
                continue
            if self.cell_value[arrx + j][arry + i] == THISISMINE:
                continue
            self.cell_value[arrx + j][arry + i] += 1


    def game_over_logic(self):
        self.draw_all_mine()


    def draw_flag_logic(self, x, y):
        arrx, arry = self.axis_to_arr(x, y)
        if self.cell_status[arrx][arry] == FLAGSWAPPWD:
            return
        if self.cell_status[arrx][arry] == FLAGDANGER and self.cell_value[arrx][arry] == THISISMINE:
            self.mine_flag += 1
        self.cell_status[arrx][arry] = (self.cell_status[arrx][arry] - FALGUNSWAAPED + 1) % 3 + FALGUNSWAAPED
        self.draw_cell(arrx, arry, self.cell_status_image[self.cell_status[arrx][arry]])
        if self.cell_status[arrx][arry] == FLAGDANGER and self.cell_value[arrx][arry] == THISISMINE:
            self.mine_flag -= 1
            if self.mine_flag == 0:
                self.you_win()
        print(self.mine_flag)


    def main(self):
        fpsClock = pygame.time.Clock()
        # self.draw_all()
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


if __name__ == "__main__":
    mine_game = cMineSwapLocig()
    mine_game.main()
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-30 11:23:49
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
import imageio


def main():
    image_list = ['gif/src1.png', 'gif/src2.png']
    gif_name = 'gif/output.gif'
    duration = 0.35
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration = duration)


if __name__ == '__main__':
    main()
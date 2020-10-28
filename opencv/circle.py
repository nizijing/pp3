#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-10-28 19:47:42
# Author : zijing (zijing412@163.com)
###################################################
import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
white = (255, 255, 255)

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
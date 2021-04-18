#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-04-18 16:05:06
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
import os
from time import sleep

# adb常用的一些命令
# 截图  adb shell screencap -p /sdcard/screen.png
# 下载  adb pull /sdcard/screen.png
# 上传  adb push 文件名 手机端SDCard路径
# 录屏  adb shell screenrecord /sdcard/demo.mp4

# adb 模拟点击、滑动、输入、按键
# 输入  adb shell input text "001"
# home按键  adb shell input keyevent 3
# 点击(540, 1104)坐标
#       adb shell input tap 540 1104
# 滑动，从(250,250)滑动到(300,300)
#       adb shell input swipe 250 250 300 300
# 长按100 100 位置长按 1000毫秒
#       adb shell input swipe 100 100 100 100 1000 


def get_screen_image():
    #os.system('adb shell screencap -p /sdcard/screen.png') 
    #os.system('adb pull /sdcard/screen.png')
    # 把图片拉下来后可以知道图片的像素是1080 x 2340
    # 从图片的大小计算出相机的位置
    os.system('adb shell input keyevent 3') 
    os.system('adb shell input tap 950 2100')   # 点击相机
    sleep(0.5)
    os.system('adb shell input tap 540 2000')   # 点击拍摄
    sleep(1)
    os.system('adb shell input keyevent 3')

def main():
    get_screen_image()

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-11-20 19:27:41
# Author : zijing (zijing412@163.com)
###################################################
import psutil


def test():
    print('CPU逻辑数量: ', psutil.cpu_count())
    print('getloadavg : ', psutil.getloadavg())
    print('cpu 空闲率 : ', psutil.cpu_percent())
    print('cpu 频率   : ', psutil.cpu_freq())
    print('cpu 统计   : ', psutil.cpu_stats())
    print('cpu times  : ', psutil.cpu_times())
    print('cpu times% : ', psutil.cpu_times_percent())
    

if __name__ == '__main__':
    test()
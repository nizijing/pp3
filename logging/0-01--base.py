#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-03-29 16:56:14
# Author : zijing (zijing412@163.com)
###################################################
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

'''Formatter说明
%(name)s            Logger的名字
%(levelname)s       文本形式的日志级别
%(message)s         用户输出的消息
%(asctime)s         字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(levelno)s         数字形式的日志级别
%(pathname)s        调用日志输出函数的模块的完整路径名，可能没有
%(filename)s        调用日志输出函数的模块的文件名
%(module)s          调用日志输出函数的模块名
%(funcName)s        调用日志输出函数的函数名
%(lineno)d          调用日志输出函数的语句所在的代码行
%(created)f         当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时来自Logger创建的毫秒数
%(thread)d          线程ID。可能没有
%(threadName)s      线程名。可能没有
%(process)d         进程ID。可能没有
'''


def test_logger():
    runner = 'user'
    logger = logging.getLogger(runner)
    screenhand = logging.StreamHandler()   # 输出到屏幕
    filehand = logging.FileHandler('logging/log/run.log')   # 同时输出到文件
    daterotehand = TimedRotatingFileHandler(
        filename='logging/log/run-date.log', # 以日期切割
        encoding='utf8',
        when='D',         # D 天；H 小时；M 分；S秒
        interval=1,       # 间隔
        backupCount=7     # 留7份
        )
    sizerotehand = RotatingFileHandler(     # 用法同上(可以print(help(RotatingFileHandler)) 查看更多细节)
        filename='logging/log/run-size.log',
        mode='a',
        encoding='utf8',
        maxBytes=1024 * 1024 * 20,
        backupCount=3
        )
    
    logger.setLevel(logging.DEBUG)      # 比这个要高的消息才会继续传递
    screenhand.setLevel(logging.INFO)
    filehand.setLevel(logging.ERROR)

    # 设置日志格式，见Formatter说明
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s")
    simpleFormatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s")

    daterotehand.setFormatter(simpleFormatter)
    filehand.setFormatter(formatter)
    screenhand.setFormatter(simpleFormatter)

    logger.addHandler(screenhand) 
    logger.addHandler(filehand)
    logger.addHandler(daterotehand)

    logger.debug('debug: ')
    logger.info('info: ')
    logger.warning('warning: ')
    logger.error('error: ')
    logger.critical('critical: ')


def main():
    test_logger()

if __name__ == '__main__':
    main()

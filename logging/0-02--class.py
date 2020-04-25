#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-04-25 17:41:48
# Author : zijing (zijing412@163.com)
###################################################
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

class myLog():
    # 将日志输出到指定路径和屏幕
    __logpath = 'logs/run.log'
    __fmt = "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s"

    def __init__(self):
        self.__screenhand = logging.StreamHandler()   # 输出到屏幕
        self.__screenhand.setLevel(logging.DEBUG)
        self.__screenhand.setFormatter(logging.Formatter(self.__fmt))

    def getInstance(self, strlogger, logpath=__logpath):
        logger = logging.getLogger(strlogger)
        logger.setLevel(logging.DEBUG)  # 比这个要高的消息才会继续传递

        daterotehand = TimedRotatingFileHandler(
        filename=logpath, # 以日期切割
        encoding='utf8',
        when='D',         # D 天；H 小时；M 分；S秒
        interval=1,       # 间隔
        backupCount=7     # 留7份
        )
        daterotehand.setLevel(logging.INFO)
        daterotehand.setFormatter(logging.Formatter(self.__fmt))

        logger.addHandler(self.__screenhand) 
        logger.addHandler(daterotehand)

        return logger

def main():
    log = myLog().getInstance('mainlog', logpath='logging/log/class.log')
    log.debug('test for debug')
    log.info('test for info')
    log.warning('test for warning')
    log.error('test for error')
    log.critical('test for critical')

if __name__ == '__main__':
    main()

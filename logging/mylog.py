#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-04-25 17:41:48
# Author : zijing (zijing412@163.com)
###################################################
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler


class myLog(logging.Logger):
    def __init__(self,
                name, 
                hander_level="INFO",    # 处理器级别，优先级更高
                level = "INFO",         # 日志级别
                file_name = None,
                fmt = "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s"
                ):
        super().__init__(name, level = level)
        if file_name is not None:
            hander = TimedRotatingFileHandler(  # 输出到文件
                filename=file_name, # 日志路径
                encoding='utf8',
                when='D',         # D 天；H 小时；M 分；S秒
                interval=1,       # 间隔
                backupCount=7     # 留7份
            )
        else:
            hander = logging.StreamHandler()    # 输出到屏幕
        self.addHandler(hander)         # 添加hander
        hander.setLevel(hander_level)   # 设置处理器级别
        hander.setFormatter(logging.Formatter(fmt)) # 设置fmt的格式：日志的显示样式


def test():
    log = myLog('mainlog', level="INFO", hander_level="DEBUG")
    log.debug('test for debug')
    log.info('test for info')
    log.warning('test for warning')
    log.error('test for error')
    log.critical('test for critical')

if __name__ == '__main__':
    test()

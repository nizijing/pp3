#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-30 17:07:25
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
import signal

class TimeoutException(Exception):
    def __init__(self, error='Timeout waiting for response from Cloud'):
        Exception.__init__(self, error)


def timeout_limit(timeout_time = 1):
    def wraps(func):
        def handler(signum, frame):
            raise TimeoutException()

        def deco(*args, **kwargs):
            # linux和windows的信号不一样
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(timeout_time)
            func(*args, **kwargs)
            signal.alarm(0)
        return deco
    return wraps


from time import sleep
@timeout_limit(1)
def demo(sleepTime):
    sleep(sleepTime)
    print('finish sleep: ', sleepTime)


demo(0.5)
demo(5)
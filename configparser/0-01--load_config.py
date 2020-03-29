#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-03-24 20:01:23
# Author : zijing (zijing412@163.com)
###################################################
import configparser
import sys

'''
配置文件test.cfg文件中内容如下

[mysqld]
user = mysql
port = 3306
'''

def load_from_filepath():
    '''
    这个方法最简单异懂
    第1, 判断mysqld这个域在不在
    第2, 判断mysqld这个域下有没有port这个变量
    第3, 加载配置
    但配置多起来的时候代码很难看，灵活性差
    '''
    filepath = 'configparser/test.cfg'
    mysql_conf = configparser.ConfigParser()
    mysql_conf.read(filepath)

    if mysql_conf.has_section('mysqld'):
        if mysql_conf.has_option('mysqld', 'port'):
            port = mysql_conf.getint('mysqld', 'port')

    return port

def try_load_from_filepath():
    '''
    用try包装，稍微好看了点，但和上一个方法半斤八两
    '''
    filepath = 'configparser/test.cfg'
    mysql_conf = configparser.ConfigParser()
    mysql_conf.read(filepath)
    try:
        port = mysql_conf.getint('mysqld', 'port')
    except Exception as err:
        print(str(err))
    
    return port

def load_with_dict():
    '''
    利用items()便利字典，不管有多少变量都一起读过来
    '''
    mysql_conf = configparser.ConfigParser()
    mysql_cfg = {
        'mysqld': {
            'user': 'mysql',
            'port': 3306
        }
    }
    mysql_conf.read_dict(mysql_cfg)
    ret = {}

    for section, option_dict in mysql_conf.items():
        ret[section] = {}
        for option, val in option_dict.items():
            ret[section][option] = val
    return ret

def main():
    print(load_from_filepath())         # unflexible
    print(try_load_from_filepath())     # too heavy
    print(load_with_dict())             # 初具雏形，还要优化 

if __name__ == '__main__':
    main()

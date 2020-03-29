#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-03-29 12:21:36
# Author : zijing (zijing412@163.com)
###################################################
import configparser

def load_with_init_dict():
    '''
    先初始化一个默认配置字典，然后读取配置字典
    再读取配置文件
    再字典遍历
    '''
    
    DEFAULT_CONF = {
        'DEFAULT': { 
            'user': 'mysql',
            'port': 3306,
            'expire_logs_days': 7
            }
        }

    mysql_conf = configparser.ConfigParser()
    filepath = 'configparser/test.cfg'
    mysql_conf.read_dict(DEFAULT_CONF)
    mysql_conf.read(filepath)

    ret = {}
    ret['DEFAULT'] = {}

    for section, option_dict in mysql_conf.items():
        ret[section] = {}
        for option, val in option_dict.items():
            ret[section][option] = val
    
    return ret

def main():
    print(load_with_init_dict())      

if __name__ == '__main__':
    main()
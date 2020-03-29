#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-03-29 15:44:09
# Author : zijing (zijing412@163.com)
###################################################
import configparser

'''配置文件内容
[mysqld2]
port = 3307

[mysqld3]
port = 3308
expire_logs_days = 14
'''

def get_conf_val(conf):
    cfg = {}
    cfg['DEFAULT'] = {}
    for section in conf.sections():
        cfg[section] = {}

    for section, option_dict in conf.items():
        for option, val in option_dict.items():
            cfg[section][option] = val
    return cfg

def main():
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
    
    cfg = get_conf_val(mysql_conf)

    mysql_conf.add_section('mysqld1')
    mysql_conf.remove_section('mysqld2')

    mysql_conf.set('mysqld1', 'port', '3306')
    mysql_conf.remove_option('mysqld3', 'expire_logs_days')

    mysql_conf.set('DEFAULT', 'user', 'root')
    
    mysql_conf.update(cfg)  # 慎用

    mysql_conf.write(open('configparser/test_save.cfg', 'w'))
    

if __name__ == '__main__':
    main()

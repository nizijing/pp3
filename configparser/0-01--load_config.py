#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-03-24 20:01:23
# Author : zijing (zijing412@163.com)
###################################################
import configparser

def main():
    filepath = 'configparser/test.cfg'
    mysql_conf = configparser.ConfigParser()
    mysql_conf.read(filepath)

    user = mysql_conf.get('mysqld', 'user')
    port = mysql_conf.getint('mysqld', 'port')
    server_id = mysql_conf.getint('mysqld', 'server-id')

    print(user, port, server_id)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-04-20 08:42:12
# Author : zijing (zijing412@163.com)
###################################################
from ldap3 import Server, Connection, SUBTREE, ALL_ATTRIBUTES
from ldap3.core.exceptions import LDAPBindError
from ldap3 import MODIFY_REPLACE, MODIFY_ADD, MODIFY_DELETE
from ldap3.utils.dn import safe_rdn
from ldap3.abstract import entry
from setting import ldap_config


class C_LDAP(object):
    def __init__(self, host, port, base_dn, group_dn, user, password):
        self.__host     = host
        self.__port     = port
        self.__base_dn  = base_dn
        self.__group_dn = group_dn
        self.__user     = user
        self.__password = password
        self.__server = Server(self.__host, self.__port)
        self.__conn = Connection(self.__server, self.__user, self.__password, auto_bind = True)

    def show_base_info(self):
        print(self.__conn)

def main():
    ldap = C_LDAP(**ldap_config)
    print('测试连接是否成功: ')
    ldap.show_base_info()

if __name__ == '__main__':
    main()

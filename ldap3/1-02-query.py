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
        self.staff_data = {}

    def show_base_info(self):
        print(self.__conn)

    def get_userdn_by_args(self, base_dn=None, **kwargs):
        # 主要的搜索函数，所有的搜索功能汇聚于此
        # 参考连接：https://www.cnblogs.com/NoSong/p/11904477.html
        search = ""
        for k, v in kwargs.items():
            search += "(%s=%s)" % (k, v)
        if not base_dn:
            base_dn = self.__base_dn
        if search:
            search_filter = '(&{})'.format(search)
        else:
            search_filter = ''
        status = self.__conn.search(base_dn,
                                    search_filter=search_filter,
                                    search_scope=SUBTREE,
                                    attributes=ALL_ATTRIBUTES)
        if status:
            return self.__conn.entries
        else:
            return False

    def get_staff_data(self, ou='Users', objectclass = 'inetOrgPerson'):
        for line in  self.get_userdn_by_args(base_dn = self.__base_dn, objectclass = objectclass):
            self.staff_data[line.entry_attributes_as_dict['uid'][0]] = line.entry_attributes_as_dict
        return self.staff_data

def main():
    ldap = C_LDAP(**ldap_config)
    print('测试连接是否成功: ')
    ldap.show_base_info()
    print('测试获取人员信息：')
    for key, val in ldap.get_staff_data()['nizj'].items():
        print(key, val)

if __name__ == '__main__':
    main()

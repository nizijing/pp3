# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# user: zijing.ni
# date: 2022/4/29
import os
from common.common import check_confpath
from P4 import P4


def p4connetc(func):
    def wrapper(self, *args, **kwargs):
        self.p4.connect()
        ret = func(self, *args, **kwargs)
        self.p4.disconnect()
        return ret
    return wrapper


class p4API(object):
    def __init__(self, p4port, p4user, p4passwd, logpath='p4api.log'):
        self.name = 'devops'
        self.p4 = P4()
        self.p4port = p4port
        self.p4user = p4user
        self.p4.port = p4port
        self.p4.user = p4user
        self.p4.password = p4passwd
        self.usage = '''usage:\n  main.py terminate\n  main.py clear'''


    @p4connetc
    def kill_process_daily(self, cmd):
        if cmd not in ['terminate', 'clear']:
            print(self.usage)
            return
        for p4process in self.p4.run('monitor', 'show', '-a'):
            if int(p4process['time'].split(':')[0]) >= 8:
                self.p4.run('monitor', cmd, p4process['id'])


    @p4connetc
    def show_process(self):
        return self.p4.run('monitor', 'show', '-a')

    @p4connetc
    def run_p4_del(self, cmd, timeThread=8, user=None):
        for p4process in self.p4.run('monitor', 'show', '-a'):
            if int(p4process['time'].split(':')[0]) >= timeThread:
                self.p4.run('monitor', cmd, p4process['id'])


    @p4connetc
    def p4_run(self, *args):
        return self.p4.run(args)


    def getp4groupName(self, p4port, p4user):
        f= os.popen('p4 -u {} -p {} groups'.format(p4user, p4port))
        return [ line.rstrip() for line in f.readlines()]


    @p4connetc
    def isUserInP4(self, username):
        user_ = self.p4.fetch_user(username)
        if len(user_) > 3:
            print(user_)
            return True
        else:
            return False


    @p4connetc
    def create_user(self, username, passwd):
        # get_user_detail_from_feishu
        # create_user
        pass


    def add_user_to_group(self, username, groupnamelist):
        # get_user_current_group
        # get_user_dest_group
        # add_user_to_group
        pass


if __name__ == '__main__':
    check_confpath('setting.py')
    import conf.setting as st

    p4api = p4API(st.P4PORT, st.P4USER, st.P4PASSWD)
    print(p4api.p4_run('group', 'admin'))
    p4api.isUserInP4('zijing.ni')
    p4api.isUserInP4('uuuuuu')

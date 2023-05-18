# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# user: zijing.ni
# date: 2022/12/6

import wx
from p4.p4Frame import FrameGUI, PanP4, PanP4user
from p4.p4api import p4API


class P4Logic(PanP4):
    def __init__(self, parent):
        PanP4.__init__(self, parent)
        import conf.setting as st
        self.p4user = st.P4USER
        self.p4passwd = st.P4PASSWD
        self.p4api = p4API(self.cbox_p4url.GetValue(), self.p4user, self.p4passwd)

    # Handlers for p4Frame events.
    def onShow(self, event):
        self.textCtrl_output.SetValue('')
        for p4process in self.p4api.show_process():
            self.textCtrl_output.AppendText('{}\n'.format(p4process))

    def onTerminate(self, event):
        self.textCtrl_output.SetValue('')
        self.runP4del('terminate')
        pass

    def onClear(self, event):
        self.textCtrl_output.SetValue('')
        self.runP4del('clear')
        pass

    def runP4del(self, cmd):
        timeThreshold = int(self.textCtrl_overtime.GetValue())
        for p4process in self.p4api.show_process():
            if int(p4process['time'].split(':')[0]) >= timeThreshold:
                self.textCtrl_output.AppendText('{} {:8} {:2} {:16} {}\n'.
                                                format(cmd, p4process['id'], p4process['status'], p4process['user'],
                                                       p4process['time']))

                self.p4api.p4_run('monitor', cmd, p4process['id'])


class P4UserLogic(PanP4user):
    def __init__(self, parent):
        PanP4user.__init__(self, parent)
        self.cBox_p4List.Clear()
        import conf.setting as st
        self.p4list = st.P4LIST
        self.p4user = st.P4USER
        self.p4passwd = st.P4PASSWD
        self.cBox_p4List.Append(self.p4list)

    def get_p4_group(self):
        self.p4api = p4API(self.cBox_p4List.GetValue(), self.p4user, self.p4passwd)
        p4groups = self.p4api.getp4groupName(self.p4port, self.p4user)
        self.lBox_groupList.Clear()
        self.lBox_groupList.Append(p4groups)

    def OB_SETP4PORT(self, event):
        self.p4port = self.cBox_p4List.GetValue()
        self.groups = None
        self.m_msg.SetValue(self.p4port + '\n')
        self.get_p4_group()

    def On_ChoiceGroup(self, event):
        self.groups = [self.lBox_groupList.GetString(group_id) for group_id in self.lBox_groupList.GetSelections()]
        self.m_msg.AppendText('groups: {}\n'.format(self.groups))

    def create_user(self, username):
        if self.isUserInP4(username):
            # self.p4api.add_user_to_group(username, self.groups)
            self.m_msg.AppendText("user {} is in p4".format(username))
            # self.feishu_msg(username, title, msg) # permission is given
        else:
            # passwd = randonpasswd()
            self.p4api.create_user(username, passwd)
            # self.p4api.add_user_to_group(username, self.groups)
            # self.feishu_msg(username, title, msg) # p4_port / p4_user / p4_passwd

    def On_createUser(self, event):
        if not self.groups:
            self.m_msg.AppendText("请选择组\n")
            return
        users_ = [user_ for user_ in self.msg_userList.GetValue().split('\n') if user_ != '']
        if not users_:
            self.m_msg.AppendText("请添加用户\n")
            return
        self.m_msg.AppendText("users: {}\n".format(users_))
        for username in users_:
            self.create_user(username)


class p4GUILogic(FrameGUI):
    def __init__(self, parent):
        FrameGUI.__init__(self, parent)

        self.p4panel = P4Logic(self)
        self.p4panel.Hide()
        self.panels = [self.p4panel]
        self.p4userpanel = P4UserLogic(self)
        self.panels.append(self.p4userpanel)

    def OM_switchP4(self, event):
        if self.p4panel.IsShown():
            return
        for panel in self.panels:
            panel.Hide()
        self.p4panel.Show()

    def OM_SwitchToP4user(self, event):
        if self.p4userpanel.IsShown():
            return
        for panel in self.panels:
            panel.Hide()
        self.p4userpanel.Show()

    def OM_cmd(self, event):
        event.Skip()
import wx
from p4.P4Class import p4GUILogic
from common.common import check_confpath


def main():
    check_confpath('setting.py')
    app = wx.App()
    p4GUILogic(None).Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
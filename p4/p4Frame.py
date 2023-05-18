# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FrameGUI
###########################################################################

class FrameGUI ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 875,655 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar_start = wx.MenuBar( 0 )
        self.menu_start = wx.Menu()
        self.mi_p4 = wx.MenuItem( self.menu_start, wx.ID_ANY, u"p4", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_start.Append( self.mi_p4 )

        self.mi_p4user = wx.MenuItem( self.menu_start, wx.ID_ANY, u"p4user", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_start.Append( self.mi_p4user )

        self.mi_cmd = wx.MenuItem( self.menu_start, wx.ID_ANY, u"命令一览", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_start.Append( self.mi_cmd )

        self.mi_help = wx.MenuItem( self.menu_start, wx.ID_ANY, u"帮助", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_start.Append( self.mi_help )

        self.m_menubar_start.Append( self.menu_start, u"开始" )

        self.SetMenuBar( self.m_menubar_start )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.OM_switchP4, id = self.mi_p4.GetId() )
        self.Bind( wx.EVT_MENU, self.OM_SwitchToP4user, id = self.mi_p4user.GetId() )
        self.Bind( wx.EVT_MENU, self.OM_cmd, id = self.mi_cmd.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OM_switchP4( self, event ):
        event.Skip()

    def OM_SwitchToP4user( self, event ):
        event.Skip()

    def OM_cmd( self, event ):
        event.Skip()


###########################################################################
## Class PanP4
###########################################################################

class PanP4 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 860,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer = wx.BoxSizer( wx.VERTICAL )

        sbSizerInput = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"输入" ), wx.HORIZONTAL )

        self.s_p4url = wx.StaticText( sbSizerInput.GetStaticBox(), wx.ID_ANY, u"p4url", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.s_p4url.Wrap( -1 )

        sbSizerInput.Add( self.s_p4url, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        cbox_p4urlChoices = []
        self.cbox_p4url = wx.ComboBox( sbSizerInput.GetStaticBox(), wx.ID_ANY, u"p4.booming.com:7777", wx.DefaultPosition, wx.DefaultSize, cbox_p4urlChoices, 0 )
        sbSizerInput.Add( self.cbox_p4url, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.s_timeover = wx.StaticText( sbSizerInput.GetStaticBox(), wx.ID_ANY, u"超时时间", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.s_timeover.Wrap( -1 )

        sbSizerInput.Add( self.s_timeover, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.textCtrl_overtime = wx.TextCtrl( sbSizerInput.GetStaticBox(), wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizerInput.Add( self.textCtrl_overtime, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.s_name = wx.StaticText( sbSizerInput.GetStaticBox(), wx.ID_ANY, u"指定人员", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.s_name.Wrap( -1 )

        sbSizerInput.Add( self.s_name, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.testCtrl_name = wx.TextCtrl( sbSizerInput.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizerInput.Add( self.testCtrl_name, 0, wx.ALL, 5 )


        bSizer.Add( sbSizerInput, 0, wx.EXPAND, 5 )

        sbSizer_ope = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"操作" ), wx.HORIZONTAL )

        self.btn_show = wx.Button( sbSizer_ope.GetStaticBox(), wx.ID_ANY, u"查看", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer_ope.Add( self.btn_show, 0, wx.ALL, 5 )

        self.btn_terminate = wx.Button( sbSizer_ope.GetStaticBox(), wx.ID_ANY, u"标记删除", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer_ope.Add( self.btn_terminate, 0, wx.ALL, 5 )

        self.btn_clear = wx.Button( sbSizer_ope.GetStaticBox(), wx.ID_ANY, u"真实删除", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer_ope.Add( self.btn_clear, 0, wx.ALL, 5 )


        bSizer.Add( sbSizer_ope, 0, wx.EXPAND, 5 )

        sbSizer_output = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"输出" ), wx.HORIZONTAL )

        self.textCtrl_output = wx.TextCtrl( sbSizer_output.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        sbSizer_output.Add( self.textCtrl_output, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer.Add( sbSizer_output, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer )
        self.Layout()

        # Connect Events
        self.btn_show.Bind( wx.EVT_BUTTON, self.onShow )
        self.btn_terminate.Bind( wx.EVT_BUTTON, self.onTerminate )
        self.btn_clear.Bind( wx.EVT_BUTTON, self.onClear )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onShow( self, event ):
        event.Skip()

    def onTerminate( self, event ):
        event.Skip()

    def onClear( self, event ):
        event.Skip()


###########################################################################
## Class PanP4user
###########################################################################

class PanP4user ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 860,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bsize_p4user = wx.BoxSizer( wx.HORIZONTAL )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer_input = wx.BoxSizer( wx.HORIZONTAL )

        self.s_user1 = wx.StaticText( self, wx.ID_ANY, u"p4", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.s_user1.Wrap( -1 )

        bSizer_input.Add( self.s_user1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        cBox_p4ListChoices = [ u"p4.booming-inc.com:7777", u"p4mars.booming-inc.com:6666", u"awaken.booming-inc.com:3333" ]
        self.cBox_p4List = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cBox_p4ListChoices, 0 )
        bSizer_input.Add( self.cBox_p4List, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.s_user = wx.StaticText( self, wx.ID_ANY, u"用户", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.s_user.Wrap( -1 )

        bSizer_input.Add( self.s_user, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.msg_userList = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer_input.Add( self.msg_userList, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer6.Add( bSizer_input, 0, wx.EXPAND, 5 )

        self.btn_create = wx.Button( self, wx.ID_ANY, u"创建", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btn_create, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.m_msg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer6.Add( self.m_msg, 1, wx.ALL|wx.EXPAND, 5 )


        bsize_p4user.Add( bSizer6, 1, wx.EXPAND, 5 )

        sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"组" ), wx.VERTICAL )

        lBox_groupListChoices = []
        self.lBox_groupList = wx.ListBox( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lBox_groupListChoices, wx.LB_MULTIPLE )
        self.lBox_groupList.SetMinSize( wx.Size( 150,-1 ) )

        sbSizer4.Add( self.lBox_groupList, 1, wx.ALL|wx.EXPAND, 5 )


        bsize_p4user.Add( sbSizer4, 0, wx.EXPAND, 5 )


        self.SetSizer( bsize_p4user )
        self.Layout()

        # Connect Events
        self.cBox_p4List.Bind( wx.EVT_COMBOBOX, self.OB_SETP4PORT )
        self.btn_create.Bind( wx.EVT_BUTTON, self.On_createUser )
        self.lBox_groupList.Bind( wx.EVT_LISTBOX, self.On_ChoiceGroup )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OB_SETP4PORT( self, event ):
        event.Skip()

    def On_createUser( self, event ):
        event.Skip()

    def On_ChoiceGroup( self, event ):
        event.Skip()



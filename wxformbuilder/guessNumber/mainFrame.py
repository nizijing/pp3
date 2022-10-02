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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"猜数字", pos = wx.DefaultPosition, size = wx.Size( 485,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.menubar = wx.MenuBar( 0 )
        self.menuBar_game = wx.Menu()
        self.menu_gameRetry = wx.MenuItem( self.menuBar_game, wx.ID_ANY, u"重新开始", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuBar_game.Append( self.menu_gameRetry )

        self.menuBar_game.AppendSeparator()

        self.menu_gameQuit = wx.MenuItem( self.menuBar_game, wx.ID_ANY, u"退出", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuBar_game.Append( self.menu_gameQuit )

        self.menubar.Append( self.menuBar_game, u"游戏" )

        self.menuBar_help = wx.Menu()
        self.game_help = wx.MenuItem( self.menuBar_help, wx.ID_ANY, u"帮助", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuBar_help.Append( self.game_help )

        self.game_about = wx.MenuItem( self.menuBar_help, wx.ID_ANY, u"关于", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuBar_help.Append( self.game_about )

        self.menubar.Append( self.menuBar_help, u"help" )

        self.SetMenuBar( self.menubar )

        bSizerGlobal = wx.BoxSizer( wx.VERTICAL )

        bSizerInputAndGuess = wx.BoxSizer( wx.HORIZONTAL )

        self.input_num = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_LEFT|wx.FULL_REPAINT_ON_RESIZE )
        bSizerInputAndGuess.Add( self.input_num, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btn_guess = wx.Button( self, wx.ID_ANY, u"猜测", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        bSizerInputAndGuess.Add( self.btn_guess, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizerGlobal.Add( bSizerInputAndGuess, 0, wx.EXPAND, 5 )

        bSizerHistoryMsg = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"历史信息" ), wx.VERTICAL )

        self.history_msg = wx.TextCtrl( bSizerHistoryMsg.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizerHistoryMsg.Add( self.history_msg, 1, wx.ALL|wx.EXPAND, 5 )


        bSizerGlobal.Add( bSizerHistoryMsg, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizerGlobal )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.onGameInit, id = self.menu_gameRetry.GetId() )
        self.Bind( wx.EVT_MENU, self.onQuit, id = self.menu_gameQuit.GetId() )
        self.Bind( wx.EVT_MENU, self.onGameHelp, id = self.game_help.GetId() )
        self.Bind( wx.EVT_MENU, self.onAbout, id = self.game_about.GetId() )
        self.btn_guess.Bind( wx.EVT_LEFT_DOWN, self.onGuessNum )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onGameInit( self, event ):
        event.Skip()

    def onQuit( self, event ):
        event.Skip()

    def onGameHelp( self, event ):
        event.Skip()

    def onAbout( self, event ):
        event.Skip()

    def onGuessNum( self, event ):
        event.Skip()



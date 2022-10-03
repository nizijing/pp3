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
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"devops", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer = wx.BoxSizer( wx.VERTICAL )

        self.staicTitle = wx.StaticText( self, wx.ID_ANY, u"题目", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staicTitle.Wrap( -1 )

        bSizer.Add( self.staicTitle, 1, wx.ALL|wx.EXPAND, 5 )

        bSizeSolve = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"答题区" ), wx.HORIZONTAL )

        self.solveInput = wx.TextCtrl( bSizeSolve.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizeSolve.Add( self.solveInput, 1, wx.ALL|wx.EXPAND, 5 )

        self.btnSolve = wx.Button( bSizeSolve.GetStaticBox(), wx.ID_ANY, u"解答", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizeSolve.Add( self.btnSolve, 0, wx.ALL, 5 )


        bSizer.Add( bSizeSolve, 1, wx.EXPAND, 5 )

        bSizeAnswer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"答案区" ), wx.VERTICAL )

        self.m_textCtrl4 = wx.TextCtrl( bSizeAnswer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizeAnswer.Add( self.m_textCtrl4, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer.Add( bSizeAnswer, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnSolve.Bind( wx.EVT_BUTTON, self.onBtnSolveClick )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onBtnSolveClick( self, event ):
        event.Skip()



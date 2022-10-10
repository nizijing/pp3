# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.mbar_main = wx.MenuBar( 0 )
        self.menu_start = wx.Menu()
        self.mitem_switchToGrid = wx.MenuItem( self.menu_start, wx.ID_ANY, u"grid", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_start.Append( self.mitem_switchToGrid )

        self.mitem_switchToText = wx.MenuItem( self.menu_start, wx.ID_ANY, u"text", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_start.Append( self.mitem_switchToText )

        self.mbar_main.Append( self.menu_start, u"开始" )

        self.SetMenuBar( self.mbar_main )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.OnM_switchToGrid, id = self.mitem_switchToGrid.GetId() )
        self.Bind( wx.EVT_MENU, self.OnM_switchToText, id = self.mitem_switchToText.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnM_switchToGrid( self, event ):
        event.Skip()

    def OnM_switchToText( self, event ):
        event.Skip()


###########################################################################
## Class panelGrid
###########################################################################

class panelGrid ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer = wx.BoxSizer( wx.VERTICAL )

        self.grid_test = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.grid_test.CreateGrid( 10, 5 )
        self.grid_test.EnableEditing( True )
        self.grid_test.EnableGridLines( True )
        self.grid_test.EnableDragGridSize( False )
        self.grid_test.SetMargins( 0, 0 )

        # Columns
        self.grid_test.EnableDragColMove( False )
        self.grid_test.EnableDragColSize( True )
        self.grid_test.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.grid_test.EnableDragRowSize( True )
        self.grid_test.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.grid_test.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer.Add( self.grid_test, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer )
        self.Layout()

    def __del__( self ):
        pass


###########################################################################
## Class panel2
###########################################################################

class panel2 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer = wx.BoxSizer( wx.VERTICAL )

        self.s_helloWorld = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.s_helloWorld.Wrap( -1 )

        bSizer.Add( self.s_helloWorld, 0, wx.ALL, 5 )


        self.SetSizer( bSizer )
        self.Layout()

    def __del__( self ):
        pass



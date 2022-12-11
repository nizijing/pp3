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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"devops", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer = wx.BoxSizer( wx.VERTICAL )

        bSizer_cfg = wx.BoxSizer( wx.HORIZONTAL )

        self.staicTitle = wx.StaticText( self, wx.ID_ANY, u"纲目", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staicTitle.Wrap( -1 )

        bSizer_cfg.Add( self.staicTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_comboBox_questionsChoices = []
        self.m_comboBox_questions = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size( 120,-1 ), m_comboBox_questionsChoices, 0 )
        bSizer_cfg.Add( self.m_comboBox_questions, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btnGetQuestion = wx.Button( self, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_cfg.Add( self.btnGetQuestion, 0, wx.ALL, 5 )

        self.m_staticText_ca = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_ca.Wrap( -1 )

        bSizer_cfg.Add( self.m_staticText_ca, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer.Add( bSizer_cfg, 0, wx.EXPAND, 5 )

        bSizer_btn = wx.BoxSizer( wx.HORIZONTAL )

        self.btnGetAnswer = wx.Button( self, wx.ID_ANY, u"查看答案", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btnGetAnswer.Enable( False )

        bSizer_btn.Add( self.btnGetAnswer, 0, wx.ALL, 5 )

        self.btnAnswerRight = wx.Button( self, wx.ID_ANY, u"回答正确", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btnAnswerRight.Enable( False )

        bSizer_btn.Add( self.btnAnswerRight, 0, wx.ALL, 5 )

        self.btnAnswerWrong = wx.Button( self, wx.ID_ANY, u"回答不正确", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btnAnswerWrong.Enable( False )

        bSizer_btn.Add( self.btnAnswerWrong, 0, wx.ALL, 5 )


        bSizer.Add( bSizer_btn, 0, wx.EXPAND, 5 )

        bSize_question = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"问题" ), wx.VERTICAL )

        bSizer_question_title = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText_question_title = wx.StaticText( bSize_question.GetStaticBox(), wx.ID_ANY, u"题目", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_question_title.Wrap( -1 )

        bSizer_question_title.Add( self.m_staticText_question_title, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl_question_title = wx.TextCtrl( bSize_question.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_question_title.Add( self.m_textCtrl_question_title, 1, wx.ALL|wx.EXPAND, 5 )


        bSize_question.Add( bSizer_question_title, 0, wx.EXPAND, 5 )

        bSizer_question_description = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText_question_description = wx.StaticText( bSize_question.GetStaticBox(), wx.ID_ANY, u"描述", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_question_description.Wrap( -1 )

        bSizer_question_description.Add( self.m_staticText_question_description, 0, wx.ALL, 5 )

        self.m_textCtrl_question_description = wx.TextCtrl( bSize_question.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer_question_description.Add( self.m_textCtrl_question_description, 1, wx.ALL|wx.EXPAND, 5 )


        bSize_question.Add( bSizer_question_description, 1, wx.EXPAND, 5 )


        bSizer.Add( bSize_question, 1, wx.EXPAND, 5 )

        bSizeAnswer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"答案区" ), wx.VERTICAL )

        self.m_textCtrl_answer = wx.TextCtrl( bSizeAnswer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizeAnswer.Add( self.m_textCtrl_answer, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer.Add( bSizeAnswer, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnGetQuestion.Bind( wx.EVT_BUTTON, self.onBtnClick_getQuestion )
        self.btnGetAnswer.Bind( wx.EVT_BUTTON, self.onBtnClick_viewAnswer )
        self.btnAnswerRight.Bind( wx.EVT_BUTTON, self.onBtnClick_answerRight )
        self.btnAnswerWrong.Bind( wx.EVT_BUTTON, self.onBtnClick_answerWrong )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onBtnClick_getQuestion( self, event ):
        event.Skip()

    def onBtnClick_viewAnswer( self, event ):
        event.Skip()

    def onBtnClick_answerRight( self, event ):
        event.Skip()

    def onBtnClick_answerWrong( self, event ):
        event.Skip()



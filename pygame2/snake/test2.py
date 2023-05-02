#-*- coding:utf-8 -*-
 
 
import wx
 
class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,u'登陆',size=(370,280),style=wx.MINIMIZE_BOX|
        wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX)
        self.SetBackgroundColour('white')
 
        self.button1 = wx.Button(self,-1,u'按钮1',pos = (80,180))
        self.button1.Bind(wx.EVT_BUTTON,self.OnButtonClick1)
 
        self.button2 = wx.Button(self,-1,u'按钮2',pos = (180,180))
        self.button2.Bind(wx.EVT_BUTTON,self.OnButtonClick2)
 
        #Button1显示组件
        self.text1 = None
        self.textc1 = None
 
        #Button2显示组件
        self.text2 = None
        self.textc2 = None
 
        
 
    def OnButtonClick1(self,event):
        if not self.text1:
            self.text1 = wx.StaticText(self,-1,u'用户名',(70,73),(50,-1),wx.ALIGN_CENTER)
            self.text1.SetBackgroundColour('black')#设置背景颜色
            self.text1.SetForegroundColour('white')#设置文本颜色
        if not self.textc1:
            self.textc1 = wx.TextCtrl(self,pos=(140,70))
 
        if self.text2:
            self.text2.Destroy()
        if self.textc2:
            self.textc2.Destroy()
    def OnButtonClick2(self,event):
        if self.text1:
            self.text1.Destroy()
        if self.textc1:
            self.textc1.Destroy()
 
        if not self.text2:
            self.text2 = wx.StaticText(self,-1,u'密码',(70,123),(50,-1),wx.ALIGN_CENTER)
            self.text2.SetBackgroundColour('black')#设置背景颜色
            self.text2.SetForegroundColour('white')#设置文本颜色
        if not self.textc2:
            self.textc2 = wx.TextCtrl(self,pos=(140,120), style=wx.TE_PASSWORD)
            
        
   
if __name__ == "__main__":
    
    app = wx.App()
    frame = TestFrame()
    frame.Show()
    app.MainLoop()
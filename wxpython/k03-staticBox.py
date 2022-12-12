import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        wx.StaticBox(pnl, label='个人信息', pos=(5,5), size=(240,170))
        wx.CheckBox(pnl, label='已婚', pos=(15,30))
        wx.StaticText(pnl, label='年龄', pos=(15, 95))
        wx.SpinCtrl(pnl, value='20', pos=(55, 90), size=(60, -1), min=1, max=120)

        btn = wx.Button(pnl, label='OK', pos=(90, 185), size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((270, 250))
        self.SetTitle('Static box')
        self.Centre()
        self.Show(True)

    
    def OnClose(self, e):
        self.Close(True)


if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()
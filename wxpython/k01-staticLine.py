import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(self, label = 'static line', pos=(130,15))
        heading.SetFont(font)
        wx.StaticLine(self, pos = (25, 50), size = (300, 1))
        
        btn = wx.Button(self, label='Close', pos=(140, 210))
        btn.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((360,280))
        self.SetTitle('wx.StaticLine')
        self.Centre()
        self.Show(True)

    def OnClose(self, e):
        self.Close(True)


if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()
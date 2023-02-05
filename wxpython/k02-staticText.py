import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        st1 = wx.StaticText(pnl, label='this is text.', style=wx.ALIGN_CENTRE)
        vbox.Add(st1, flag=wx.ALL, border=5)

        pnl.SetSizer(vbox)
        self.SetSize((220, 180))
        self.SetTitle('wx.StaticText')
        self.Centre()
        self.Show(True)


if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()
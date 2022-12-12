import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        # 创建一个 Close 按键，点击 Close 即可关闭应用
        cbtn = wx.Button(pnl, label='Close', pos=(20, 30))
        # 按钮的文本标签以及它在面板上的位置
        cbtn.Bind(wx.EVT_BUTTON, self.OnClose)
        self.SetSize((250, 200))
        self.SetTitle('wx.Button')
        self.Centre()
        self.Show(True)

    def OnClose(self, e):
        # 调用 Close() 函数来关闭应用
        self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()
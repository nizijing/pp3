import wx

class Example(wx.Frame):
    def __init__(self, parent):
        super(Example, self).__init__(parent, title='绝对定位', size=(260, 180))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self, -1)
        # 使用绝对定位，x=3、y=3，宽度250px、高度150px
        wx.TextCtrl(panel, pos=(3, 3), size=(250, 150))

if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()

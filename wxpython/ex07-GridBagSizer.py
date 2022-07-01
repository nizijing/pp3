import wx

class Example(wx.Frame):
    """创建一个大的 Grid 表"""
    def __init__(self, parent):
        super(Example, self).__init__(parent, title='wx.GridBagSizer', size=(320, 160))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)
        # "重命名为" 文本将被放置在左上角，所以设置了 (0,0) 位置，另外在顶部、左边和底部增加了 5px 的间隔空间
        text = wx.StaticText(panel, label="重命名为")
        sizer.Add(text, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        # wx.TextCtrl 从第二行开始，从0开始计数，它占据了1行和5列：(1,5)，放置了 5px 的左右边框空间
        tc = wx.TextCtrl(panel)
        sizer.Add(tc, pos=(1, 0), span=(1, 5), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
        buttonOk = wx.Button(panel, label="Ok", size=(90, 28))
        buttonClose = wx.Button(panel, label="Close", size=(90, 28))
        # 在第四行放置了2个 Button，第三行是空的，所以 wx.TextCtrl 和 Button 之间留有间隔，
        # 把 OK 按钮放在第四列，close 按钮放在第五列。需要注意，一旦给一个控件应用了边框，整行都会受到影响，
        # 这是没有为 OK 按钮设置底部边框空间的原因。因为在 wx.GridBagSizer 的构造函数中，已经设置了所有控件之间的间隔，
        # 所以在两个按钮之间没有放置任何空间。
        sizer.Add(buttonOk, pos=(3, 3))
        sizer.Add(buttonClose, pos=(3, 4), flag=wx.RIGHT | wx.BOTTOM, border=5)
        # 最后需要让对话框可增长，让第二列和第三行可增长，现在可以放大或者缩小窗口，注释掉则不能自动缩放
        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizerAndFit(sizer)


if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()

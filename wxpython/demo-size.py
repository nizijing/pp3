import wx


class Example(wx.Frame):
    """创建一个更复杂的布局，同时使用了 wx.GridBagSizer 和 wx.StaticBoxSizer"""
    def __init__(self, parent):
        super(Example, self).__init__(parent, title='wx.GridBagSizer Pro', size=(450, 370))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)
        text1 = wx.StaticText(panel, label="python")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=15)
        # 在第一行右侧放了一个 wx.StaticBitmap
        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('resources/python.png'))
        sizer.Add(icon, pos=(0, 4), flag=wx.TOP | wx.RIGHT | wx.ALIGN_RIGHT, border=5)
        # 创建一条分隔线，来分隔布局中不同组的控件
        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5), flag=wx.EXPAND | wx.BOTTOM, border=10)
        text2 = wx.StaticText(panel, label="名称")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)
        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND)
        text3 = wx.StaticText(panel, label="包")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT | wx.TOP, border=10)
        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        button1 = wx.Button(panel, label="浏览...")
        sizer.Add(button1, pos=(3, 4), flag=wx.TOP | wx.RIGHT, border=5)
        text4 = wx.StaticText(panel, label="继承")
        sizer.Add(text4, pos=(4, 0), flag=wx.TOP | wx.LEFT, border=10)
        combo = wx.ComboBox(panel)
        sizer.Add(combo, pos=(4, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        button2 = wx.Button(panel, label="浏览...")
        sizer.Add(button2, pos=(4, 4), flag=wx.TOP | wx.RIGHT, border=5)
        # wxStaticBoxSizer 和 wx.BoxSizer 类似，但它在 Sizer 周围添加了一个静态的盒子，在盒子中放入了 Check 选项
        sb = wx.StaticBox(panel, label="可选属性")
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer.Add(wx.CheckBox(panel, label="公有"), flag=wx.LEFT | wx.TOP, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="生成默认构造函数"), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="生成 Main 方法"), flag=wx.LEFT | wx.BOTTOM, border=5)
        sizer.Add(boxsizer, pos=(5, 0), span=(1, 5), flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        button3 = wx.Button(panel, label='帮助')
        sizer.Add(button3, pos=(7, 0), flag=wx.LEFT, border=10)
        button4 = wx.Button(panel, label="确定")
        sizer.Add(button4, pos=(7, 3))
        button5 = wx.Button(panel, label="取消")
        sizer.Add(button5, pos=(7, 4), span=(1, 1), flag=wx.BOTTOM | wx.RIGHT, border=5)
        sizer.AddGrowableCol(2)
        panel.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()
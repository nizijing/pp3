import wx

class Example(wx.Frame):
    """
    创建了红色、绿色和蓝色的 Toggle button 和一个 Panel，
    点击 toggle button的时候，可以改变 Panel 的颜色。
    """
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        self.col = wx.Colour(0, 0, 0)
        # 创建一个 wx.ToggleButton 控件
        rtb = wx.ToggleButton(pnl, label='red', pos=(20, 25))
        gtb = wx.ToggleButton(pnl, label='green', pos=(20, 60))
        btb = wx.ToggleButton(pnl, label='blue', pos=(20, 100))
        # 创建一个 Panel，颜色设置为 self.col
        self.cpnl = wx.Panel(pnl, pos=(150, 20), size=(110, 110))
        self.cpnl.SetBackgroundColour(self.col)
        # 点击 rtb 触发这个 button 的时候 ToggleRed() 会被调用
        rtb.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleRed)
        gtb.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleGreen)
        btb.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleBlue)
        self.SetSize((300, 200))
        self.SetTitle('Toggle buttons')
        self.Centre()
        self.Show(True)

    def ToggleRed(self, e):
        """对 rtb 按钮是否被按下做出反应，来改变特定面板的颜色"""
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        green = self.col.Green()
        blue = self.col.Blue()
        if isPressed:
            self.col.Set(255, green, blue)
        else:
            self.col.Set(0, green, blue)
        self.cpnl.SetBackgroundColour(self.col)
        self.cpnl.Refresh()

    def ToggleGreen(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        red = self.col.Red()
        blue = self.col.Blue()
        if isPressed:
            self.col.Set(red, 255, blue)
        else:
            self.col.Set(red, 0, blue)
        self.cpnl.SetBackgroundColour(self.col)
        self.cpnl.Refresh()

    def ToggleBlue(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        red = self.col.Red()
        green = self.col.Green()
        if isPressed:
            self.col.Set(red, green, 255)
        else:
            self.col.Set(red, green, 0)
        self.cpnl.SetBackgroundColour(self.col)
        self.cpnl.Refresh()


if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()
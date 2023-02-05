import wx

class Example(wx.Frame):
    def __init__(self, parent):
        super(Example, self).__init__(parent, title='String deal', size=(390, 350))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='字符串')
        st1.SetFont(font)

        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        vbox.Add((-1, 10))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='匹配类')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add((-1, 10))
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        # 虽然可以通过结合边框相关的 flag 参数来控制控件之间的距离，但问题是 Add() 函数只允许设置一个边框数值，
        # 这意味着只能给几个方向一样大小的边框，这种方法是无法做到左右边框设置为 10px，而底部设置为 25px 的情况
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)
        # 如果需要不同的边框值，可以增加额外的占位空间，如 vbox.Add((-1, 25)) 即是插入占位空间的语句，
        # (-1,25) 分别代表宽度和长度，如果某个数值为 -1 则表明不关注该方向

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='确定', size=(70, 30))
        hbox5.Add(btn1)
        btn2 = wx.Button(panel, label='关闭', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)
        # 在窗口的右侧放置了两个 Button，实现这个需求要三个参数：proportion、align flag 和 wx.EXPAND 标记，
        # proportion 必须设置为 0 ，表示在通过鼠标调整窗口大小时，Button 不允许更改大小，
        # 一定不能设置 wx.EXPAND 标记，因为 Button 只允许出现在被分配的位置上，
        # 最后必须设置 wx.ALIGN_RIGHT 标记，水平 Sizer 中的右对齐可以满足要求
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)
        panel.SetSizer(vbox)


if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()
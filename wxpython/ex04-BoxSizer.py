import wx

"""
box = wx.BoxSizer(integer orient)
wx.VERTICAL  竖直
wx.HORIZONTAL  水平
"""

"""
box.Add(wx.Window window, integer proportion=0, integer flag=0, integer border=0)

参数 proportion 表示在给定的方向中，控件按照什么比例来调整大小：
0   表示默认，不改变控件大小
1   表示控件以1倍调整大小
大于1   表示控件以1的N倍调整大小

flag 定义控件在 wx.BoxSizer 中的行为，通过它可以控制控件之间的距离，因而需要对不同方向的边界进行定义，不同方向之间可以通过竖线符号 | 组合，可选的方向为
wx.LEFT - 左
wx.RIGHT - 右
wx.BOTTOM - 底部
wx.TOP - 顶部
wx.ALL - 周围

wx.EXPAND 标记，控件将使用所有剩余的空间
wx.ALIGN_LEFT - 左对齐
wx.ALIGN_RIGHT - 右对齐
wx.ALIGN_TOP - 顶部对齐
wx.ALIGN_BOTTOM - 底部对齐
wx.ALIGN_CENTER_VERTICAL - 竖直居中对齐
wx.ALIGN_CENTER_HORIZONTAL - 水平居中对齐
wx.ALIGN_CENTER - 居中对齐
"""

class Example(wx.Frame):
    """在 Panel(面板)四周设置一些空间"""
    def __init__(self, parent):
        super(Example, self).__init__(parent, title='wx.BoxSizer', size=(260, 180))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#4f5049')
        vbox = wx.BoxSizer(wx.VERTICAL)
        midPan = wx.Panel(panel)
        midPan.SetBackgroundColour('#ededed')
        # 使用 wx.EXPAND 标记，控件将使用所有剩余的空间
        vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
        panel.SetSizer(vbox)


if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()

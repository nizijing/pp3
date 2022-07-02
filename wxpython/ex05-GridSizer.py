import wx

class Example(wx.Frame):
    # 创建一个计算器的框架
    def __init__(self, parent):
        super(Example, self).__init__(parent, title='wx.GridSizer', size=(300, 250))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        # 网格布局的构造函数中，我们可以定义表格的行列数，以及单元格之间的横竖间距
        # wx.GridSizer(int rows=1, int cols=0, int vgap=0, int hgap=0)
        gs = wx.GridSizer(5, 4, 5, 5)
        # 使用 AddMany() 方法，便于一次性插入多个控件
        gs.AddMany([(wx.Button(self, label='Cls'), 0, wx.EXPAND),
                    (wx.Button(self, label='Bck'), 0, wx.EXPAND),
                    # 在 Bck 和 Close 两个按钮之间放了一个空的 wx.StaticText，来达到分隔的目的
                    (wx.StaticText(self), wx.EXPAND),
                    (wx.Button(self, label='Close'), 0, wx.EXPAND),
                    (wx.Button(self, label='7'), 0, wx.EXPAND),
                    (wx.Button(self, label='8'), 0, wx.EXPAND),
                    (wx.Button(self, label='9'), 0, wx.EXPAND),
                    (wx.Button(self, label='/'), 0, wx.EXPAND),
                    (wx.Button(self, label='4'), 0, wx.EXPAND),
                    (wx.Button(self, label='5'), 0, wx.EXPAND),
                    (wx.Button(self, label='6'), 0, wx.EXPAND),
                    (wx.Button(self, label='*'), 0, wx.EXPAND),
                    (wx.Button(self, label='1'), 0, wx.EXPAND),
                    (wx.Button(self, label='2'), 0, wx.EXPAND),
                    (wx.Button(self, label='3'), 0, wx.EXPAND),
                    (wx.Button(self, label='-'), 0, wx.EXPAND),
                    (wx.Button(self, label='0'), 0, wx.EXPAND),
                    (wx.Button(self, label='.'), 0, wx.EXPAND),
                    (wx.Button(self, label='='), 0, wx.EXPAND),
                    (wx.Button(self, label='+'), 0, wx.EXPAND)])
        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()
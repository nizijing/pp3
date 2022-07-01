import wx

class Example(wx.Frame):
    """创建一个评论窗口"""
    def __init__(self, parent):
        super(Example, self).__init__(parent, title='wx.FlexGridSizer', size=(300, 250))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        # 创建一个水平的 Sizer
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # wx.FlexGridSizer(int rows=1, int cols=0, int vgap=0, int hgap=0)
        # rows 和 cols 定义行数和列数，vgap 和 hgap 定义两个方向的控件的间距
        fgs = wx.FlexGridSizer(3, 2, 9, 25)
        title = wx.StaticText(panel, label="标题")
        author = wx.StaticText(panel, label="作者")
        review = wx.StaticText(panel, label="评论")
        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        # 使用 AddMany() 添加控件到 Sizer 中，wx.FlexGridSizer 和 wx.GridSizer 都有这个方法
        fgs.AddMany(
            [(title), (tc1, 1, wx.EXPAND), (author), (tc2, 1, wx.EXPAND), (review, 1, wx.EXPAND), (tc3, 1, wx.EXPAND)])
        # 让第三行和第二列为可增长的，这使得窗口变化大小时，TextCtrl 也会跟着增长，
        # 前两个 TextCtrl 的宽度会增长，第三个会在两个方向都增长（注意：需要添加 wx.EXPAND 标记）
        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)
        # 在控件表格周围放置 15px 的空间
        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)

if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()
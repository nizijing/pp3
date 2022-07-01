import wx

class Example(wx.Frame):
    """
    把 wx.TextCtrl 放入 wx.Frame, 它有一个内置的 sizer, 但是只允许放置一个控件, 多于一个的话会得到混乱的布局, 
    放入的子控件占用了所有剩余空间，除去边框、菜单、工具栏和状态栏
    """
    def __init__(self, parent):
        super(Example, self).__init__(parent, title='内置的Sizer', size=(260, 180))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        menubar = wx.MenuBar()
        filem = wx.Menu()
        editm = wx.Menu()
        helpm = wx.Menu()
        menubar.Append(filem, '&文件')
        menubar.Append(editm, '&编辑')
        menubar.Append(helpm, '&帮助')
        self.SetMenuBar(menubar)
        # 没有显式的 sizer 定义
        wx.TextCtrl(self)

if __name__ == '__main__':
    app = wx.App()
    frm = Example(None)
    frm.Show()
    app.MainLoop()

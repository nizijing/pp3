import wx, random
from mainFrame import MainFrame

class mainGameLogic(MainFrame):
    def __init__( self, parent ):
        MainFrame.__init__( self, parent )
        self.gameInit()

    def onGuessNum( self, event ):
        guessnum = self.input_num.GetValue()
        if not guessnum:
            self.messagebox("请输入一个数")
            return
        guessnum = int(guessnum)
        result_msg = '猜大了'
        if self.num > guessnum:
            result_msg = '猜小了'
        elif self.num == guessnum:
            self.messagebox('恭喜你，猜中了')
            self.gameInit()
            return
        self.history_msg.AppendText('{:2d}'.format(guessnum) + result_msg + '\n')
        self.input_num.SetValue('')


    def onGameHelp( self, event ):
        self.messagebox("猜数字")


    def onGameInit( self, event ):
       self.gameInit()


    def messagebox(self, msg):
        c_dialog = wx.MessageDialog(None, msg, "游戏提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
        if c_dialog.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
            c_dialog.Destroy()  # 则关闭提示框

    def gameInit(self):
        self.num = random.randint (1,100)
        print(self.num)
        self.history_msg.SetValue('游戏开始!\n')
        self.input_num.SetValue('')


if __name__ == "__main__":
    app = wx.App()
    mgame = mainGameLogic(None)
    mgame.Show()
    app.MainLoop()
    
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-05-03 15:08:56
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
from tkinter import Tk, Label, Entry, Button, Text, messagebox
from tkinter import END
from random import randint


class cGuessNum():
    def __init__(self):
        self.root = Tk()
        self.root.title('Guess Nummber!')
        self.gameHelp = '这是1个0 - 1000的数，你要在10次内猜中他！'
        self.gameMsg = '剩余机会: {}    猜测数字：'
        self.tryCount = 10
        self.destNum = randint(1, 1000)
        print(self.destNum)
        self.root.geometry('300x300')
        self.lbGameHelp = Label(self.root, text = self.gameHelp)
        self.lbGameHelp.place(x = 5, y =5)
        self.lbGameMsg = Label(self.root, text = self.gameMsg.format(self.tryCount))
        self.lbGameMsg.place(x = 5, y = 30)
        self.inGuessNum = Entry(self.root)
        self.inGuessNum.place(x = 150, y = 30, width = 50, height = 25)
        self.btnGuess = Button(self.root, text = '猜测', command = self.getGuessNum)
        self.btnGuess.place(x = 210, y = 30, width = 50, height = 25)
        self.txtHistory = Text(self.root)
        self.txtHistory.place( x = 5, y = 60, relwidth = 0.96, relheight = 0.77)
        
        self.txtHistory.insert(END, 'Game start!')
        self.root.mainloop()

    def win(self):
        messagebox.showinfo(title = 'Hi', message = 'flag_you_get_success!')  


    def lose(self):
        messagebox.showinfo(title = 'Hi', message = 'you can try again!')
        self.gameRstart()


    def getGuessNum(self):
        guess_num = int(self.inGuessNum.get())
        self.tryCount -= 1
        msg = '\n还有{}次机会，你猜测的数：{}'.format(self.tryCount, guess_num)
        if guess_num > self.destNum:
            msg += ' 偏大了!'
        elif guess_num < self.destNum:
            msg += ' 偏小了!'
        else:
            msg += '中了!'
            self.win()
            self.root.destroy()
            return
        if self.tryCount == 0:
            self.lose()
            return
        self.txtHistory.insert(END, msg)

        
    def gameRstart(self):
        self.tryCount = 10
        self.destNum = randint(1, 1000)
        self.txtHistory.delete(1.0, END)
        self.txtHistory.insert(END, 'Game Retry!')


if __name__ == '__main__':
    gn = cGuessNum()

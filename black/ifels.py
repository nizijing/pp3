#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-06-30 11:54:50
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################

def work():
    print('Oh,no...我要开始工作了。')

def play():
    print("Dota鱼塘局，快来五连坐...")

def drink():
    print("没有撤退可言，不醉不归！")

def old_demo(choice):
    if choice == 'work':
        work()
    elif choice == 'play':
        play()
    elif choice == 'drink':
        drink()
    else:
        print("你玩的太溜,我的字典里没有...")

def new_demo(user_choice):
    choices = {'work': work, 'play': play, 'drink': drink}
    if user_choice not in choices:
        print("你玩的太溜,我的字典里没有...")
        return

    choices.get(user_choice)()

old_demo('dance')
new_demo('drink')
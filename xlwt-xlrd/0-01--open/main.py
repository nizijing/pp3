#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#####################################################
# Created : 2020-03-23 08:43:56
# Author : zijing (nizj@pukkasoft.cn)
# -----
# Last Modified : 2020-03-23 08:43:56
# Modified By : zijing (nizj@pukkasoft.cn>)
# -----
# HISTORY:
# Date      	By	Comments
#####################################################
import xlrd

def try_open_excel(filepath):
    try:
        wbk = xlrd.open_workbook(filepath)
        print('open excel success')
        return wbk
    except Exception as err:
        print(str(err))
        exit

def main():
   filepath = 'xlwt-xlrd/0-01--open/test.xlsx'
   wbk = try_open_excel(filepath)

if __name__ == '__main__':
   main()

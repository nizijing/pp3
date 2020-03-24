#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#####################################################
# Created : 2020-03-23 20:31:09
# Author : zijing (zijing412@163.com)
#####################################################
import xlrd

def show_data_messages(sheet_data):
    for nrow in range(0, sheet_data.nrows):
        for ncol in range(0, sheet_data.ncols):
            print(sheet_data.cell(nrow, ncol).value, end=', ')
        print()
    print('row: {}; col: {}'.format(sheet_data.nrows, sheet_data.ncols))


def main():
    filepath = 'xlwt-xlrd/0-01--open/test.xlsx'
    wbk = xlrd.open_workbook(filepath)
    sheet_data = wbk.sheets()[0]
    #sheet_data = wbk.sheet_by_name(sheet_name)
    show_data_messages(sheet_data)


if __name__ == '__main__':
    main()

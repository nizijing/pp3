#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#####################################################
# Created : 2019-12-09 18:29:12
# Author : zijing (nizj@pukkasoft.cn)
# -----
# Last Modified : 2019-12-09 18:29:12
# Modified By : zijing (nizj@pukkasoft.cn>)
# -----
# HISTORY:
# Date      	By	Comments
#####################################################
import sys
DEBUG = True

def main():
   if DEBUG: print(sys._getframe().f_code.co_name)

if __name__ == '__main__':
   main()

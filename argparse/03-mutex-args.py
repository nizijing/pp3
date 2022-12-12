import math
import argparse


def parse_args():
    parse = argparse.ArgumentParser(description='Calculate cylinder volume')
    group = parse.add_mutually_exclusive_group()  # 1、在参数对象中添加互斥组
    group.add_argument('-b', '--brief', action='store_true', help='print brief message')  # 2、在互斥组中添加参数（store_true默认当命令行未输入参数则为False，否则为True）
    group.add_argument('-v', '--verbose', action='store_true', help='print verbose message')
    args = parse.parse_args()
    return args


def cal_vol(radius, height):
    vol = math.pi * pow(radius, 2) * height
    return vol


if __name__ == '__main__':
    args = parse_args()
    if args.brief:
        print('brief message')
    elif args.verbose:
        print('comp message')
    else:
        print('hello?')


    print('run main.py -b -v')
import math
import argparse


def parse_args():
    parse = argparse.ArgumentParser(description='Calculate cylinder volume')
    parse.add_argument('-n', '--num', type=int, nargs='+', metavar='', required=True, help='a string of nums')
    args = parse.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    print(args.num)


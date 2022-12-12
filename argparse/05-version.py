import argparse


def parse_args():
    parse = argparse.ArgumentParser(description='version')
    parse.add_argument('-v', '--version', action = 'store_true', help='version')
    args = parse.parse_args()
    return args


def single_input(single_input):
    return single_input


if __name__ == '__main__':
    args = parse_args()
    if args.version:
        print('version 1')


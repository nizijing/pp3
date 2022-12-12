import argparse


def parse_args():
    parse = argparse.ArgumentParser(description='single input')
    parse.add_argument('single_input')
    args = parse.parse_args()
    return args


def single_input(single_input):
    return single_input


if __name__ == '__main__':
    args = parse_args()
    print(single_input(args.single_input))

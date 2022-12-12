import argparse

def minus_one(x):
    print(int(x) - 1)

def time(x, y):
    print(int(x) * int(y))

def main():
    parser = argparse.ArgumentParser(description='Foo Bar')

    subparsers = parser.add_subparsers(dest='command', help='Commands to run', required=True)

    parser_minus_one = subparsers.add_parser('minusone')
    parser_minus_one.add_argument('x', help='X')
    parser_minus_one.set_defaults(func=minus_one)

    parser_time = subparsers.add_parser('time', help='X times Y')
    parser_time.add_argument('x', help='X')
    parser_time.add_argument('y', help='Y')
    parser_time.set_defaults(func=time)

    args = parser.parse_args()

    args_ = vars(args).copy()
    args_.pop('command', None)
    args_.pop('func', None)
    args.func(**args_)

if __name__ == '__main__':
    main()
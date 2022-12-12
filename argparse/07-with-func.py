import argparse

def foo(args):
    print('foo {}'.format(args.x))

def bar(args):
    print('bar {}'.format(args.x))

def main():
    parser = argparse.ArgumentParser(description='Foo Bar')

    subparsers = parser.add_subparsers(dest='command', help='Commands to run', required=True)

    parser_foo = subparsers.add_parser('foo')
    parser_foo.add_argument('x', help='X')
    parser_foo.set_defaults(func=foo)

    parser_bar = subparsers.add_parser('bar')
    parser_bar.add_argument('x', help='X')
    parser_bar.set_defaults(func=bar)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
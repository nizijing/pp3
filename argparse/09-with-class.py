import argparse

class Test:
    def __init__(self) -> None:
        pass

    def foo(self, args):
        print("foo")

    def bar(self, args):
        print("bar {}".format(args.context))

def main():
    test = Test()

    parser = argparse.ArgumentParser(description='Foo Bar')
    subparsers = parser.add_subparsers(dest='command', help='Commands to run', required=True)

    foo = subparsers.add_parser('foo', help='foo some Foos')
    foo.set_defaults(func=test.foo)

    bar = subparsers.add_parser('bar', help='bar some Bars')
    bar.add_argument('context', help='context for bar')
    bar.set_defaults(func=test.bar)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
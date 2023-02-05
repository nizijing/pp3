def yield_way(data):
    for i in data:
        print("yield:", i)
        if i % 2 == 0:
            yield i


def common_way(data):
    ret = []
    for i in data:
        print("common:", i)
        if i % 2 == 0:
            ret.append(i)
    return ret


def main(data):
    for it in common_way(data):
        print(it)
    print('-----------')
    for it in yield_way(data):
        print(it)


if __name__ == '__main__':
    data = range(1, 10)
    main(data)
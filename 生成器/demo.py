def yield_way(data):
    for odd in data:
        if odd % 2 == 0:
            yield odd


def common_way(data):
    return [odd for odd in data if odd % 2 == 0]


def main(data):
    for it in common_way(data):
        print(it)
    print('-----------')
    for it in yield_way(data):
        print(it)


if __name__ == '__main__':
    data = range(1, 10)
    main(data)
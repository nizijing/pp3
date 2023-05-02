#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   51-for.py
@Time    :   2023/05/02 22:08:23
@Author  :   zijing
@Version :   1.0
@Site    :   https://none
@Desc    :   None
'''

'''
如何定义一个可以被for循环使用的类
1. 对象要有__iter__ 或 __next__ 迭代器方法
2. 被迭代的序列对象是否具有 __getitem__ 或 __len__
'''

from datetime import timedelta, date


class Fibonacci:
    """
    F0 = 0
    F1 = 1
    Fn = Fn-1 + Fn -2 (n>=2)
    """
    def __init__(self, n):
        self.previous = 0
        self.current = 1
        self._count = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self._count > self.n:
            raise StopIteration
        self._count += 1
        return_value = self.previous
        self.previous, self.current = self.current, self.previous + self.current
        return return_value


class DateRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self._current_date = start

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_date >= self.end:
                raise StopIteration

        return_value = self._current_date
        self._current_date += timedelta(days=1)
        return return_value


def fib(n):
    prev, current = 0, 1
    for _ in range(n + 1):
        yield prev
        prev, current = current, prev + current


print("class fib")
for n in Fibonacci(5):
    print(n, end=" ")

print("\nfunction fib")
for n in fib(5):
    print(n, end=" ")


print("\nDateReange")
for date_ in DateRange(date(2023, 2, 26), date(2023, 3, 3)):
    print(date_, end=" ")

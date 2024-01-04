'''迭代器 (Iterator) 模式在Python中已经内建并广泛应用, 它提供了一种顺序访问聚合对象 (例如容器或集合) 中的元素的机制, 而无需暴露其底层表示。
在Python中, 我们可以通过实现__iter__()方法和__next__()方法来创建一个自定义迭代器。'''

class MyCustomList:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return MyListIterator(self)

class MyListIterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = 0

    def __next__(self):
        if self.index >= len(self.my_list.data):
            raise StopIteration
        else:
            value = self.my_list.data[self.index]
            self.index += 1
            return value

# 客户端代码
data = [1, 2, 3, 4, 5]
my_list = MyCustomList(data)
for item in my_list:
    print(item)

# 输出：
# 1
# 2
# 3
# 4
# 5
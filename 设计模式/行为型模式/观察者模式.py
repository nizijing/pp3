'''
观察者 (Observer) 模式是一种行为设计模式, 它定义了对象之间的一对多依赖关系, 当一个对象的状态发生改变时, 所有依赖于它的对象都会得到通知并自动更新。
在Python中, 我们可以使用内建的collections.abc模块中的Observable抽象基类来实现观察者模式。
不过, 在标准库中并没有直接提供这个抽象基类, 因此通常我们会自定义一个观察者模式的实现。
以下是一个简单的示例
'''

import abc

# 定义抽象主题接口（Subject）
class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register_observer(self, observer):
        pass

    @abc.abstractmethod
    def remove_observer(self, observer):
        pass

    @abc.abstractmethod
    def notify_observers(self, *args, **kwargs):
        pass

# 定义具体主题（Concrete Subject）
class ConcreteSubject(Subject):
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(*args, **kwargs)

# 定义抽象观察者接口（Observer）
class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, *args, **kwargs):
        pass

# 定义具体观察者（Concrete Observer）
class ConcreteObserver(Observer):
    def update(self, new_state):
        print(f"Observer received new state: {new_state}")

# 客户端代码
def client_code():
    subject = ConcreteSubject()
    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()

    subject.register_observer(observer1)
    subject.register_observer(observer2)

    subject.notify_observers("New State")

if __name__ == "__main__":
    client_code()

# 输出：
# Observer received new state: New State
# Observer received new state: New State
    

'''
在这个例子中：

    Subject 是抽象主题类, 定义了注册、移除观察者以及通知观察者的抽象方法。
    ConcreteSubject 是具体主题类, 实现了主题类的方法, 并维护了一个观察者列表。
    Observer 是抽象观察者接口, 定义了当接收到主题状态变化时需要调用的 update() 方法。
    ConcreteObserver 是具体观察者类, 实现了 update() 方法, 用于接收和处理新的状态信息。
    在客户端代码中, 我们创建了一个具体主题实例和两个具体观察者实例, 并将观察者添加到主题中。当主题状态变化时, 调用 notify_observers() 方法通知所有的观察者。

'''
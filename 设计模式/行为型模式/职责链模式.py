from abc import ABC, abstractmethod

# 抽象处理者类
class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass

    def set_successor(self, successor):
        self._successor = successor

    def _pass_to_successor(self, request):
        if self._successor is not None:
            self._successor.handle_request(request)

# 具体处理者类
class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request <= 10:  # 只处理数值小于等于10的请求
            print(f"ConcreteHandler1 handled request: {request}")
        else:
            self._pass_to_successor(request)

class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request > 10 and request <= 20:  # 只处理数值在10到20之间的请求
            print(f"ConcreteHandler2 handled request: {request}")
        else:
            self._pass_to_successor(request)

class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if request > 20:  # 处理数值大于20的请求
            print(f"ConcreteHandler3 handled request: {request}")
        else:
            self._pass_to_successor(request)

# 客户端代码
def client_code():
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()

    # 构建职责链
    handler1.set_successor(handler2)
    handler2.set_successor(handler3)

    # 发送不同请求
    for request in [5, 15, 25]:
        handler1.handle_request(request)

if __name__ == "__main__":
    client_code()

# 输出：
# ConcreteHandler1 handled request: 5
# ConcreteHandler2 handled request: 15
# ConcreteHandler3 handled request: 25
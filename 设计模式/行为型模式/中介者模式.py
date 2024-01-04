from abc import ABC, abstractmethod

# 抽象同事类（Colleague）
class Colleague(ABC):
    def __init__(self, mediator):
        self._mediator = mediator

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive(self, message):
        pass

# 具体同事类
class ConcreteColleagueA(Colleague):
    def send(self, message):
        print(f"ConcreteColleagueA sends: {message}")
        self._mediator.distribute(message, self)

    def receive(self, message):
        print(f"ConcreteColleagueA receives: {message}")

class ConcreteColleagueB(Colleague):
    def send(self, message):
        print(f"ConcreteColleagueB sends: {message}")
        self._mediator.distribute(message, self)

    def receive(self, message):
        print(f"ConcreteColleagueB receives: {message}")

# 中介者类（Mediator）
class Mediator:
    def __init__(self):
        self._colleagues = []

    def register_colleague(self, colleague):
        self._colleagues.append(colleague)

    def distribute(self, message, sender):
        for colleague in self._colleagues:
            if colleague != sender:
                colleague.receive(message)

# 客户端代码
def client_code():
    mediator = Mediator()
    colleague_a = ConcreteColleagueA(mediator)
    colleague_b = ConcreteColleagueB(mediator)

    mediator.register_colleague(colleague_a)
    mediator.register_colleague(colleague_b)

    # 同事A发送消息
    colleague_a.send("Hello from A")

# 运行客户端代码
if __name__ == "__main__":
    client_code()

# 输出：
# ConcreteColleagueA sends: Hello from A
# ConcreteColleagueB receives: Hello from A
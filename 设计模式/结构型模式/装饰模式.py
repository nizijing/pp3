# 原始组件（Component）
class Coffee:
    def __init__(self, description: str):
        self.description = description

    def get_description(self) -> str:
        return self.description

# 装饰器抽象基类（Decorator）
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

# 具体装饰器
class Mocha(CoffeeDecorator):
    def __init__(self, coffee: Coffee):
        super().__init__(coffee)
        self.description = f"{coffee.get_description()}, with Mocha"

class Whip(CoffeeDecorator):
    def __init__(self, coffee: Coffee):
        super().__init__(coffee)
        self.description = f"{coffee.get_description()}, with Whip"

# 客户端代码
simple_coffee = Coffee("Simple Coffee")
print(simple_coffee.get_description())  # 输出：Simple Coffee

fancy_coffee = Mocha(Whip(simple_coffee))
print(fancy_coffee.get_description())  # 输出：Simple Coffee, with Whip, with Mocha
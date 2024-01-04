from abc import ABC, abstractmethod

# 披萨产品
class Pizza:
    def __init__(self):
        self._size = None
        self._cheese = None
        self._toppings = []

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def cheese(self):
        return self._cheese

    @cheese.setter
    def cheese(self, value):
        self._cheese = value

    @property
    def toppings(self):
        return self._toppings

    def add_topping(self, topping):
        self._toppings.append(topping)

    def __str__(self):
        return f"Size: {self.size}, Cheese: {self.cheese}, Toppings: {', '.join(self.toppings)}"

# 披萨建造者抽象类
class PizzaBuilder(ABC):
    @abstractmethod
    def build_size(self, size):
        pass

    @abstractmethod
    def build_cheese(self, cheese):
        pass

    @abstractmethod
    def build_toppings(self, *toppings):
        pass

    @abstractmethod
    def get_pizza(self):
        pass

# 具体的披萨建造者
class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self._pizza = Pizza()

    def build_size(self, size):
        self._pizza.size = size

    def build_cheese(self, cheese):
        self._pizza.cheese = cheese

    def build_toppings(self, *toppings):
        self._pizza.add_topping("Ham")
        self._pizza.add_topping("Pineapple")
        for topping in toppings:
            self._pizza.add_topping(topping)

    def get_pizza(self):
        return self._pizza

# 导演类
class PizzaDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct_pizza(self, size, cheese, *toppings):
        self._builder.build_size(size)
        self._builder.build_cheese(cheese)
        self._builder.build_toppings(*toppings)
        return self._builder.get_pizza()

# 使用建造者模式构建和打印披萨
def main():
    builder = HawaiianPizzaBuilder()
    director = PizzaDirector(builder)

    pizza = director.construct_pizza("Large", "Mozzarella", "Extra Pineapple")
    print(pizza)

if __name__ == "__main__":
    main()


# 在这个例子中：

#     Pizza是产品，定义了所有可能被建造的披萨对象的属性和方法。
#     PizzaBuilder是抽象建造者，定义了创建披萨对象的接口，声明了构建披萨各个部分的方法。
#     HawaiianPizzaBuilder是具体建造者，是PizzaBuilder的子类，实现了构建披萨各个部分的方法，并返回完整的披萨对象。
#     PizzaDirector是导演类，负责协调建造者的各个部分，指导如何具体构建披萨。

# 通过使用建造者模式，我们可以将复杂的构建过程封装在建造者类中，使得客户端只需指定需要的类型和参数，无需关心具体的构建细节。
# 这提高了代码的可读性和可维护性，并且使得添加新的披萨类型或修改构建过程变得更加容易。
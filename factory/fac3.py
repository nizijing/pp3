# -*- coding: utf-8 -*-

# 抽象工厂方法：提供一个接口，无需指定具体的类，就能创建一系列相关的对象

from abc import ABC, abstractmethod
class FruitPizza(ABC): 
    @abstractmethod 
    def prepare(self): pass
class MeatPizza(ABC): 
    @abstractmethod 
    def serve(self): pass
class ApplePizza(FruitPizza): 
    def prepare(self): print("ApplePizza")
class PeachPizza(FruitPizza): 
    def prepare(self): print("PeachPizza")
class PorkPizza(MeatPizza): 
    def serve(self): print("PorkPizza")
class BeefPizza(MeatPizza): 
    def serve(self): print("BeefPizza")

# 抽象工厂
class PizzaFactory(ABC): 
    @abstractmethod 
    def create_meat_pizza(self): pass 
    @abstractmethod 
    def create_fruit_pizza(self): pass
class IndianPizzaFactory(PizzaFactory): 
    def create_meat_pizza(self): return PorkPizza() 
    def create_fruit_pizza(self): return ApplePizza()
class USPizzaFactory(PizzaFactory): 
    def create_meat_pizza(self): return BeefPizza() 
    def create_fruit_pizza(self): return PeachPizza()
class PizzaStore(object): 
    def make_pizza(self): 
        for factory in [IndianPizzaFactory(), USPizzaFactory()]: 
            meat_pizza = factory.create_meat_pizza() 
            fruit_pizza = factory.create_fruit_pizza() 
            meat_pizza.serve() 
            fruit_pizza.prepare()

if __name__ == '__main__': 
    pizza_store = PizzaStore() 
    pizza_store.make_pizza() 
    """ PorkPizza ApplePizza BeefPizza PeachPizza """

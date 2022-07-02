# -*- coding: utf-8 -*-

# the simple example
# 简单工厂：可以在运行时根据客户端传入的参数类型来创建相应的实例

from abc import ABC, abstractmethod
class Animal(ABC): 
    @abstractmethod 
    def say_hi(self): 
        pass
class Dog(Animal): 
    def say_hi(self): 
        print("汪汪汪...")
class Cat(Animal):
    def say_hi(self): 
        print("喵喵喵...")
class Factory(object): 
    def make_sound(self, animal): 
        eval(animal)().say_hi()
if __name__ == '__main__': 
    factory = Factory() 
    factory.make_sound("Dog") 
    factory.make_sound("Cat") 
    """ 汪汪汪... 喵喵喵... """

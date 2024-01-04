from abc import ABC, abstractmethod

# 抽象产品接口（Food）
class Food(ABC):
    @abstractmethod
    def get_name(self):
        pass

# 具体产品（Pizza）
class Pizza(Food):
    def get_name(self):
        return "Pizza"

# 具体产品（Burger）
class Burger(Food):
    def get_name(self):
        return "Burger"

# 抽象产品接口（Drink）
class Drink(ABC):
    @abstractmethod
    def get_name(self):
        pass

# 具体产品（Soda）
class Soda(Drink):
    def get_name(self):
        return "Soda"

# 具体产品（Coffee）
class Coffee(Drink):
    def get_name(self):
        return "Coffee"

# 抽象工厂（FoodFactory）
class FoodFactory(ABC):
    @abstractmethod
    def create_food(self):
        pass

    @abstractmethod
    def create_drink(self):
        pass

# 具体工厂（ItalianFoodFactory）
class ItalianFoodFactory(FoodFactory):
    def create_food(self):
        return Pizza()

    def create_drink(self):
        return Coffee()

# 具体工厂（AmericanFoodFactory）
class AmericanFoodFactory(FoodFactory):
    def create_food(self):
        return Burger()

    def create_drink(self):
        return Soda()

# 使用抽象工厂创建和打印食品和饮料
def main():
    factory = ItalianFoodFactory()
    food = factory.create_food()
    drink = factory.create_drink()
    print(f"Eating {food.get_name()} and drinking {drink.get_name()}.")

    factory = AmericanFoodFactory()
    food = factory.create_food()
    drink = factory.create_drink()
    print(f"Eating {food.get_name()} and drinking {drink.get_name()}.")

if __name__ == "__main__":
    main()


# 在这个例子中：

#     Food和Drink是抽象产品接口，定义了所有可能被创建的食品和饮料对象的接口。
#     Pizza、Burger、Soda和Coffee是具体产品，实现了相应的抽象产品接口，由具体工厂创建的对象。
#     FoodFactory是抽象工厂，定义了创建食品和饮料对象的接口，声明了创建食品和饮料对象的方法。
#     ItalianFoodFactory和AmericanFoodFactory是具体工厂，是FoodFactory的子类，实现了创建食品和饮料对象的方法，决定具体创建哪种类型的产品组合。

# 通过使用抽象工厂模式，我们可以根据需要动态地选择创建何种类型的食品和饮料组合，
# 而无需在代码中硬编码具体的食品和饮料类型。
# 这提高了代码的灵活性和可扩展性，并且使得产品之间的关联和依赖关系更加清晰。
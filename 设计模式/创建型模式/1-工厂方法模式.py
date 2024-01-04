from abc import ABC, abstractmethod

# 抽象产品（Car）
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

# 具体产品（ElectricCar）
class ElectricCar(Car):
    def drive(self):
        return "Driving an electric car."

# 具体产品（GasolineCar）
class GasolineCar(Car):
    def drive(self):
        return "Driving a gasoline car."

# 抽象工厂（CarFactory）
class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

# 具体工厂（ElectricCarFactory）
class ElectricCarFactory(CarFactory):
    def create_car(self):
        return ElectricCar()

# 具体工厂（GasolineCarFactory）
class GasolineCarFactory(CarFactory):
    def create_car(self):
        return GasolineCar()

# 使用工厂方法创建和驾驶汽车
def main():
    factory = ElectricCarFactory()
    car = factory.create_car()
    print(car.drive())

    factory = GasolineCarFactory()
    car = factory.create_car()
    print(car.drive())

if __name__ == "__main__":
    main()

# 在这个例子中：

#     Car是抽象产品，定义了所有可能被创建的汽车对象的接口。
#     ElectricCar和GasolineCar是具体产品，实现了Car接口，由具体工厂创建的对象。
#     CarFactory是抽象工厂，定义了一个创建汽车对象的接口，声明了一个创建汽车对象的方法。
#     ElectricCarFactory和GasolineCarFactory是具体工厂，是CarFactory的子类，实现了创建汽车对象的方法，决定具体创建哪种类型的汽车对象。

# 通过使用工厂方法模式，我们可以根据需要动态地选择创建何种类型的汽车，而无需在代码中硬编码具体的汽车类型。这提高了代码的灵活性和可扩展性。
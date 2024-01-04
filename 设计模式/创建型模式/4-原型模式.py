from abc import ABC, abstractmethod

# 抽象原型
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def clone(self):
        pass

# 具体原型：圆形
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle with radius {self.radius}.")

    def clone(self):
        return Circle(self.radius)

# 具体原型：矩形
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing a rectangle with width {self.width} and height {self.height}.")

    def clone(self):
        return Rectangle(self.width, self.height)

# 使用原型模式克隆和绘制形状
def main():
    circle = Circle(5)
    circle.draw()

    cloned_circle = circle.clone()
    cloned_circle.radius = 10
    cloned_circle.draw()

    rectangle = Rectangle(3, 4)
    rectangle.draw()

    cloned_rectangle = rectangle.clone()
    cloned_rectangle.width = 6
    cloned_rectangle.height = 8
    cloned_rectangle.draw()

if __name__ == "__main__":
    main()


# 在这个例子中：

#     Shape是抽象原型，定义了所有可能被克隆的形状对象的接口，包括绘制方法和克隆方法。
#     Circle和Rectangle是具体原型，实现了Shape接口，并提供了具体的克隆方法来创建新的相同类型的对象。
#     在主函数中，我们创建了原始的形状对象并调用它们的draw方法进行绘制。然后，我们通过调用clone方法创建克隆对象，并修改克隆对象的属性。最后，我们再次调用克隆对象的draw方法来查看修改后的形状。

# 通过使用原型模式，我们可以快速地创建具有相同或相似属性的新对象，而无需每次都执行完整的初始化过程。
# 这在需要大量创建相似对象或者对象初始化成本较高的场景中非常有用。
# 同时，原型模式也使得代码更加灵活，因为我们可以轻松地添加新的形状类型或者修改克隆逻辑。
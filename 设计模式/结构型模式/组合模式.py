from abc import ABC, abstractmethod

# 抽象组件（Component）
class GraphicShape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def add(self, shape):
        pass

    @abstractmethod
    def remove(self, shape):
        pass

# 叶子对象（Leaf）
class Circle(GraphicShape):
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f"Drawing a circle: {self.name}")

    def add(self, shape):  # 叶子节点没有添加行为
        raise NotImplementedError("Cannot add shapes to a leaf node")

    def remove(self, shape):  # 叶子节点没有移除行为
        raise NotImplementedError("Cannot remove shapes from a leaf node")

# 组合对象（Composite）
class GraphicComposite(GraphicShape):
    def __init__(self, name):
        self.name = name
        self.shapes = []

    def draw(self):
        print(f"Drawing composite: {self.name}")
        for shape in self.shapes:
            shape.draw()

    def add(self, shape):
        self.shapes.append(shape)

    def remove(self, shape):
        self.shapes.remove(shape)

# 客户端代码
circle1 = Circle("Circle 1")
circle2 = Circle("Circle 2")

composite = GraphicComposite("Group")
composite.add(circle1)
composite.add(circle2)

circle1.draw()  # 输出：Drawing a circle: Circle 1
circle2.draw()  # 输出：Drawing a circle: Circle 2
composite.draw()  # 输出：Drawing composite: Group
                 #       Drawing a circle: Circle 1
                 #       Drawing a circle: Circle 2
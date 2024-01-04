# 抽象部分
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

class Shape:
    def __init__(self, drawing_api):
        self._drawing_api = drawing_api

    def draw(self):
        pass  # 具体形状会调用DrawingAPI的相关方法绘制图形

# 实现部分
class DrawingAPIV1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"Drawing a circle at ({x}, {y}) with radius {radius} using API V1.")

class DrawingAPIV2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"Drawing a circle at ({x}, {y}) with radius {radius} using API V2.")

# 具体形状
class CircleShape(Shape):
    def __init__(self, drawing_api):
        super().__init__(drawing_api)

    def draw(self):
        self._drawing_api.draw_circle(0, 0, 5)  # 假设圆心在原点，半径为5

# 客户端代码
shape = CircleShape(DrawingAPIV1())  # 使用API V1绘制圆形
shape.draw()

shape = CircleShape(DrawingAPIV2())  # 使用API V2绘制同一个圆形
shape.draw()

# 在这个例子中，Shape是抽象部分，它定义了所有形状共有的接口，并持有对绘图API对象的引用；
# DrawingAPI及其子类是实现部分，提供了不同的绘图实现。
# 客户端可以根据需求选择具体的绘图API版本，并创建相应的形状实例。
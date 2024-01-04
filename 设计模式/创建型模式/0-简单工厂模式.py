class Color:
    def show_color(self):
        pass

class Red(Color):
    def show_color(self):
        print("Showing red color.")

class Green(Color):
    def show_color(self):
        print("Showing green color.")

class Blue(Color):
    def show_color(self):
        print("Showing blue color.")

# 简单工厂类
class ColorFactory:
    @staticmethod
    def create_color(color_type):
        if color_type == "Red":
            return Red()
        elif color_type == "Green":
            return Green()
        elif color_type == "Blue":
            return Blue()
        else:
            raise ValueError("Invalid color type.")

# 使用简单工厂模式创建和显示颜色
def main():
    color_type = input("Enter the color type (Red, Green, or Blue): ")
    color = ColorFactory.create_color(color_type)
    color.show_color()

if __name__ == "__main__":
    main()
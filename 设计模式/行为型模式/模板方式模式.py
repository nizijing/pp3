from abc import ABC, abstractmethod

# 抽象类
class AbstractClass(ABC):
    def template_method(self):
        """模板方法，定义了基本算法框架"""
        self.primitive_operation1()
        self.primitive_operation2()
        self.hook_method()
        self.primitive_operation3()

    @abstractmethod
    def primitive_operation1(self):
        pass

    @abstractmethod
    def primitive_operation2(self):
        pass

    def hook_method(self):
        """钩子方法，默认行为，子类可选择覆盖此方法以改变行为"""
        print("Default hook method")

    def primitive_operation3(self):
        """具体操作方法，不需要子类实现"""
        print("Executing primitive operation 3")

# 具体子类
class ConcreteClass(AbstractClass):
    def primitive_operation1(self):
        print("ConcreteClass implements primitive_operation1")

    def primitive_operation2(self):
        print("ConcreteClass implements primitive_operation2")

    # 可选地，如果需要，也可以重写钩子方法
    def hook_method(self):
        print("ConcreteClass overrides the hook method")

# 客户端代码
def main():
    obj = ConcreteClass()
    obj.template_method()

if __name__ == "__main__":
    main()
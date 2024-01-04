from abc import ABC, abstractmethod

# 抽象元素类（Element）
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# 具体元素类
class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

# 抽象访问者类（Visitor）
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass

# 具体访问者类
class ConcreteVisitor1(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"ConcreteVisitor1 visiting ConcreteElementA")

    def visit_concrete_element_b(self, element):
        print(f"ConcreteVisitor1 visiting ConcreteElementB")

class ConcreteVisitor2(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"ConcreteVisitor2 visiting ConcreteElementA")

    def visit_concrete_element_b(self, element):
        print(f"ConcreteVisitor2 visiting ConcreteElementB")

# 客户端代码
def client_code(elements, visitor):
    for element in elements:
        element.accept(visitor)

if __name__ == "__main__":
    elements = [ConcreteElementA(), ConcreteElementB()]
    visitor1 = ConcreteVisitor1()
    visitor2 = ConcreteVisitor2()

    client_code(elements, visitor1)
    print("\n")
    client_code(elements, visitor2)

# 输出：
# ConcreteVisitor1 visiting ConcreteElementA
# ConcreteVisitor1 visiting ConcreteElementB
#
# ConcreteVisitor2 visiting ConcreteElementA
# ConcreteVisitor2 visiting ConcreteElementB
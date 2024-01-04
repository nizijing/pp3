from abc import ABC, abstractmethod

# 抽象表达式接口
class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# 树叶节点 - 数字表达式
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

# 操作符表达式
class Operation(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @abstractmethod
    def interpret(self, context):
        pass

# 具体操作符子类：加法表达式
class AddOperation(Operation):
    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

# 具体操作符子类：减法表达式
class SubtractOperation(Operation):
    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)

# 上下文环境类，这里我们不需要额外的状态信息，所以简单起见未提供
# 如果需要存储状态变量，例如变量名和值，则可以通过Context类来维护

# 客户端代码
def client_code():
    expression = AddOperation(Number(5), SubtractOperation(Number(3), Number(2)))
    result = expression.interpret(None)
    print(f"Interpreted result: {result}")

if __name__ == "__main__":
    client_code()

# 输出：
# Interpreted result: 6
    
'''
在这个例子中：

    Expression 是抽象表达式接口，所有具体的表达式都继承自这个接口。
    Number 类代表了叶子节点，即原始数值表达式。
    Operation 是抽象操作符表达式基类，它有两个子表达式作为属性，并且实现了抽象方法 interpret()。
    AddOperation 和 SubtractOperation 是具体的操作符表达式子类，它们各自实现了加法和减法运算。
    在客户端代码中，我们创建了一个嵌套的表达式树结构，然后通过调用 interpret() 方法计算出结果。

'''
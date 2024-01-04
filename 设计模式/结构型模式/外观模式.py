# 子系统类
class SubsystemA:
    def operation_a(self):
        print("Subsystem A: Operation A")

class SubsystemB:
    def operation_b(self):
        print("Subsystem B: Operation B")

class SubsystemC:
    def operation_c(self):
        print("Subsystem C: Operation C")

# 外观类（Facade）
class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()
        self.subsystem_c = SubsystemC()

    def perform_complex_task(self):
        # 协调并封装子系统的操作
        self.subsystem_a.operation_a()
        self.subsystem_b.operation_b()
        self.subsystem_c.operation_c()

# 客户端代码
facade = Facade()
facade.perform_complex_task()

# 输出：
# Subsystem A: Operation A
# Subsystem B: Operation B
# Subsystem C: Operation C

# 在这个例子中，SubsystemA, SubsystemB, 和 SubsystemC 是子系统中的不同组件，它们各自提供了一种操作。
# 而 Facade 类则作为外观角色，通过 perform_complex_task 方法对外暴露一个简单的接口，该方法内部调用了所有子系统的相关操作。
# 当客户端需要执行一项复杂的任务时，只需调用外观对象的方法即可，无需关注这项任务内部是如何由各个子系统协作完成的。
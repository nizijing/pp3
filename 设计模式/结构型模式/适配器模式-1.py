class TargetInterface:
    def request(self):
        pass

# 需要被适配的类
class Adaptee:
    def specific_request(self):
        return "Adaptee's functionality"

# 类适配器，通过继承 Adaptee 并实现 TargetInterface
class Adapter(TargetInterface, Adaptee):
    def request(self):
        # 调用 Adaptee 的方法并转换为 TargetInterface 接口所需的行为
        result = self.specific_request()
        return f"Adapter adapted {result}"
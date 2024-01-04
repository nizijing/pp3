class Adaptee:
    def specific_request(self):
        return "Adaptee's functionality"

# 对象适配器，包含一个 Adaptee 实例
class Adapter(TargetInterface):
    def __init__(self, adaptee_obj):
        self._adaptee = adaptee_obj

    def request(self):
        # 调用 Adaptee 的方法并转换为 TargetInterface 接口所需的行为
        result = self._adaptee.specific_request()
        return f"Adapter adapted {result}"
    
# 在这个例子中，Coffee是原始组件，而Mocha和Whip是装饰器，它们分别给咖啡增加了摩卡和奶油的功能。
# 客户端可以根据需要动态地将这些装饰器添加到咖啡上，从而在不修改原有类的情况下增强了其功能。
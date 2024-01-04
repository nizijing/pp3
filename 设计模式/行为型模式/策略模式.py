'''
    策略接口 (Strategy Interface) : 定义所有支持的算法的公共接口, 通常是一个抽象方法, 允许执行一个特定的操作。

    具体策略类 (Concrete Strategy Classes) : 实现了策略接口, 每个类代表一种具体的算法或行为策略。当需要改变算法的行为时, 可以选择不同的具体策略类来实现。

    上下文 (Context) : 持有一个对策略对象的引用, 并负责调用这个策略对象的业务方法。上下文并不关心具体的策略如何实现, 只需知道策略接口即可。

    客户端 (Client) : 创建具体的策略对象并将其设置到上下文中, 根据需求选择不同的策略来改变上下文的行为。
'''

# 策略接口
class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

# 具体策略类
class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using cash.")

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid {amount} using credit card: {self.card_number}")

# 上下文
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, total_amount):
        print(f"Checking out with total amount: {total_amount}")
        self.payment_strategy.pay(total_amount)

# 客户端代码
def client_code():
    cart = ShoppingCart(CashPayment())
    cart.checkout(100)
    
    cart.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456"))
    cart.checkout(200)

client_code()

# 输出: 
# Checking out with total amount: 100
# Paid 100 using cash.
#
# Checking out with total amount: 200
# Paid 200 using credit card: 1234-5678-9012-3456

'''
在这个例子中, PaymentStrategy 是策略接口, CashPayment 和 CreditCardPayment 是具体策略类, 它们分别代表了现金支付和信用卡支付两种策略；
ShoppingCart 是上下文, 它在结账时调用所选支付策略的 pay() 方法；
客户端代码展示了如何在运行时改变购物车使用的支付策略并进行支付操作。
'''
'''
    命令接口 (Command Interface) : 定义了执行方法 (如 execute()) ，所有具体命令类都必须实现这个接口。

    具体命令类 (Concrete Command Classes) : 实现了命令接口，它们存储了接收者对象的引用，并且在 execute() 方法中调用接收者的特定方法来执行操作。

    接收者 (Receiver) : 负责执行命令请求的具体操作。任何类都可以作为一个接收者，只要它能够完成相应的业务逻辑。

    调用者/请求者 (Invoker) : 拥有并调用命令对象的组件。通过调用命令对象的 execute() 方法触发请求，而不必了解命令是如何被实现的。

    客户端 (Client) : 创建具体的命令对象，并设置其接收者。随后，将命令对象传递给调用者，由调用者决定何时执行命令。
'''

# 命令接口
class Command:
    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")

# 具体命令类
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# 接收者
class Light:
    def turn_on(self):
        print("The light is turned on.")

    def turn_off(self):
        print("The light is turned off.")

# 调用者/请求者
class RemoteControl:
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def press_button(self):
        for command in self._commands:
            command.execute()

# 客户端
def client_code(remote_control):
    living_room_light = Light()
    living_room_on = LightOnCommand(living_room_light)
    living_room_off = LightOffCommand(living_room_light)

    remote_control.add_command(living_room_on)
    remote_control.add_command(living_room_off)

    remote_control.press_button()

remote = RemoteControl()
client_code(remote)

# 输出: 
# The light is turned on.
# The light is turned off.
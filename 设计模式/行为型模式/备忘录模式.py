class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state
        print(f"State changed to: {state}")

    def get_state(self):
        return self._state

    def create_memento(self):
        """创建一个备忘录对象"""
        return Memento(self._state)

    def restore_from_memento(self, memento):
        """从备忘录恢复状态"""
        self.set_state(memento.get_saved_state())

class Memento:
    def __init__(self, saved_state):
        self._saved_state = saved_state

    def get_saved_state(self):
        return self._saved_state

# 客户端代码
def client_code():
    originator = Originator()
    originator.set_state("State 1")

    # 创建一个备忘录以保存当前状态
    memento = originator.create_memento()

    originator.set_state("State 2")
    print("Current state:", originator.get_state())

    # 恢复之前保存的状态
    originator.restore_from_memento(memento)
    print("Restored state:", originator.get_state())

if __name__ == "__main__":
    client_code()

# 输出：
# State changed to: State 1
# State changed to: State 2
# Current state: State 2
# Restored state: State 1
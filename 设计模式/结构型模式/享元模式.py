# 享元接口
class Character:
    def __init__(self, char):
        self._char = char

    @property
    def char(self):
        return self._char

    def display(self, position):
        print(f"Displaying character: {self._char} at position: {position}")

# 具体享元类
class CharacterFlyweight(Character):
    _cache = {}

    @classmethod
    def get_instance(cls, char):
        if char not in cls._cache:
            cls._cache[char] = cls(char)
        return cls._cache[char]

# 客户端代码
def display_text(text, start_pos=0):
    for index, char in enumerate(text):
        flyweight_char = CharacterFlyweight.get_instance(char)
        flyweight_char.display(start_pos + index)

text = "Hello, World!"
display_text(text) 

# 输出：
# Displaying character: H at position: 0
# Displaying character: e at position: 1
# ...

'''在这个例子中，Character 是享元接口，而 CharacterFlyweight 是具体享元类，它利用类级别的缓存 _cache 来存储已经创建过的字符对象。
当客户端请求显示文本时，通过 get_instance 方法获取每个字符对应的享元对象，如果对象已经存在则直接返回，避免了重复创建。
display 方法中的 position 参数就是这里的外部状态，它随客户端的上下文变化而变化。'''
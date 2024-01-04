class SingletonConfig:
    _instance = None

    @staticmethod
    def get_instance():
        if SingletonConfig._instance is None:
            SingletonConfig._instance = SingletonConfig()
        return SingletonConfig._instance

    def __init__(self):
        if SingletonConfig._instance is not None:
            raise Exception("This is a singleton class. Use 'get_instance()' method to get the single instance.")
        else:
            self.config_data = {}

    def set_config(self, key, value):
        self.config_data[key] = value

    def get_config(self, key):
        return self.config_data.get(key)

# 使用单例模式获取和设置配置信息
def main():
    config1 = SingletonConfig.get_instance()
    config1.set_config("database_url", "localhost:5432")

    config2 = SingletonConfig.get_instance()
    print(config2.get_config("database_url"))  # 输出：localhost:5432

if __name__ == "__main__":
    main()

# 在这个例子中：

#     SingletonConfig是单例类，通过定义一个类变量_instance来存储唯一的实例，并提供一个静态方法get_instance()来获取这个实例。
#     在__init__方法中，我们检查是否已经存在实例。如果已经存在（即_instance不为None），则抛出异常，防止创建多个实例。否则，初始化新的实例并保存在_instance中。
#     我们还定义了set_config和get_config方法来操作配置数据。

# 通过使用单例模式，我们可以确保在整个应用程序中只存在一个配置对象，从而避免了由于多个配置对象导致的数据不一致问题。
# 同时，由于单例对象是在需要时才创建的，所以也实现了延迟初始化，提高了资源利用率。
# 定义原始 Image 类，代表需要加载的真实图像资源
class Image:
    def __init__(self, filename):
        self.filename = filename
        self.loaded = False

    def load_from_disk_or_network(self):
        print(f"Loading image from disk/network: {self.filename}")
        # 实际加载图片的操作（这里仅模拟）
        self.loaded = True

    def display(self):
        if not self.loaded:
            self.load_from_disk_or_network()
        print(f"Displaying image: {self.filename}")


# 创建代理类 CachedImageProxy，它同样实现了 Image 接口
class CachedImageProxy(Image):
    def __init__(self, filename):
        super().__init__(filename)
        self.cache = {}

    def load_from_disk_or_network(self):
        if self.filename not in self.cache:
            super().load_from_disk_or_network()
            self.cache[self.filename] = "loaded image data"
        else:
            print("Using cached image")

    def display(self):
        if self.filename not in self.cache:
            super().display()
        else:
            print(f"Displaying cached image: {self.filename}")

# 使用代理类进行操作
image_proxy = CachedImageProxy("image.jpg")
image_proxy.display()  # 第一次调用时加载图像
image_proxy.display()  # 第二次调用时使用缓存

# 在这个例子中，当客户端通过CachedImageProxy访问图像时，代理会检查是否有缓存。
# 如果有缓存，则直接使用缓存中的数据，否则才真正去加载图像并将其添加到缓存中。
# 这样就实现了对原始Image对象访问的一种间接控制，从而优化了性能。
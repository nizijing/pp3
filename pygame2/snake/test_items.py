import random
import pygame

# 全局变量定义
CELL_SIZE = 20                      # 小格子大小
CELL_X = 20
CELL_Y = 16
WINDOW_WIDTH = CELL_X * CELL_SIZE
WINDOW_HEIGH = CELL_Y * CELL_SIZE
SCREEN_RECT = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGH)       # 游戏窗口矩形区域

BACKGROUND_COLOR = (0, 0, 0)              # 主窗口背景颜色
SCORE_TEXT_COLOR = (0, 0, 0)              # 分数文字颜色
TIP_TEXT_COLOR = (0, 0, 255)                   # 提示文字颜色

FOOD_UPDATE_EVENT = pygame.USEREVENT            # 食物更新事件
SNAKE_UPDATE_EVENT = pygame.USEREVENT + 1       # 贪吃蛇移动事件


class Label(object):
    """文字标签类"""
    def __init__(self, size=48, is_score=True):
        """初始化方法

        :param size: 字体大小
        :param is_score: 是否分数
        """
        self.font = pygame.font.SysFont("simhei", size)  # 黑体字
        self.is_score = is_score

    def draw(self, window, text):
        """在窗口中绘制文本内容

        :param window: 游戏主窗口
        :param text: 要显示的文本内容
        """
        # 1. 使用字体渲染文本内容
        color = SCORE_TEXT_COLOR if self.is_score else TIP_TEXT_COLOR
        text_surface = self.font.render(text, True, color)

        # 获得文本图像的矩形区域
        text_rect = text_surface.get_rect()
        # 获得主窗口的矩形区域
        window_rect = window.get_rect()

        # 设置位置
        if self.is_score:  # 分数文字显示在右下角
            text_rect.bottomright = window_rect.bottomright
        else:  # 其他文字显示在中间
            text_rect.center = window_rect.center

        # 2. 在游戏窗口中绘制渲染结果
        window.blit(text_surface, text_rect)


class Food(object):
    """食物类"""
    def __init__(self):
        self.color = (0, 255, 0)  # 绿色食物
        self.score = 5  # 每颗食物得分 5 分
        self.rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)  # 食物位置

        self.random_rect()  # 设置食物随机位置

    def random_rect(self):
        col = SCREEN_RECT.w / CELL_SIZE - 1  # 屏幕上小格子的列数
        row = SCREEN_RECT.h / CELL_SIZE - 1  # 屏幕上小格子的行数

        x = random.randint(0, col) * CELL_SIZE
        y = random.randint(0, row) * CELL_SIZE

        self.rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        # 食物初始不可见
        self.rect.inflate_ip(-CELL_SIZE, -CELL_SIZE)

        pygame.time.set_timer(FOOD_UPDATE_EVENT, 30000)  # 设置更新食物事件

    def draw(self, window):

        # # 判断宽度是否达到小格子宽度
        if self.rect.w < CELL_SIZE:
            self.rect.inflate_ip(2, 2)  # 向四周各自放大 1 个像素

        pygame.draw.ellipse(window, self.color, self.rect)


class Snake(object):
    """贪吃蛇类"""
    def __init__(self):
        self.dir = pygame.K_RIGHT  # 初始向右运动
        self.score = 0  # 初始得分
        self.time_interval = 250 # 运动间隔时间
        self.color = (255, 144, 255)  # 身体颜色-紫粉

        self.body_list = []  # 身体列表

        self.reset_snake()

    def reset_snake(self):
        """重置蛇属性"""
        self.dir = pygame.K_RIGHT
        self.score = 0
        self.time_interval = 250

        self.body_list.clear()  # 清空身体列表

        for i in range(2):  # 添加一节身体
            self.add_node()

    def add_node(self):
        """在蛇的运动方向上，增加一节身体"""
        # 1. 判断是否有身体
        if self.body_list:
            head = self.body_list[0].copy()
        else:
            head = pygame.Rect(-CELL_SIZE, 0, CELL_SIZE, CELL_SIZE)

        # 2. 根据运动方向，调整 head 的位置
        if self.dir == pygame.K_RIGHT:
            head.x += CELL_SIZE
        elif self.dir == pygame.K_LEFT:
            head.x -= CELL_SIZE
        elif self.dir == pygame.K_UP:
            head.y -= CELL_SIZE
        elif self.dir == pygame.K_DOWN:
            head.y += CELL_SIZE

        # 3. 将蛇头插入到身体列表第 0 项
        self.body_list.insert(0, head)

        # 4. 设置贪吃蛇移动定时器
        pygame.time.set_timer(SNAKE_UPDATE_EVENT, self.time_interval)

    def draw(self, window):
        # 遍历绘制每一节身体
        for idx, rect in enumerate(self.body_list):
            pygame.draw.rect(window,
                             self.color,
                             rect.inflate(-2, -2),  # 缩小矩形区域
                             idx == 0)              # 蛇头绘制边框不填充

    def update(self):
        """移动贪吃蛇的整个身体

        一旦发现贪吃蛇移动后会死亡，则恢复整个身体数据

        :return: 移动成功返回 True，贪吃蛇死亡表示不能移动，返回 False
        """
        # 1. 备份身体列表
        body_list_copy = self.body_list.copy()

        # 2. 移动身体
        self.add_node()         # 沿着运动方向在蛇头位置增加一节身体
        self.body_list.pop()    # 删除蛇尾

        # 3. 判断是否死亡，如果是，恢复备份的身体
        if self.is_dead():
            self.body_list = body_list_copy

            return False

        return True

    def change_dir(self, to_dir):
        """改变贪吃蛇的运动方向

        :param to_dir: 要变化的方向
        """
        hor_dirs = (pygame.K_RIGHT, pygame.K_LEFT)      # 水平方向
        ver_dirs = (pygame.K_UP, pygame.K_DOWN)         # 垂直方向

        # 判断当前运动方向及要修改的方向
        if ((self.dir in hor_dirs and to_dir not in hor_dirs) or
                (self.dir in ver_dirs and to_dir not in ver_dirs)):

            self.dir = to_dir

    def has_eat(self, food):
        """判断蛇头是否与食物相遇 - 吃到食物

        :param food: 食物对象
        :return: 是否吃到食物
        """

        if self.body_list[0].contains(food.rect):
            self.score += food.score    # 增加分数

            # 修改运动时间间隔
            if self.time_interval > 100:
                self.time_interval -= 50

            self.add_node()             # 增加一节身体

            return True

        return False

    def is_dead(self):
        """判断贪吃蛇是否死亡

        :return: 死亡返回 True，否则返回 False
        """
        # 1. 记录蛇头的矩形区域
        head = self.body_list[0]

        # 2. 判断蛇头是否移出屏幕
        if not SCREEN_RECT.contains(head):
            return True

        # 3. 判断是否与身体其他部分重叠
        for body in self.body_list[1:]:
            if head.contains(body):
                return True

        return False

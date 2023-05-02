import random
import pygame

# 全局变量定义
CELL_SIZE = 20                      # 小格子大小
CELL_X = 20
CELL_Y = 16
WINDOW_WIDTH = CELL_X * CELL_SIZE
WINDOW_HEIGH = CELL_Y * CELL_SIZE
SCREEN_RECT = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGH)       # 游戏窗口矩形区域

FOOD_UPDATE_EVENT = pygame.USEREVENT            # 食物更新事件

class Food(object):
    """食物类"""
    def __init__(self):
        self.color = (0, 255, 0)  # 绿色食物
        self.score = 5  # 每颗食物得分 5 分
        self.rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)  # 食物位置

        self.random_rect()  # 设置食物随机位置

    def random_rect(self):
        x = random.randint(0, CELL_X) * CELL_SIZE
        y = random.randint(0, CELL_Y) * CELL_SIZE

        self.rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

        # pygame.time.set_timer(FOOD_UPDATE_EVENT, 30000)  # 每30s更新一次食物位置

    def draw(self, window):

        # # 判断宽度是否达到小格子宽度
        if self.rect.w < CELL_SIZE:
            self.rect.inflate_ip(2, 2)  # 向四周各自放大 1 个像素

        pygame.draw.ellipse(window, self.color, self.rect)
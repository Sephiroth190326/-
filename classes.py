import pygame
import random
import fb


class GameSprite1(pygame.sprite.Sprite):
    """定义一个球类"""
    def __init__(self, image_name, up_speed=10, down_speed=5):
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()  # 获取加载图像的尺寸
        self.up_speed = up_speed
        self.down_speed = down_speed


class Ball(GameSprite1):
    def __init__(self):  # 调用父类方法，创建精灵，同时指定图像
        super().__init__(".\\images\\球1.png")
        self.dead = False
        # 指定位置
        self.rect.x = 200
        self.rect.y = 350
        self.radius = self.rect.width / 2

    def update(self):  # 调用父类方法，保持垂直方向的飞行 判断是否飞出屏幕，如果是，需要从组中移除
        if fb.settings.jump_active:
            # 小球跳跃
            self.up_speed -= 1  # 速度递减，上升越来越慢
            self.rect.y -= self.up_speed  # 球Y轴坐标减小，球上升
        else:
            # 球坠落
            self.down_speed += 0.2  # 重力递增，下降越来越快
            self.rect.y += self.down_speed  # 球Y轴坐标增加，球下降


class GameSprite2(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):  # 调用父类的初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()  # 获取加载图像的尺寸
        self.speed = speed  # 定义速度，初始值为1

    def update(self):  # 在屏幕的水平方向上移动
        self.rect.x -= self.speed


class Enemy(GameSprite2):
    def __init__(self):  # 调用父类方法，创建障碍物，同时指定图像
        super().__init__(".\\images\\球2.png")
        # 指定障碍物的初始速度
        if fb.settings.score <= 100:
            self.speed = random.randint(3, 5)
        elif fb.settings.score <= 200:
            self.speed = random.randint(4, 7)
        else:
            self.speed = random.randint(6, 10)
        # 指定障碍物的初始随机位置
        self.rect.x = 800
        self.rect.y = random.randint(20, 670)
        self.radius = self.rect.width / 2

    def update(self):  # 调用父类方法，保持垂直方向的飞行 判断是否离开屏幕，如果是，需要从组中移除
        super().update()
        if self.rect.x < -20:
            self.kill()  # kill方法可以将障碍物从所有组中移除
            fb.settings.score += 1

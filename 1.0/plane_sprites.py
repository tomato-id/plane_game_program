import pygame
import random

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 发射子弹定时器
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.rect.y = -42


class Background(GameSprite):
    """背景精灵"""
    def __init__(self, is_alt=False):
        # 调用父类方法
        super().__init__("../images/background.png")
        # 判断是否是交替图像,并设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类方法实现
        super().update()
        # 判断是否移出屏幕，并更新位置
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        # 调用父类
        super().__init__("../images/enemy1.png")
        # 敌机速度
        self.speed = random.randint(1, 3)

        # 敌机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类
        super().update()
        # 敌机飞出并删除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
            self.__del__()

    def __del__(self):
        # print("敌机删除")
        pass


class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        super().__init__("../images/me1.png", speed=0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.height - 100

        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 水平移动
        self.rect.x += self.speed
        if self.rect.left < -3:
            self.rect.left = -3
        elif self.rect.right > SCREEN_RECT.right+3:
            self.rect.right = SCREEN_RECT.right+3

    def fire(self):
        # 创建子弹精灵
        bullet = Bullet()
        # 设置精灵的位置
        bullet.rect.bottom = self.rect.y - 10
        bullet.rect.centerx = self.rect.centerx
        # 降精灵添加到精灵组
        self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("../images/bullet1.png", speed=-2)

    def update(self):
        # 调用父类,垂直飞行
        super().update()
        # 是否飞出屏幕
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass

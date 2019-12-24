import pygame
import random
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""
    def __init__(self):
        print("游戏初始化")
        # 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法,精灵和精灵组的创建
        self.__create_sprite()
        # 设置定时器事件-创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 150)

    def __create_sprite(self):
        # 创建背景精灵和组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy0_group = pygame.sprite.Group()
        self.enemy1_group = pygame.sprite.Group()
        self.enemy2_group = pygame.sprite.Group()

        # 创建英雄精灵和组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print('游戏开始')

        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprite()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        """事件监听"""
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵

                enemy_types = ["../images/enemy1.png",
                               "../images/enemy2.png",
                               "../images/enemy3_n1.png"]
                num = random.randint(1, 100)
                hp = 1
                if num <= 9:
                    speed = 1
                    hp = 10
                    enemy2 = Enemy(enemy_types[2], speed, hp)
                    self.enemy2_group.add(enemy2)
                elif 9 < num <= 25:
                    speed = random.randint(1, 2)
                    hp = 4
                    enemy1 = Enemy(enemy_types[1], speed, hp)
                    self.enemy1_group.add(enemy1)
                else:
                    speed = random.randint(1, 3)
                    # speed = 8
                    enemy0 = Enemy(enemy_types[0], speed, hp)
                    self.enemy0_group.add(enemy0)

            elif event.type == HERO_FIRE_EVENT:
                # 发射子弹
                self.hero.fire()

        # 使用键盘提供的方法获取键盘按键- 按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 4
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -4
        else:
            self.hero.speed = 0

    def __check_collide(self):
        """碰撞检测"""
        # 子弹摧毁敌机
        for x in [self.enemy0_group, self.enemy1_group, self.enemy2_group]:
            shot_enemy = pygame.sprite.groupcollide(self.hero.bullets, x, True, False)
            if len(shot_enemy) > 0:
                for enemys in shot_enemy:
                    enemy_list = shot_enemy[enemys]
                    for enemy in enemy_list:
                        enemy.HP -= 1

        # 敌机撞毁英雄
        for y in [self.enemy0_group, self.enemy1_group, self.enemy2_group]:
            shot_hero = pygame.sprite.spritecollide(self.hero, y, True)
            if len(shot_hero) > 0:
                self.hero.isboom = True
                # if self.hero.boom_image_index == self.hero.boom_image_length:
                #     self.hero.kill()
                #     # 结束游戏
                #     PlaneGame.__game_over()

    def __update_sprite(self):
        """更新精灵"""
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy0_group.update()
        self.enemy0_group.draw(self.screen)
        self.enemy1_group.update()
        self.enemy1_group.draw(self.screen)
        self.enemy2_group.update()
        self.enemy2_group.draw(self.screen)

        if self.hero.isboom:
            quit_game = self.hero.boom(self.screen)
            if quit_game:
                self.hero.kill()
                PlaneGame.__game_over()
        else:
            self.hero_group.update()
            self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()


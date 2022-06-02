# @Author : dcg

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """飞船类"""

    def __init__(self, ai_game):
        """初始化飞船"""
        super().__init__()
        # 获取屏幕对象
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 获取屏幕的rect对象
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ava.bmp')
        self.rect = self.image.get_rect()

        # 将飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # 飞船移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def move(self):
        """根据移动开关调整飞船位置"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        self.rect.x = self.x

    def center_ship(self):
        """将飞船放在屏幕底部中间"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def center_ship(self):
        """让飞船底部居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

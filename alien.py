# @Author : dcg

import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """单个外星人"""

    def __init__(self, ai_game):
        """初始化外星人及位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/yellowbean.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """如果外星人位于屏幕边缘,就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_x_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x

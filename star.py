# @Author : dcg

import pygame

from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, ai_game):
        """初始化修星星及位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/redbean.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


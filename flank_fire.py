# @Author : dcg

import sys
import pygame
from settings import Settings

pygame.init()
settings = Settings()
# 主界面
screen_image = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # 全屏
screen_rect = screen_image.get_rect()  # 获取窗口的矩形区域
screen_image.fill(settings.bg_color)  # 填充背景色

# Ava号飞船
ship_image = pygame.image.load('images/ava.bmp')
ship_image = pygame.transform.rotate(ship_image, -90)  # 图片旋转
ship_rect = ship_image.get_rect()
ship_rect.midleft = screen_rect.midleft  # 将飞船放在屏幕底部中央

# 飞船移动
move_up = False
move_down = False

bullet = pygame.sprite.Group()

while True:
    # 检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 按下键盘
            if event.key == pygame.K_q:  # 按下q键退出
                sys.exit()
            if event.key == pygame.K_DOWN:  # 下移
                move_up = True
            if event.key == pygame.K_UP:  # 上移
                move_down = True
            if event.key == pygame.K_SPACE:  # 发射子弹
                if len(bullet) < settings.bullets_allowed:
                    new_bullet = pygame.sprite.Sprite()
                    new_bullet.rect = pygame.Rect(0, 0, 10, 5)
                    new_bullet.rect.midbottom = ship_rect.midright
                    bullet.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                move_up = False
            if event.key == pygame.K_UP:
                move_down = False

    if move_down and ship_rect.top > 0:
        ship_rect.y -= settings.ship_speed
    if move_up and ship_rect.bottom < screen_rect.bottom:
        ship_rect.y += settings.ship_speed

    ship_sprite = pygame.sprite.Sprite()
    ship_sprite.image = ship_image
    ship_sprite.rect = ship_rect

    # 绘制图像
    screen_image.fill(settings.bg_color)
    screen_image.blit(ship_image, ship_rect)

    # 绘制子弹
    for b in bullet:
        pygame.draw.rect(screen_image, settings.bullet_color, b)
        b.rect.x += settings.bullet_speed
        if b.rect.left >= 1920:
            bullet.remove(b)

    pygame.display.flip()

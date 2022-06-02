# @Author : dcg

import unittest
from ship import Ship
from alien_invasion import AlienInvasion


class TestMove(unittest.TestCase):
    """测试飞船的移动"""

    def test_left_move(self):
        # 飞船左移测试
        ship = Ship(AlienInvasion())
        ship.move_left = True
        ship.move()
        # 飞船坐标小于屏幕底部中心坐标
        self.assertLess(ship.rect.midbottom, ship.screen_rect.midbottom)

    def test_right_move(self):
        # 飞船右移测试
        ship = Ship(AlienInvasion())
        ship.move_right = True
        ship.move()
        # 飞船坐标大于屏幕底部中心坐标
        self.assertGreater(ship.rect.midbottom, ship.screen_rect.midbottom)

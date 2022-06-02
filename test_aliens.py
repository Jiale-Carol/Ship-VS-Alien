# @Author : dcg

import unittest
from alien import Alien
from alien_invasion import AlienInvasion


class TestEdges(unittest.TestCase):
    """测试外星人是否触碰到屏幕边缘"""

    def test_left_edges(self):
        # 当外星人触碰到屏幕左边时返回True
        alien_invasion = AlienInvasion()
        alien = Alien(alien_invasion)
        alien.rect.left = 0
        self.assertEqual(alien.check_edges(), True)

    def test_right_edges(self):
        # 当外星人触碰到屏幕右边时返回True
        alien_invasion = AlienInvasion()
        alien = Alien(alien_invasion)
        alien.rect.right = alien_invasion.screen.get_rect().right
        self.assertEqual(alien.check_edges(), True)

    def test_not_edges(self):
        # 没有触碰时返回False
        alien_main = AlienInvasion()
        alien = Alien(alien_main)
        alien.rect.right = 380
        self.assertEqual(alien.check_edges(), False)

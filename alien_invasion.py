# @Author : dcg

import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:

    def __init__(self):

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:
            #for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        sys.exit()
            #self.screen.fill(self.bg_color)
            #self.ship.blitme()
            #pygame.display.flip()
            self._check_events()
            #self.ship.update()
            #self._update_screen()

    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False

                    # self.ship.rect.x += 1

    def _update_screen(self):

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()




if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

import pygame
from plane_sprites import *


class PlaneGame(object):
    """plane game main program"""

    def __init__(self):
        print("game init...")
        # 1. create game's windows
        self.screen = pygame.display.set_mode((480, 700))
        # 2. create game's clock
        self.clock = pygame.time.Clock()
        # 3. call private methods ,create sprites and their group
        self.__create_sprites()

    def __create_sprites(self):
        pass

    def start_game(self):
        print("start game...")


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()

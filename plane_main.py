import pygame
from plane_sprites import *


class PlaneGame(object):
    """plane game main program"""

    def __init__(self):
        print("game init...")
        # 1. create game's windows
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. create game's clock
        self.clock = pygame.time.Clock()
        # 3. call private methods ,create sprites and their group
        self.__create_sprites()

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

    def start_game(self):
        print("start game...")
        while True:
            # 1. set frequency
            self.clock.tick(FRAME_PER_SEC)
            # 2. event listening
            self.__event_handler()
            # 3. detective crash
            self.__check_collide()
            # 4. update and draw sprites and their group
            self.__update_sprites()
            # 5. update display
            pygame.display.update()

            pass

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("GAME OVER")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()

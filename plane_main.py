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
        # 4. set timer event,create enemy 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 5.set hero fire ,0.5s
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

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
            elif event.type == CREATE_ENEMY_EVENT:
                # print("enemy show up")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #    print("move right...")
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 1. bullet kill enemy
        pygame.sprite.groupcollide(self.hero.bullet, self.enemy_group, True, True)
        # 2. enemy kill hero
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet.update()
        self.hero.bullet.draw(self.screen)

    @staticmethod
    def __game_over():
        print("GAME OVER")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()

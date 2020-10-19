import random
import pygame

# screen size
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# frequency
FRAME_PER_SEC = 60

# create enemy timer
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        # 1.call farther, create enemy and picture
        super().__init__("./images/enemy1.png")

        # 2. enemy random speed 1~3
        self.speed = random.randint(1, 3)

        # 3. enemy random position
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

        pass

    def update(self):
        # 1. call farther,
        super().update()

        # 2. if out of screen ,delete enemy
        if self.rect.y >= SCREEN_RECT.height:
            print("out of screen, delete enemy")
            self.kill()

        pass

    def __del__(self):
        print("enemy die %s" % self.rect)

import random
import pygame

# screen size
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# frequency
FRAME_PER_SEC = 60

# create enemy timer
CREATE_ENEMY_EVENT = pygame.USEREVENT

# fire ire event
HERO_FIRE_EVENT = pygame.USEREVENT + 1


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

    def update(self):
        # 1. call farther,
        super().update()

        # 2. if out of screen ,delete enemy
        if self.rect.y >= SCREEN_RECT.height:
            # print("out of screen, delete enemy")
            self.kill()

    def __del__(self):
        pass
        # print("enemy die %s" % self.rect)


class Hero(GameSprite):
    def __init__(self):
        # 1. call farther, set  image and speed
        super().__init__("./images/me2.png", 0)
        # 2. position
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 3. bullet sprite group
        self.bullet = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # print("Fire... ... ...")
       for i in (0,1,2):
            # 1. create bullet sprite
            bullet = Bullet()
            # 2. position
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3. add to group
            self.bullet.add(bullet)



class Bullet(GameSprite):
    def __init__(self):
        # 1.call farther,image and speed
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 1. call farther
        super().update()
        # 2.if out of screen
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("Bullet gone...")

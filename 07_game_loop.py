import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
hero = pygame.image.load("./images/me2.png")
screen.blit(hero, (150, 500))
pygame.display.update()

i = 0

clock = pygame.time.Clock()

while True:
    clock.tick(1)
    print(i)
    i += 1

pygame.quit()

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
<<<<<<< Updated upstream
=======


>>>>>>> Stashed changes
pygame.display.update()

hero = pygame.image.load("./images/me2.png")
screen.blit(hero, (150, 500))
pygame.display.update()

while True:
    pass

pygame.quit()

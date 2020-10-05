import pygame
from pygame.draw import *
from random import *


def place_mushroom(surface, pos, scale=1.0, angle=0):
    mushroom = pygame.Surface((1000, 1000), pygame.SRCALPHA)
    ellipse(mushroom, WHITE, (400, 200, 200, 600))
    ellipse(mushroom, RED, (200, 100, 600, 200))
    ellipse(mushroom, WHITE, (400, 200, 100, 50))
    ellipse(mushroom, WHITE, (320, 130, 100, 50))
    ellipse(mushroom, WHITE, (600, 150, 100, 50))
    mushroom = pygame.transform.rotozoom(mushroom, angle, scale / 10)
    surface.blit(mushroom, pos)


def place_hedgehog(surface, pos, scale=1.0):
    hedgehog = pygame.Surface((3200, 3600), pygame.SRCALPHA)
    ellipse(hedgehog, PURPULE, (100, 600, 1500, 800))  # body
    ellipse(hedgehog, PURPULE, (1400, 1200, 300, 200))  # front leg
    ellipse(hedgehog, PURPULE, (200, 1200, 300, 200))  # back right leg
    ellipse(hedgehog, PURPULE, (100, 1100, 250, 150))  # back left leg
    ellipse(hedgehog, PURPULE, (1700, 900, 400, 300))  # head
    ellipse(hedgehog, BLACK, (1800, 1000, 100, 50))  # eye
    spine = pygame.Surface((80, 800), pygame.SRCALPHA)
    polygon(spine, LIGHT_BLACK, ((40, 0), (0, 400), (80, 400)))
    polygon(spine, BLACK, ((40, 0), (0, 400), (80, 400)), 10)
    for i in range(100):
        if i == 70:
            ellipse(hedgehog, ORANGE, (200, 500, 400, 400))
            ellipse(hedgehog, RED, (1200, 500, 400, 400))
            place_mushroom(hedgehog, (200, 0), 10, -20)
        turn = randint(-40, 40)
        x = randint(100, 1200)
        y = randint(0, 600)
        hedgehog.blit(pygame.transform.rotate(spine, turn), (x, y))
    hedgehog = pygame.transform.rotozoom(hedgehog, 0, scale/10)
    surface.blit(hedgehog, pos)


SEA_GREEN = (0, 164, 113)
TEAL = (68, 119, 135)
YELLOW = (255, 236, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPULE = (77, 0, 69)
ORANGE = (255, 176, 0)
LIGHT_BLACK = (20, 20, 20)

pygame.init()
FPS = 60
screen = pygame.display.set_mode((600, 700))

# background
sky = pygame.Surface((600, 700))
sky.fill(SEA_GREEN)
ground = pygame.Surface((600, 250))
ground.fill(TEAL)
screen.blit(sky, (0, 0))
screen.blit(ground, (0, 450))

# trees
rect(screen, YELLOW, (0, 0, 45, 520), 0)
rect(screen, YELLOW, (80, 0, 135, 680), 0)
rect(screen, YELLOW, (450, 0, 45, 520), 0)
rect(screen, YELLOW, (560, 0, 30, 580), 0)

# mushrooms in the right bottom corner
mushrooms = [((450, 675), 0.5, 0), ((380, 665), 0.5, 15), ((460, 640), 1, 20), ((390, 630), 1, -10)]
for mushroom in mushrooms:
    place_mushroom(screen, *mushroom)

# hedgehogs with mushrooms
hedgehogs = [((50, 500), 0.5), ((350, 400), 1)]
for hedgehog in hedgehogs:
    place_hedgehog(screen, *hedgehog)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

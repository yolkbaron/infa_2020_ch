import pygame
from pygame.draw import *
from random import *

pygame.init()
FPS = 60
sc = pygame.display.set_mode((600, 700))

#background
sky = pygame.Surface((600, 700))
sky.fill((0, 164, 113))
ground = pygame.Surface((600, 250))
ground.fill((68, 119, 135))
sc.blit(sky, (0, 0))
sc.blit(ground, (0, 450))

#trees
rect(sc, (255, 236, 0), (0, 0, 45, 520), 0)
rect(sc, (255, 236, 0), (80, 0, 135, 680), 0)
rect(sc, (255, 236, 0), (450, 0, 45, 520), 0)
rect(sc, (255, 236, 0), (560, 0, 30, 580), 0)

#fly agaric
mh = pygame.Surface((100, 100), pygame.SRCALPHA)
ellipse(mh, (255, 255, 255), (40, 20, 20, 60))
ellipse(mh, (255, 0, 0), (20, 10, 60, 20))
ellipse(mh, (255, 255, 255), (40, 20, 10, 5))
ellipse(mh, (255, 255, 255), (32, 13, 10, 5))
ellipse(mh, (255, 255, 255), (60, 15, 10, 5))
minimh = pygame.transform.scale(mh, (mh.get_width()//2, mh.get_height()//2))
sc.blit(pygame.transform.rotate(minimh, 0), (450, 675))
sc.blit(pygame.transform.rotate(minimh, 15), (380, 665))
sc.blit(pygame.transform.rotate(mh, 20), (460, 630))
sc.blit(pygame.transform.rotate(mh, -10), (390, 630))

#ej
ej = pygame.Surface((400, 400), pygame.SRCALPHA)
ellipse(ej, (77, 0, 69), (100, 100, 150, 80))
ellipse(ej, (77, 0, 69), (220, 160, 30, 20))
ellipse(ej, (77, 0, 69), (100, 160, 30, 20))
ellipse(ej, (77, 0, 69), (90, 150, 25, 15))
ellipse(ej, (77, 0, 69), (240, 130, 40, 30))
ellipse(ej, (0, 0, 0), (260, 140, 10, 5))
sc.blit(ej, (200, 200))
miniej = pygame.transform.scale(ej, (ej.get_width()//2, ej.get_height()//2))
sc.blit(miniej, (-40, 600))

#igles
ig = pygame.Surface((8, 30), pygame.SRCALPHA)
polygon(ig, (0, 0, 0), ((4, 0), (0, 30), (8, 30)))
for i in range(150):
    if i == 110:
        ellipse(sc, (255, 176, 0), (320, 300, 30, 40))
        ellipse(sc, (255, 0, 0), (400, 290, 30, 40))
        sc.blit(pygame.transform.rotate(mh, -20), (310, 250))
    turn = randint(-40, 40)
    x = randint(300, 420)
    y = randint(280, 340)
    sc.blit(pygame.transform.rotate(ig, turn), (x, y))
for i in range(75):
    if i == 110:
        ellipse(sc, (255, 176, 0), (100, 500, 15, 20))
        ellipse(sc, (255, 0, 0), (400, 290, 15, 20))
        sc.blit(pygame.transform.rotate(mh, -20), (310, 250))
    turn = randint(-40, 40)
    x = randint(300, 420)
    y = randint(280, 340)
    sc.blit(pygame.transform.rotate(ig, turn), (x, y))



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
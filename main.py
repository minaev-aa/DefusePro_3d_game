import pygame
from settings import *
from Player import *
from pygame.draw import *
from map import *
from ray_casting import *

finished = False
player = Player()
pygame.init()

screen = pygame.display.set_mode((width_screen, height_screen))


while not finished:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    player.move()
    #draw()
    pygame.draw.rect(screen, Blue, (0, 0, width_screen, height_screen//2))
    pygame.draw.rect(screen, Yellow, (0, height_screen//2, width_screen, height_screen//2))
    ray_casting(screen, player.pos, player.angle)
    pygame.display.flip()

pygame.quit()
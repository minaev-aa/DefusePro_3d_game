import pygame
from settings import *
from Player import *
from pygame.draw import *
#test
finished = False
player = Player()

pygame.init()

screen = pygame.display.set_mode((width_screen, height_screen))

def draw():
    circle(screen, Green, (int(player.x_player), int(player.y_player)), radius_player)

while not finished:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    player.move()
    draw()


    pygame.display.update()
    screen.fill(Black)

pygame.quit()
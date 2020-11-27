import pygame
from settings import *
from ray_casting import *


class Planning:
    def __init__(self, sc):
        self.sc = sc
        self.textures = {'1': pygame.image.load('Resources/Textures/2tex6x6.png').convert(),
                         '2': pygame.image.load('Resources/Textures/tex6X6.png').convert(),
                         'S': pygame.image.load('Resources/Textures/stars.png').convert()
                         }

    def sky(self, angle):
        sky_offset = -5 * math.degrees(angle) % width_screen
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - width_screen, 0))
        self.sc.blit(self.textures['S'], (sky_offset + width_screen, 0))
        pygame.draw.rect(self.sc, (40, 40, 40), (0, height_screen // 2, width_screen, height_screen // 2))

    def plan(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle, self.textures)

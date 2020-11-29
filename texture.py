import pygame
from settings import *
from ray_casting import *


class Planning:
    '''
    Класс рисования текстур
    '''
    def __init__(self, sc):
        self.sc = sc
        self.textures = {'1': pygame.image.load('Resources/Textures/2tex6x6.png').convert(),
                         '2': pygame.image.load('Resources/Textures/tex6X6.png').convert(),
                         'S': pygame.image.load('Resources/Textures/stars.png').convert()
                         }

    def sky(self, angle):
        '''
        :param angle:
        :return: Рисует стены
        '''
        sky_offset = -5 * math.degrees(angle) % width_screen
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - width_screen, 0))
        self.sc.blit(self.textures['S'], (sky_offset + width_screen, 0))
        pygame.draw.rect(self.sc, Grey, (0, height_screen // 2, width_screen, height_screen // 2))

    def plan(self, player_pos, player_angle):
        '''
        :param player_pos: Координаты игрока
        :param player_angle: Положение угла камеры
        :return: Рисует стены
        '''
        ray_casting(self.sc, player_pos, player_angle, self.textures)
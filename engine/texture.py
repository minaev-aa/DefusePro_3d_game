# from engine.ray_casting import *
import engine.ray_casting
from settings import *


class Planning:
    '''
    Класс рисования текстур
    :param  sc: экран
    :param textures: словарь с загрузкой png картинки текстуры
    '''

    def __init__(self, sc):
        self.sc = sc
        self.textures = {'0': pygame.image.load('Resources/Textures/2tex6x6.png').convert(),
                         '1': pygame.image.load('Resources/Textures/9tex6X6.png').convert(),
                         '2': pygame.image.load('Resources/Textures/8tex6X6.png').convert(),
                         '3': pygame.image.load('Resources/Textures/4tex6x6.png').convert(),
                         '4': pygame.image.load('Resources/Textures/5tex6x6.png').convert(),
                         '5': pygame.image.load('Resources/Textures/7tex6x6.png').convert(),
                         '6': pygame.image.load('Resources/Textures/tex6x6.png').convert(),
                         '7': pygame.image.load('Resources/Textures/10tex6x6.png').convert(),
                         'S': pygame.image.load('Resources/Textures/stars.png').convert(),
                         'o': pygame.image.load('Resources/Textures/3.3tex6x6.png').convert(),
                         'd': pygame.image.load('Resources/Textures/3.3tex6x6.png').convert(),
                         't': pygame.image.load('Resources/Textures/3.3tex6x6.png').convert(),
                         'c': pygame.image.load('Resources/Textures/3.3tex6x6.png').convert(),
                         'p': pygame.image.load('Resources/Textures/3.3tex6x6.png').convert(),
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

    def plan(self, player_pos, player_angle, sprites):
        '''
        :param player_pos: Координаты игрока
        :param player_angle: Положение угла камеры
        :return: Рисует стены и спрайт с самого далёкого до самого ближнего
        '''
        walls = engine.ray_casting.ray_casting(self.sc, player_pos, player_angle, self.textures)
        if not (sprites[2] == 0):
            walls.append(sprites)
        walls = sorted(walls, key=lambda wall: wall[0], reverse=True)  # сортировка по расстоянию
        for wall in walls:
            self.sc.blit(wall[1], wall[2])

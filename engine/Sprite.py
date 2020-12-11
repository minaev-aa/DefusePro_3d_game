import numpy as np
from settings import *

class Sprite:
    def __init__(self, scale, x_pos, y_pos, file, screen, player):
        """

        @param scale:
        @type scale: float
        @param x_pos: координата x спрайта
        @type x_pos: int
        @param y_pos: координата y спрайта
        @type y_pos: int
        @param file: картинка
        @param screen: холт, где спрайт будет рисоваться.
        @type screen: pygame.surface
        @param player: игрок, который смотрит на спрайт
        """
        self.scale = scale
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.surf = pygame.image.load(file)
        self.screen = screen
        self.player = player

    def angle(self):
        '''
        Функция, которая расчитывает угол между игроком и спрайтом.
        :return: угол между игроком и спрайтом.
        '''
        delta_x = self.x_pos - self.player.x_player
        delta_y = self.y_pos - self.player.y_player
        angle_sprite = np.arctan(delta_y / delta_x)
        angle_to_player = -(angle_sprite - self.player.angle)
        if delta_x > 0:
            angle_to_player += np.pi
        angle_to_player %= 2 * np.pi
        return angle_to_player

    def distance_to_player(self):
        '''
        :return: Вычисление расстояния до игрока
        '''
        distance_to_player = ((self.x_pos - self.player.x_player) ** 2 + (self.y_pos - self.player.y_player) ** 2) ** (1 / 2)
        return distance_to_player

    def size(self):
        '''
        Расчитывает размер изображения спрайта на экране
        :return: размер спрайта
        '''
        distance_to_player = self.distance_to_player()
        if distance_to_player == 0:
            distance_to_player = player_angle
        proec_size = int(proec_k / distance_to_player * self.scale * size_sprite)
        if not(distance_to_player > 30):
            proec_size = 0
        return proec_size

    def draw(self):
        '''
        :return: Отрисовка спрайта
        '''
        angle_to_player = self.angle()
        if not (angle_to_player < np.pi / 2 or angle_to_player > 3 / 2 * np.pi):
            guard_surf_new = pygame.transform.scale(self.surf, (int(self.size()), int(self.size())))
            guard_rect = guard_surf_new.get_rect(
                    center=(width_screen // 2 - 4*distance * np.tan(angle_to_player), height_screen // 2))
        else:
            guard_surf_new, guard_rect = (0, 0)
        return guard_surf_new, guard_rect


class Guard(Sprite):
    def __init__(self, scale, x_pos, y_pos, screen, player):
        super().__init__(scale, x_pos, y_pos, 'Resources\\Sprayt\\guard_good.png', screen, player)

    def move(self, x, y):
        self.x_pos = x
        self.y_pos = y
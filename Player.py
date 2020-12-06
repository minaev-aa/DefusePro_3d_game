from settings import *
import pygame
import numpy as np
from ray_casting import mapping
from map import *


class Player:
    '''
    Класс игрока
    player_pos :param Координаты игрока в кортеже
    '''
    def __init__(self, player_pos):
        self.x_player, self.y_player = player_pos
        self.angle = player_angle

    def audio_init(self, audio):
        self.audio = audio

    def sound_of_steps(self):
        """
        Включает звук ходьбы для персонажа.
        :return: звук.
        """
        self.audio.Sound_play(self.audio.steps, steps_duration, self.audio.steps_start_time)
        self.audio.steps_start_time = self.audio.check_sound(steps_duration, self.audio.steps_start_time)

    def sound_of_running(self):
        """
        Включает звук бега для персонажа.
        :return: звук.
        """
        self.audio.Sound_play(self.audio.running, running_duration, self.audio.running_start_time)
        self.audio.running_start_time = self.audio.check_sound(running_duration, self.audio.running_start_time)

    @property
    def pos(self):
        '''
        :return: Позиция игрока
        '''
        return (int(self.x_player), int(self.y_player))

    def move(self):
        '''
        :return: Движение игрока
        '''
        pressed_keys = pygame.key.get_pressed()
        self.is_move = False
        self.Vy = player_speed * np.cos(self.angle)
        self.Vx = player_speed * np.sin(self.angle)
        if pressed_keys[pygame.K_LSHIFT]:
            self.Vy *= 2
            self.Vx *= 2
        if pressed_keys[pygame.K_a]:
            self.is_move = True
            # self.sound_of_steps()
            self.x_player, self.y_player = self.__mover_player__(self.x_player, self.Vx, self.y_player, -1 * self.Vy)
        if pressed_keys[pygame.K_d]:
            self.is_move = True
            # self.sound_of_steps()
            self.x_player, self.y_player = self.__mover_player__(self.x_player, -1 * self.Vx, self.y_player, self.Vy)
        if pressed_keys[pygame.K_s]:
            self.is_move = True
            # self.sound_of_steps()
            self.x_player, self.y_player = self.__mover_player__(self.x_player, -1 * self.Vy, self.y_player,
                                                                 -1 * self.Vx)
        if pressed_keys[pygame.K_w]:
            self.is_move = True
            # self.sound_of_steps()
            self.x_player, self.y_player = self.__mover_player__(self.x_player, self.Vy, self.y_player, self.Vx)

        if pressed_keys[pygame.K_RIGHT]:
            self.angle += player_angle_change_speed
        if pressed_keys[pygame.K_LEFT]:
            self.angle -= player_angle_change_speed

    def is_player_in_colader(self, cord_x, Vx, cord_y, Vy):
        """
        Проверяет, попадет ли игрок в следующем кадре в текстуры.
        :cord_x:  и :cord_y:  Координаты, по которым считается перемещение.
        :Vx: и :Vy: - Скорости по данным коодринатам.
        :return: Возращает скорочти по координатам cord_x и cord_yю
        """
        Vx_m = Frames_for_taching_with_walls * Vx
        Vy_m = Frames_for_taching_with_walls * Vy
        m_x = mapping(cord_x + Vx_m, cord_y)  # Создает кортеж координат.
        m_y = mapping(cord_x, cord_y + Vy_m)  # Создает кортеж координат.
        if m_x in map:
            Vx = 0
        if m_y in map:
            Vy = 0
        return Vx, Vy

    def __mover_player__(self, cord_x, Vx, cord_y, Vy):
        """
        Меняет координаты игрока.
        Проверяет, может ли он идти дальше (проверка на текстутры).
        :cord_x: и :cord_y:  Координаты, по которым считается перемещение.
        :Vx: и :Vy: - Скорости по данным коодринатам.
        :return: Новую коодринату.
        """
        Vx, Vy = self.is_player_in_colader(cord_x, Vx, cord_y, Vy)
        cord_x += Vx
        cord_y += Vy
        return cord_x, cord_y

    def is_player_move(self):
        """
        Проверяет движентся ли игрок.
        :return: True, если игрок движется, иаче False.
        """
        return self.is_move

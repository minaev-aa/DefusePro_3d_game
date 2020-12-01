from settings import *
import pygame
import numpy as np


class Player:
    def __init__(self, dplayer_pos):
        self.x_player, self.y_player = dplayer_pos
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
        return (int(self.x_player), int(self.y_player))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        self.is_move = False
        self.Vy = player_speed * np.cos(self.angle)
        self.Vx = player_speed * np.sin(self.angle)
        if pressed_keys[pygame.K_a]:
            self.is_move = True
            # self.sound_of_steps()
            self.x_player += self.Vx
            self.y_player -= self.Vy
        if pressed_keys[pygame.K_d]:
            self.is_move = True
            # self.sound_of_steps()
            self.x_player -= self.Vx
            self.y_player += self.Vy
        if pressed_keys[pygame.K_s]:
            self.is_move = True
            # self.sound_of_steps()
            self.x_player -= self.Vy
            self.y_player -= self.Vx
        if pressed_keys[pygame.K_w]:
            self.is_move = True
            # self.sound_of_steps()
            self.x_player += self.Vy
            self.y_player += self.Vx

        if pressed_keys[pygame.K_RIGHT]:
            self.angle += player_angle_change_speed
        if pressed_keys[pygame.K_LEFT]:
            self.angle -= player_angle_change_speed

    def is_player_move(self):
        """
        Проверяет движентся ли игрок.
        :return: True, если игрок движется, иаче False.
        """
        if self.is_move:
            return True
        else:
            return False

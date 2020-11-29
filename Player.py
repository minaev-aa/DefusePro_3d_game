from settings import *
import pygame
import numpy as np
from Music_module import Audio_source
import time


class Player:
    def __init__(self):
        self.x_player, self.y_player = player_pos
        self.angle = player_angle

    def audio_init(self, audio):
        self.audio = audio

    def sound_of_steps(self):
        """
        Включает звук ходьбы для персонажа.
        :return: звук.
        """
        # Проверка, на то, что еще не включен звук бега.
        if self.audio.running_start_time + running_duration <= time.time():
            self.audio.Sound_play(self.audio.steps, steps_duration, self.audio.steps_start_time)
            self.audio.steps_start_time = self.audio.check_sound(steps_duration, self.audio.steps_start_time)

    def sound_of_running(self):
        """
        Включает звук бега для персонажа.
        :return: звук.
        """
        # Проверка на то, что не включен звук ходьбы.
        if self.audio.steps_start_time + steps_duration <= time.time():
            self.audio.Sound_play(self.audio.running, running_duration, self.audio.running_start_time)
            self.audio.running_start_time = self.audio.check_sound(running_duration, self.audio.running_start_time)

    @property
    def pos(self):
        return (self.x_player, self.y_player)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            self.sound_of_running()
            self.x_player += player_speed * np.cos(self.angle)
            self.y_player += player_speed * np.sin(self.angle)
        if pressed_keys[pygame.K_a]:
            self.sound_of_steps()
            self.x_player += player_speed * np.sin(self.angle)
            self.y_player -= player_speed * np.cos(self.angle)
        if pressed_keys[pygame.K_d]:
            self.sound_of_steps()
            self.x_player -= player_speed * np.sin(self.angle)
            self.y_player += player_speed * np.cos(self.angle)
        if pressed_keys[pygame.K_s]:
            self.sound_of_steps()
            self.x_player -= player_speed * np.cos(self.angle)
            self.y_player -= player_speed * np.sin(self.angle)

        if pressed_keys[pygame.K_RIGHT]:
            self.angle -= player_angle_change_speed
        if pressed_keys[pygame.K_LEFT]:
            self.angle += player_angle_change_speed

from settings import *
import pygame
import numpy as np


class Player:
    def __init__(self):
        self.x_player, self.y_player = player_pos
        self.angle = player_angle

    def audio_init(self, audio):
        self.audio = audio

    @property
    def pos(self):
        return (self.x_player, self.y_player)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a]:
            self.x_player += player_speed * np.sin(self.angle)
            self.y_player -= player_speed * np.cos(self.angle)
        if pressed_keys[pygame.K_d]:
            self.x_player -= player_speed * np.sin(self.angle)
            self.y_player += player_speed * np.cos(self.angle)
        if pressed_keys[pygame.K_s]:
            self.x_player -= player_speed * np.cos(self.angle)
            self.y_player -= player_speed * np.sin(self.angle)
        if pressed_keys[pygame.K_w]:
            self.x_player += player_speed * np.cos(self.angle)
            self.y_player += player_speed * np.sin(self.angle)

        if pressed_keys[pygame.K_RIGHT]:
            self.angle -= player_angle_change_speed
        if pressed_keys[pygame.K_LEFT]:
            self.angle += player_angle_change_speed


from settings import *
import pygame

class Player:
    def __init__(self):
        self.angle = player_angle
        self.x_player = x_player
        self.y_player = y_player

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_a]:
            self.x_player -= 1
        if pressed_keys[pygame.K_d]:
            self.x_player += 1
        if pressed_keys[pygame.K_s]:
            self.y_player += 1
        if pressed_keys[pygame.K_w]:
            self.y_player -= 1
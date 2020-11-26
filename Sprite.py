from settings import *
import pygame
from Player import *
import numpy as np
from map import *

player = Player()
pygame.init()

class Sprite:
    def __init__(self, scale, x_pos, y_pos, file):
        self.scale = scale
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle_to_player = 0
        self.surf = pygame.image.load(file)

    def angle(self):
        delta_x = self.x_pos - player.x_player
        delta_y = self.y_pos - player.y_player
        angle_sprite = np.arctan(delta_y / delta_x)
        angle_to_player = angle_sprite - player.angle
        if delta_x > 0:
            angle_to_player += np.pi
        angle_to_player %= 2*np.pi
        return angle_to_player

    def size(self):
        angle_to_player = self.angle()
        distance_to_player = ((self.x_pos - player.x_player) ** 2 + (self.y_pos - player.y_player) ** 2) ** (1 / 2)
        proec_size = int(distance / distance_to_player * self.scale * size_sprite)
        if distance_to_player > 30:
            return proec_size
        else:
            return 0

    def draw(self):
        guard_surf_new = pygame.transform.scale(self.surf, (int(sprite1.size()), int(sprite1.size())))

        angle_to_player = self.angle()
        if not (angle_to_player < np.pi / 2 or angle_to_player > 3 / 2 * np.pi):
            guard_rect = guard_surf_new.get_rect(
                center=(width_screen // 2 - distance * np.tan(sprite1.angle()), height_screen // 2))
            screen.blit(guard_surf_new, guard_rect)


screen = pygame.display.set_mode((width_screen, height_screen))
d = sprite1_data
sprite1 = Sprite(d[0], d[1], d[2], d[3])

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    player.move()
    pygame.draw.rect(screen, Blue, (0, 0, width_screen, height_screen // 2))
    pygame.draw.rect(screen, Yellow, (0, height_screen // 2, width_screen, height_screen // 2))

    # Для теста, рисование "мини-карты"
    pygame.draw.circle(screen, Green, (int(player.x_player), int(player.y_player)), 5)
    pygame.draw.circle(screen, Red, (int(sprite1.x_pos), int(sprite1.y_pos)), 5)
    pygame.draw.line(screen, Green, (player.x_player, player.y_player),
                     (player.x_player + width_screen * np.cos(player.angle), player.y_player + width_screen * np.sin(player.angle)), 2)

    sprite1.draw()
    pygame.display.flip()

pygame.quit()

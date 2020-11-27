import pygame
from Player import *
from map import *
from ray_casting import *


def draw_minimap(player, screen):
    x_pl = int(player.x_player) // scale_minimap
    y_pl = int(player.y_player) // scale_minimap
    pygame.draw.rect(screen, Black, ((0, 0), (width_screen // scale_minimap, height_screen // scale_minimap)))
    pygame.draw.circle(screen, Green, (x_pl, y_pl), player_radius)
    pygame.draw.line(screen, Yellow, (x_pl, y_pl),
                     (x_pl + player_length * np.cos(player.angle),
                      y_pl + player_length * np.sin(player.angle)), player_width)
    for x, y in map:
        pygame.draw.rect(screen, Red,
                         (x // scale_minimap, y // scale_minimap, cube // scale_minimap, cube // scale_minimap))

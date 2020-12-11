#from engine.Player import *
#import engine.Player
from engine.map import *
import numpy as np
#from engine.ray_casting import *
#import engine.ray_casting


def draw_minimap(player, screen):
    '''
    Рисует миникарту.
    :param player: игрок
    :param screen: экран, на котором будет карта
    '''
    # Рисование бэкграунда
    pygame.draw.rect(screen, Black,
                     ((0, 0), (len(text_map[1]) * cube // scale_minimap, len(text_map) * cube // scale_minimap)))
    # Рисование игрока
    x_pl = int(player.x_player) // scale_minimap
    y_pl = int(player.y_player) // scale_minimap
    pygame.draw.circle(screen, Green, (x_pl, y_pl), player_radius)
    pygame.draw.line(screen, Yellow, (x_pl, y_pl),
                     (x_pl + player_length * np.cos(player.angle),
                      y_pl + player_length * np.sin(player.angle)), player_width)

    # Рисование кубиков
    for x, y in map:
        if map[(x, y)] in ['0', '6', '7']:
            pygame.draw.rect(screen, Red,
                             (x // scale_minimap, y // scale_minimap, cube // scale_minimap, cube // scale_minimap))
        if map[(x, y)] in ['1', '2', '3', '4', '5']:
            pygame.draw.rect(screen, Green,
                             (x // scale_minimap, y // scale_minimap, cube // scale_minimap, cube // scale_minimap))
        if map[(x, y)] in ['o', 'd', 't', 'c', 'p']:
            pygame.draw.rect(screen, Yellow,
                             (x // scale_minimap, y // scale_minimap, cube // scale_minimap, cube // scale_minimap))

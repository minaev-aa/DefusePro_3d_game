from engine.Player import *
from minigames.letter import *
from minigames.minigame import *
from minigames.minigame2 import *


def active(player, Mistake):
    """
    Если подойти к определённым стенам и нажать 'E', то запуститься миниигра.
    """
    for x, y in active_in_map:
        if player.x_player > x - active_size and player.x_player < x + cube + active_size \
                and player.y_player > y - active_size and player.y_player < y + cube + active_size:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    if active_in_map[x, y] == '1':
                        return ('1', Manager(False,  sn, Mistake))
                    if active_in_map[x, y] == '2':
                        A = game2(sn, Mistake).draw()
                        return ('2', A)
                    if active_in_map[x, y] == '3':
                        pass
                    if active_in_map[x, y] == '4':
                        pass
                    if active_in_map[x, y] == '5':
                        pass
                    if active_in_map[x, y] in ['o', 'd','t', 'c', 'p']:
                        Letter(screen, active_in_map[x, y]).draw()


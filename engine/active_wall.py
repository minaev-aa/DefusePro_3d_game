#from engine.Player import *
#import engine.Player
from engine.map import *
import minigames.finishedgame
import minigames.letter
import minigames.minigame
import minigames.minigame2
import minigames.minigame3
import minigames.minigame4
from settings import *


def active(minigames_list, player, Mistake, TimeAll):
    """
    Если подойти к определённым стенам и нажать 'E', то запуститься миниигра.
    """
    for x, y in active_in_map:
        if player.x_player > x - active_size and player.x_player < x + cube + active_size \
                and player.y_player > y - active_size and player.y_player < y + cube + active_size:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    if player.role == 1:
                        if active_in_map[x, y] in ['o', 'd', 't', 'c', 'p']:
                            return (minigames.letter.Letter(screen, active_in_map[x, y], TimeAll).draw())
                    if player.role == 2:
                        if active_in_map[x, y] not in ['o', 'd', 't', 'c', 'p']:
                            if minigames_list[int(active_in_map[x, y]) - 1] == 0:
                                if active_in_map[x, y] == '1':
                                    return ('1', minigames.minigame.Manager(False, screen, Mistake, TimeAll))
                                if active_in_map[x, y] == '2':
                                    A = minigames.minigame2.game2(sn, Mistake, TimeAll).draw()
                                    return ('2', A)
                                if active_in_map[x, y] == '3':
                                    B = minigames.minigame3.Game3(Mistake, TimeAll).manager()
                                    return ('3', B)
                                if active_in_map[x, y] == '4':
                                    C = minigames.minigame4.game4(Mistake, TimeAll).Manager()
                                    return ('4', C)
                                if active_in_map[x, y] == '5':
                                    pass
                            if minigames_list[int(active_in_map[x, y]) - 1] == 1:
                                minigames.finishedgame.fingame(0, TimeAll).draw()

import engine.map
import minigames.finishedgame
import minigames.letter
import minigames.minigame
import minigames.minigame2
import minigames.minigame3
import minigames.minigame4
import minigames.minigame5
from settings import *


def active(minigames_list, player, Mistake, TimeAll):
    """
    Если подойти к определённым стенам и нажать 'E', то запуститься миниигра.
    """
    map, active_in_map = engine.map.map_create(engine.map.text_map)
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
                                    F = minigames.minigame.Manager(False, sn, Mistake, TimeAll)

                                if active_in_map[x, y] == '2':
                                    F = minigames.minigame2.game2(sn, Mistake, TimeAll).draw()

                                if active_in_map[x, y] == '3':
                                    F = minigames.minigame3.Game3(Mistake, TimeAll).manager()

                                if active_in_map[x, y] == '4':
                                    F = minigames.minigame4.game4(Mistake, TimeAll).Manager()

                                if active_in_map[x, y] == '5':
                                    F = minigames.minigame5.game5(Mistake, TimeAll).main()

                                return (active_in_map[x, y], F)
                            if minigames_list[int(active_in_map[x, y]) - 1] == 1:
                                minigames.finishedgame.fingame(0, TimeAll).draw()

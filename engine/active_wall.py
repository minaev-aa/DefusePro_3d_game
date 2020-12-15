import engine.map
import minigames.finishedgame
import minigames.letter
import minigames.minigame
import minigames.minigame2
import minigames.minigame3
import minigames.minigame4
import minigames.minigame5
from settings import *


def active(minigames_list, player, mistake, TimeAll):
    '''
    :param minigames_list: список завершённых миниигр
    :param player: игрок
    :param mistake: Количество ошибок
    :param TimeAll: Время начала программы
    :return: Если подойти к определённым стенам и нажать 'E', то запуститься миниигра.

    '''
    map, active_in_map = engine.map.map_create(engine.map.text_map)
    for x, y in active_in_map:
        if player.x_player > x - active_size and player.x_player < x + cube + active_size \
                and player.y_player > y - active_size and player.y_player < y + cube + active_size:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    if player.role == 1 and active_in_map[x, y] in ['o', 'd', 't', 'c', 'p']:
                        return (minigames.letter.Letter(screen, active_in_map[x, y], TimeAll).manager())
                    if player.role == 2 and active_in_map[x, y] not in ['o', 'd', 't', 'c', 'p']:
                        if minigames_list[int(active_in_map[x, y]) - 1] == 0:
                            if active_in_map[x, y] == '1':
                                func = minigames.minigame.Manager(False, sn, mistake, TimeAll)

                            if active_in_map[x, y] == '2':
                                func = minigames.minigame2.Game2(sn, mistake, TimeAll).manager()

                            if active_in_map[x, y] == '3':
                                func = minigames.minigame3.Game3(mistake, TimeAll).manager()

                            if active_in_map[x, y] == '4':
                                func = minigames.minigame4.Game4(mistake, TimeAll).manager()

                            if active_in_map[x, y] == '5':
                                func = minigames.minigame5.Game5(mistake, TimeAll).manager()
                            return (active_in_map[x, y], func)
                        if minigames_list[int(active_in_map[x, y]) - 1] == 1:
                            minigames.finishedgame.Fingame(0, TimeAll).manager()

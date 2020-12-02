from map import *
from Player import *
from minigame import *
from minigame2 import *
from settings import *
from letter import *


def active(player, timer_event, Time, Mistake):
    for x, y in active_in_map:
        if player.x_player > x - active_size and player.x_player < x + cube + active_size \
                and player.y_player > y - active_size and player.y_player < y + cube + active_size:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    if active_in_map[x,y] == '1':
                        return('1', Manager(False, timer_event, Time, sn, Mistake))
                    if active_in_map[x,y] == '2':
                        A = game2(timer_event, Time, sn, Mistake)
                        return('2', A.draw())
                    if active_in_map[x,y] == '3':
                        pass
                    if active_in_map[x,y] == '4':
                        pass
                    if active_in_map[x,y] == '5':
                        pass
                    if active_in_map[x,y] == 'o':
                        return(Letter(screen, timer_event, Time, 'o').draw())
                    if active_in_map[x,y] == 'd':
                        return(Letter(screen, timer_event, Time, 'd').draw())
                    if active_in_map[x,y] == 't':
                        return(Letter(screen, timer_event, Time, 't').draw())
                    if active_in_map[x,y] == 'c':
                        return(Letter(screen, timer_event, Time, 'c').draw())
                    if active_in_map[x,y] == 'p':
                        return(Letter(screen, timer_event, Time, 'p').draw())
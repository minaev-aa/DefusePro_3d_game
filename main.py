import pygame
from settings import *
from Player import *
from pygame.draw import *
from map import *
from texture import Planning
from main_menu import Menu, Button, Load_cicle, Settings, Points_of_settings
from minimap import *
from network import Network
from Sprite import *
from active_wall import *

pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))
sc = Planning(screen)
# Инициализация загрузчика.
Loader = Load_cicle(screen)


# guard1_data = (1, width_screen, height_screen, 'Resources\\Sprayt\\guard_good.png') # Маштаб, х, y, файл


def Menu_func():
    """
    Запускает окно загрузки игры.
    Потом открывает главное меню.
    :return: Окно.
    """
    Loader.main_menu_init()
    # p.audio_init(Loader.audio)
    # Отрисовка меню.
    finished = False
    while not finished:

        screen.blit(Loader.LK, (0, -100))
        Loader.menu.draw()
        pygame.time.delay(60)
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                is_one_of_buttons_on = Loader.menu.is_one_of_buttons_on()
                if is_one_of_buttons_on != -1:
                    Loader.audio.Sound_play(Loader.audio.sound_if_button_down,
                                            sound_if_button_down_duration,
                                            Loader.audio.sound_if_button_down_start_time)
                    Loader.audio.sound_if_button_down_start_time \
                        = Loader.audio.check_sound(sound_if_button_down_duration,
                                                   Loader.audio.sound_if_button_down_start_time)
                    num_in_massive_of_buttoms_from_main_menu = is_one_of_buttons_on
                    indificate_func(num_in_massive_of_buttoms_from_main_menu)
                    finished = True


def indificate_func(num_in_massive_of_buttoms):
    """
    Проверяет, какая из кнопок была нажата и запускает команду соответствующую этой кнопке.
    :param num_in_massive_of_buttoms: Номер нажатой кнопки в массиве.
    :return: None
    """
    if num_in_massive_of_buttoms == 0:
        Main_game()
    elif num_in_massive_of_buttoms == 1:
        pass
    elif num_in_massive_of_buttoms == 2:
        Menu_of_settings()
    else:
        pass


def Menu_of_settings():
    """
    Рисует окно настроек.
    """
    Set_Win = Settings(screen)
    Set_Win.main()

    finnish1 = False
    while not finnish1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                finnish1 = True
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    finnish1 = True
            elif i.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                Loader.audio.is_sounds_on = (Set_Win.points[0].is_point_down(mouse_position))
        Set_Win.draw_set_win()
        pygame.time.delay(60)
        pygame.display.update()

    Menu_func()


def redrawWindow(win, player, player2, ModelPlayer, text):
    pressed_keys = pygame.key.get_pressed()
    sc.sky(player.angle)
    sprite_surf, sprite_rect = ModelPlayer.draw()
    sprites = (ModelPlayer.distance_to_player(), sprite_surf, sprite_rect)
    sc.plan(player.pos, player.angle, sprites)
    ModelPlayer.move(player2.x_player, player2.y_player)
    #ModelPlayer.draw()
    if pressed_keys[pygame.K_m]:
        draw_minimap(player, screen)
    if pressed_keys[pygame.K_t]:
        global Time
        surf1 = pygame.Surface((300, 120))
        surf1.fill(White)
        text_rect = text.get_rect(center=surf1.get_rect().center)
        surf1.fill(White)
        surf1.blit(text, text_rect)
        screen.blit(surf1, (0, 0))
    # pygame.draw.circle(screen, Red, player.pos, 10)
    # pygame.draw.circle(screen, Red, player2.pos, 10)
    # pygame.draw.circle(screen, Green, (ModelPlayer.x_pos // scale_minimap, ModelPlayer.y_pos // scale_minimap), 5)
    pygame.display.flip()


def Main_game():
    global All, Time
    minigames = [0] * count_of_minigame
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)
    font = pygame.font.SysFont(None, 100)
    text = font.render(str(Time) + ' сек', True, Black)
    n = Network()
    p = n.getP()
    p2 = n.send(p)
    ModelPlayer = Guard(1, p2.x_player, p2.y_player, screen, p)
    fr = 0
    while not All:
        pygame.time.Clock().tick(FPS)
        fr += 0
        if fr % 10 == 0:
            p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                All = True
            if event.type == timer_event:
                Time -= 1
                text = font.render(str(Time) + ' сек', True, Black)
                if Time == 0:
                    All = True
                    finished = True
        p.move()
        if p.is_player_move():
            Loader.audio.Sound_play(Loader.audio.steps, steps_duration, Loader.audio.steps_start_time)
            Loader.audio.steps_start_time = Loader.audio.check_sound(steps_duration, Loader.audio.steps_start_time)
        redrawWindow(sc, p, p2, ModelPlayer, text)
        try:
            ro = active(p, timer_event, Time)
            minigames[int(ro[0]) - 2], Time = ro[1]
        except:
            try:
                ro = active(p, timer_event, Time)
                if ro!= None:
                    Time = ro
            except:
                pass
    #TODO Проверка времени, количесттва ошибок и выполненных заданий
    pygame.quit()


if __name__ == '__main__':
    Menu_func()

import pygame
from settings import *
from Player import *
from pygame.draw import *
from map import *
from texture import Planning
from main_menu import Menu, Button, Load_cicle
from minimap import *
from network import Network
from Sprite import *


pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))
sc = Planning(screen)
# Инициализация загрузчика.
Loader = Load_cicle(screen)
#guard1_data = (1, width_screen, height_screen, 'Resources\\Sprayt\\guard_good.png') # Маштаб, х, y, файл

def Menu_func():
    """
    Запускает окно загрузки игры.
    Потом открывает главное меню.
    :return: Окно.
    """
    Loader.main_menu_init()
    #p.audio_init(Loader.audio)
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
    print(num_in_massive_of_buttoms)
    if num_in_massive_of_buttoms == 0:
        Main_game()
    elif num_in_massive_of_buttoms == 1:
        pass
    else:
        pass

def redrawWindow(win,player, player2, ModelPlayer):
    pressed_keys = pygame.key.get_pressed()
    sc.sky(player.angle)
    sc.plan(player.pos, player.angle)
    ModelPlayer.move(player2.x_player, player2.y_player)
    if pressed_keys[pygame.K_m]:
        draw_minimap(player, screen)
    pygame.draw.circle(screen, Red, player.pos, 10)
    pygame.draw.circle(screen, Red, player2.pos, 10)
    pygame.draw.circle(screen, Green, (ModelPlayer.x_pos // scale_minimap, ModelPlayer.y_pos // scale_minimap), 5)
    pygame.display.flip()

def Main_game():
    finished = False
    n = Network()
    p = n.getP()
    p2 = n.send(p)
    print(p2.x_player, p2.y_player)
    ModelPlayer = Guard(1, p2.x_player, p2.y_player, screen, p)
    fr = 0
    while not finished:
        pygame.time.Clock().tick(FPS)
        fr += 0
        if fr % 10 == 0:
            p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        ModelPlayer.draw()
        p.move()
        if p.is_player_move():
            Loader.audio.Sound_play(Loader.audio.steps, steps_duration, Loader.audio.steps_start_time)
            Loader.audio.steps_start_time = Loader.audio.check_sound(steps_duration, Loader.audio.steps_start_time)
        redrawWindow(sc, p, p2, ModelPlayer)
    pygame.quit()


if __name__ == '__main__':
    Menu_func()
    #Main_game()

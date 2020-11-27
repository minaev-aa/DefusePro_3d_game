import pygame
from settings import *
from Player import *
from pygame.draw import *
from map import *
from ray_casting import *
from main_menu import Menu, Button, Load_cicle
from minimap import *

player = Player()
pygame.init()

screen = pygame.display.set_mode((width_screen, height_screen))


def Menu_func():
    """
    Запускает окно загрузки игры.
    Потом открывает главное меню.
    :return: Окно.
    """
    # Инициализация загрузчика.
    Loader = Load_cicle(screen)
    Loader.main_menu_init()
    # Отрисовка меню.
    finished = False
    while not finished:

        screen.blit(Loader.LK, (0, -100))  # Поправить, если будет новое разрешение.
        Loader.menu.draw()
        pygame.time.delay(60)
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                is_one_of_buttons_on = Loader.menu.is_one_of_buttons_on()
                if is_one_of_buttons_on != -1:
                    Loader.audio.Sound_play(Loader.audio.sound_if_button_down)
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


def Main_game():
    finished = False
    while not finished:
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        player.move()
        pygame.draw.rect(screen, Blue, (0, 0, width_screen, height_screen//2))
        pygame.draw.rect(screen, Yellow, (0, height_screen//2, width_screen, height_screen//2))
        ray_casting(screen, player.pos, player.angle)
        draw_minimap(player, screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    Menu_func()
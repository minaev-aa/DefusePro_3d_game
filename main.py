from engine.Sprite import *
from engine.active_wall import *
from engine.minimap import *
from engine.network import Network
from engine.texture import Planning
from minigames.main_menu import Load_cicle, Settings
from settings import *

pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))
sc = Planning(screen)
# Инициализация загрузчика.
Loader = Load_cicle(screen)


# guard1_data = (1, width_screen, height_screen, 'Resources\\Sprayt\\guard_good.png') # Маштаб, х, y, файл


def Menu_func(All, Mistake):
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
                    indificate_func(num_in_massive_of_buttoms_from_main_menu, All, Mistake)
                    finished = True


def indificate_func(num_in_massive_of_buttoms, All, Mistake):
    """
    Проверяет, какая из кнопок была нажата и запускает команду соответствующую этой кнопке.
    :param num_in_massive_of_buttoms: Номер нажатой кнопки в массиве.
    :return: None
    """
    if num_in_massive_of_buttoms == 0:
        Main_game(All, Mistake)
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
    '''
    :param win: экран
    :param player: основной игрок
    :param player2: второй игрок
    :param ModelPlayer: модель второго игрока
    :param text: объект текста с оставшимся временем в таймер
    :return: обновление экрана
    '''
    pressed_keys = pygame.key.get_pressed()
    sc.sky(player.angle)
    sprite_surf, sprite_rect = ModelPlayer.draw()
    sprites = (ModelPlayer.distance_to_player(), sprite_surf, sprite_rect)
    sc.plan(player.pos, player.angle, sprites)
    ModelPlayer.move(player2.x_player, player2.y_player)
    if pressed_keys[pygame.K_m]:
        draw_minimap(player, screen)
    if pressed_keys[pygame.K_t]:
        surf1 = pygame.Surface((300, 120))
        surf1.fill(White)
        text_rect = text.get_rect(center=surf1.get_rect().center)
        surf1.fill(White)
        surf1.blit(text, text_rect)
        screen.blit(surf1, (0, 0))
    pygame.display.flip()


def Main_game(All, Mistake):
    font = pygame.font.SysFont(None, 100)
    text = font.render(str(Time) + ' сек', True, Black)
    n = Network()
    p = n.getP()
    p2 = n.send(p)
    ModelPlayer = Guard(1, p2.x_player, p2.y_player, screen, p)
    fr = 0
    while not All:
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                All = True
                p.change(True, 1)
        text = font.render(str(Time - round(time.time()-TimeAll)) + ' сек', True, Black)
        p.move()
        if p.is_player_move():
            Loader.audio.Sound_play(Loader.audio.steps, steps_duration, Loader.audio.steps_start_time)
            Loader.audio.steps_start_time = Loader.audio.check_sound(steps_duration, Loader.audio.steps_start_time)
        redrawWindow(sc, p, p2, ModelPlayer, text)
        ro = active(minigames, p, Mistake)
        if type(ro) != type(None):
            minigames[int(ro[0]) - 1], Mistake = ro[1]
        if (Time - round(time.time()-TimeAll)) <= 0 or (Mistake > 3):
            All = True
            p.change(True, 1)
            p2 = n.send(p)
            fingame(1).draw()
        try:
            minigames.index(0)
        except:
            All = True
            p.change(True, 2)
            p2 = n.send(p)
            fingame(2).draw()
        if p2.status[0]:
            All = True
            fingame(p2.status[1]).draw()

        p2 = n.send(p)
    pygame.quit()

if __name__ == '__main__':
    Menu_func(All, Mistake)

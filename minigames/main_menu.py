import time

import pygame as pg

from engine.Music_module import Audio_source
from settings import *


class Menu():
    def __init__(self, audio, sc):
        """
        Это конструктор главного меню.
        :param audio: обьект, делающий звук.
        :param sc: Экран, на котором рисуется игра.
        """
        self.size_of_font = 30
        self.but_size = 120
        self.buts = []
        self.audio = audio
        self.W = width_screen  # Размеры экрана для модуля главного меню.
        self.H = height_screen  # Ширина для модуля главного меню.
        self.y_but = self.H // 2
        self.sc = sc
        # Создадим кнопок.
        self.but_init(self.W // 2, self.y_but, "Подключиться", self.but_size)
        self.but_init(self.W // 2, self.y_but, "Настройки", self.but_size)
        self.but_init(self.W // 2, self.y_but, "Выход", self.but_size)

    def draw(self):
        """
        Отрисовывает элементы главного меню.
        Включает звук, если курсор над клавишей.
        :return: Новые элементы.
        """
        pos_of_mouse = pg.mouse.get_pos()
        for num in range(len(self.buts)):
            # Проверка на наведение курсора, и на то, что это первый кадр, когда курсор на кнопке
            if self.buts[num].is_down != self.buts[num].is_but_down(pos_of_mouse) and \
                    self.buts[num].is_but_down(pos_of_mouse):
                self.audio.Sound_play(self.audio.sound_when_cursor_under_button,
                                      sound_when_cursor_under_button_duration,
                                      self.audio.sound_when_cursor_under_button_start_time)
                self.audio.sound_when_cursor_under_button_start_time \
                    = self.audio.check_sound(sound_when_cursor_under_button_duration,
                                             self.audio.sound_when_cursor_under_button_start_time)

            self.buts[num].draw()

    def but_init(self, x, y, text, size):
        """
        Инициализирует кнопки.
        :param x и y:  Координаты центра экрана.
        :param text:  Текст, который будет написан на кнопке.
        :param size:  Размер кнопки.
        :return:  Массив кнопок, готовых к использованию.
        """
        self.buts.append(Button(size, x, y, self.audio, self.sc))
        l = len(self.buts)
        self.buts[l - 1].Text = text
        self.y_but += int(0.7 * size)

    def is_one_of_buttons_on(self):
        """
        Проверяетб нажата ли кнопка.
        :return: -1, если не нажата, номер нажатой кнопки в массиве, если нажата.
        """
        self.searched = False
        for num in range(len(self.buts)):
            if self.buts[num].is_down == 1:
                self.searched = True
                return num
        if not self.searched:
            return -1


class Button():
    def __init__(self, size, x, y, audio, sc):
        """
        Это конструктор класса кнопок.
        :param size: ширина кнопки.
        :param x и y: Координаты центра кнопки.
        :param audio: обьект, делающий звук.
        :param sc: Экран, на котором рисуется игра.
        """
        self.size_of_font = 30
        self.size = size
        self.Text = "Введите текст"
        self.y = y
        self.x = x
        self.sc = sc
        self.BACK_LOAD = (250, 235, 205)  # Цвет для фона экрана загрузки.
        self.BUT_LOAD = (240, 225, 215)  # Цвет для нажатой кнопки экрана загрузки.
        self.COLOR = self.BACK_LOAD
        self.W = width_screen  # Размеры экрана для модуля главного меню.
        self.H = height_screen  # Ширина для модуля главного меню.
        self.pi = 3.14

        self.audio = audio
        self.is_down = 0

    def draw(self):
        """
        Рисует кнопку.
        :param x и y: Координаты центра кнопки.
        :return: кнопку на экране.
        """
        sc = self.sc
        x = self.x
        y = self.y
        a = int(self.size / 2)
        pg.draw.arc(sc, self.COLOR,
                    (x - 3 * a, y - a / 2, 6 * a, a),
                    0, 2 * self.pi, 13)
        text_blit(x - int((len(self.Text) / 2) * self.size_of_font // 3),
                  y - int(self.size_of_font / 3),
                  self.Text, White, self.size_of_font)

    def is_but_down(self, massive):
        """
        Проверяет, наведена ли мышь на кнопку
        :param massive: Массив координат мыши.
        :return: 1, если мышь нажата, иначе 0.
        """
        a = int(self.size / 2)
        if self.y - a / 2 < massive[1] < self.y + a / 2 and \
                self.W // 2 - 3 * a < massive[0] < self.W // 2 + 3 * a:
            self.COLOR = self.BUT_LOAD
            self.is_down = 1
            return self.is_down
        else:
            self.COLOR = self.BACK_LOAD
            self.is_down = 0
            return self.is_down


class Load_cicle():
    """
    Это класс обьекта, являющегося индификатором процесса загрузки.
    """

    def __init__(self, sc):
        """
        Это конструктор класса загрузочный модуль.
        :param sc: Экран, на котором рисуется игра.
        """
        self.persent_of_load = 0
        self.opposite_persent_of_load = 0
        self.scale = 1
        self.size = 150
        self.sc = sc
        self.size_of_font = 30
        self.GREEN_LOAD = (10, 200, 20)  # Цвет кружка загрузки.
        self.BACK_LOAD = (250, 235, 205)  # Цвет для фона экрана загрузки.
        self.BUT_LOAD = (240, 225, 215)  # Цвет для нажатой кнопки экрана загрузки.
        self.W = width_screen  # Размеры экрана для модуля главного меню.
        self.H = height_screen  # Ширина для модуля главного меню.
        self.pi = 3.14


    def draw_cicle(self, x, y):
        """
        Рисует шкалу загрузки.
        :param x и y: Координаты центра экрана, на котором рисуется шкала.
        :return: шкалу загрузки на экране.
        """
        sc = self.sc
        r = int(self.size / 2)
        pg.draw.arc(sc, self.GREEN_LOAD,
                    (x - r, y - r, 2 * r, 2 * r),
                    self.opposite_persent_of_load, 2 * self.pi * self.persent_of_load, 13)
        font = pg.font.Font(None, self.size_of_font)  # Задает шрифт.
        text = font.render(str(int(self.persent_of_load * 100)) + "%", True, Grey)
        # Добавляет текст на шкалу на координатах x, y.
        sc.blit(text, [int(x - self.size_of_font / 3), int(y - self.size_of_font / 3)])

    def draw_all_load(self):
        """
        Меняет цвет фона и рисует процесс загрузки.
        :return: фон, процесс загрузки.
        """
        pg.draw.rect(self.sc, self.BACK_LOAD, (0, 0, self.W, self.H), 0)
        self.draw_cicle(self.W // 2, self.H // 2)

    def main_menu_init(self):
        """
        Запускает главное меню и загружает все, что необходимо для работы игры в переменные.
        Паралельно отрисовывает процесс загрузки.
        :return: Главное меню и процесс его загрузки.
        """
        count = 13
        self.persent_of_load = 0
        self.draw_all_load()  # 0 - номер процедуры подгрузки.
        pg.display.update()


        self.LK = pg.image.load('Resources\Textures\ЛК.jpg')  # 1
        self.__upd__main_load(count)

        self.audio = Audio_source()  # 2
        self.__upd__main_load(count)

        self.menu = Menu(self.audio, self.sc)  # 3
        self.__upd__main_load(count)

        self.Set_Win = Settings(screen)
        self.__upd__main_load(count)

        Dict_of_audio_inits = {self.audio.sound_when_cursor_under_button_init(): '1',
                               self.audio.sound_if_button_down_init(): '2',
                               self.audio.steps_init(): '3',
                               self.audio.running_init(): '4',
                               self.audio.plus_anything_init(): '5',
                               self.audio.shortness_init(): '6',
                               self.audio.exhalation_init(): '7',
                               self.audio.checkpoint_init(): '8'}
        # Массив звуков.
        self.Audios = [self.audio.steps,
                       self.audio.running,
                       self.audio.plus_anythings,
                       self.audio.sound_when_cursor_under_button,
                       self.audio.sound_if_button_down,
                       self.audio.shortness,
                       self.audio.exhalation,
                       self.audio.checkpoint]

        # Инициализация звуков.
        for num in range(len(self.Audios)):  # 4 - 11
            Dict_of_audio_inits.get(str(num + 1))
            self.__upd__main_load(count)
        # Загрузка настроек.
        file = open('Resources\Sets_saves\sets.txt', 'r')  # 12
        Sets = file.readlines()
        self.audio.is_sounds_on = int(Sets[0].split()[0])
        file.close()
        self.__upd__main_load(count)
        # Помни, что нужно увеличить count, если добавил процедур загрузки.

    def __upd__main_load(self, count):
        """
        Process of load.
        """
        self.persent_of_load += 1 / count
        time.sleep(0.05)
        self.draw_all_load()
        pg.display.update()


class Settings():
    """
    Этот класс отвечает за рисование окна настроек для главного меню.
    """

    def __init__(self, sc):
        self.size = height_screen // 3
        self.y0 = height_screen - self.size
        self.delta = 50
        self.sc = sc
        self.size_of_font = 30
        self.points = []
        self.fractional_points = []
        self.main()

    def main(self):
        """
        Определяет размеры и настроки для окна настроек.
        Здесь можно добавить пунктов бинарной настройки фунцией self.setting_point().
        Можно добавить промежуточных настроек типа позунок функцией self.fractional_point_init().
        А после, добавить её в списке настроек settings_list.
        """
        self.x = width_screen // 2
        self.y = height_screen // 2
        self.a = self.size
        # Список настроек. Здсь сверху вниз 1 - бинарная настройка, 2 - дробная.
        self.settings_list = [(1, 'Звук'), (2, 'Скорость поворота')]
        file = open('Resources\Sets_saves\sets.txt', 'r')
        Sets = file.readlines()
        file.close()
        for i in range(len(self.settings_list)):
            if self.settings_list[i][0] == 1:
                self.setting_point(self.settings_list[i][1], self.size, int(Sets[0].split()[i]))
            elif self.settings_list[i][0] == 2:
                self.fractional_point_init(self.settings_list[i][1], self.size, int(Sets[0].split()[i]))

    def draw_set_win(self):
        """
        Рисует окно настроек.
        """
        b = 0.65 * self.a
        c = self.a // 4
        pygame.draw.rect(self.sc, BACK_LOAD, (self.x - self.a, self.y - self.a, 2 * self.a, 2 * self.a), 0)
        pygame.draw.rect(self.sc, Black, (self.x - self.a, self.y - self.a, 2 * self.a, 2 * self.a), 2)
        font = pg.font.Font(None, self.size_of_font)  # Задает шрифт.
        text = font.render('ВЫХОД', True, Black)
        # Добавляет текст на нужных координатах x, y.
        self.sc.blit(text, [self.x + b, self.y - b - c])
        text = font.render(' ESC', True, Black)
        # Добавляет еще текста сразу под предыдущим.
        self.sc.blit(text, [self.x + b, self.y - b - c + self.size_of_font])
        for num in range(len(self.points)):
            self.points[num].draw()
        for num in range(len(self.fractional_points)):
            self.fractional_points[num].draw()

    def setting_point(self, text, size, parametr):
        """
        Добавляет бинарную настройку.
        """
        a = int(0.8 * size)
        self.points.append(Points_of_settings(self.sc, parametr))
        self.points[len(self.points) - 1].Text = text
        self.points[len(self.points) - 1].x = width_screen // 2 - a
        self.y0 += self.delta
        self.points[len(self.points) - 1].y = self.y0 - a

    def fractional_point_init(self, text, size, parametr):
        """
        Добавляет настройку - ползунок (slider).
        """
        a = int(0.8 * size)
        self.fractional_points.append(Fractional_settings(self.sc, parametr))
        self.fractional_points[len(self.points) - 1].Text = text
        self.fractional_points[len(self.points) - 1].x = width_screen // 2 - a
        self.y0 += self.delta
        self.fractional_points[len(self.points) - 1].y = self.y0 - a
        self.y0 += self.delta


class Points_of_settings():
    """
    Это класс отдельных настроек для окна настроек.
    Он реализует использование бинарных настроек.
    """
    def __init__(self, sc, parametr):
        self.Text = "Настройка"
        self.y = 110
        self.x = 110
        self.sc = sc

        self.size = 10
        self.size_of_font = 30
        self.parametr = parametr

    def draw(self):
        """
        Рисует настройку.
        """
        sc = self.sc
        x = self.x
        y = self.y
        a = int(1.5 * self.size)
        b = self.size_of_font // 3

        pg.draw.circle(self.sc, Black, (x, y), self.size, self.size // 6)
        if self.parametr:
            pg.draw.circle(self.sc, Green, (x, y), self.size // 3, 0)

        font = pg.font.Font(None, self.size_of_font)  # Задает шрифт.
        text = font.render(self.Text, True, SET_BUT)
        # Добавляет текст на нухных координатах x, y.
        sc.blit(text, [x + a, y - b])

    def is_point_down(self, massive, number):
        """
        Проверяет, нажали ли на настройку.
        :massive: Это массив данных о положении курсора на экране.
        :number: Это номер настройки в списке settings_list класса Settings (начиная с нуля).
        Возращает ПАРАМЕТР, если курсор нажал на настройку и если не нажал.
        Меняет параметр, если настройка изменена.
        """
        a = self.size / 2
        c = self.size_of_font / 2
        leng = self.size_of_font * len(self.Text)
        if self.x - c <= massive[0] <= self.x + leng and \
                self.y - a <= massive[1] <= self.y + a:
            if self.parametr:
                self.parametr = False
            else:
                self.parametr = True
            save_sets_in_file(number, self.parametr)

        return self.parametr


class Fractional_settings(Points_of_settings):
    """
    Это класс отдельных настроек для окна настроек.
    Он реализует использование настроек, у который можно выбрать градации значений.
    """
    def __init__(self, sc, parametr):
        super(Fractional_settings, self).__init__(sc, parametr)
        self.lenght_of_slider = 220

    def draw(self):
        """
        Рисует ползунок.
        """
        pg.draw.rect(screen, (15, 25, 50), (self.x, self.y + self.size_of_font,
                                            self.lenght_of_slider, self.size // 3), 0)
        x = int(self.x + self.lenght_of_slider * self.parametr / 100)
        self.__draw_endings(Green)
        self.__draw_curcle(x)
        text_blit(self.x + 1.5 * self.size, self.y,
                  self.Text, SET_BUT, self.size_of_font)
        y = self.y + self.size_of_font + self.size
        text_blit(self.x, y, 'Медленнее', SET_BUT, self.size_of_font // 2)
        __text = 'Быстрее'
        x = self.x + self.lenght_of_slider - self.size_of_font * len(__text) // 5
        text_blit(x, y, __text, SET_BUT, self.size_of_font // 2)

    def __draw_endings(self, Colour):
        """
        Рисует законцовки на краях плолоски настроек.
        """
        pg.draw.rect(screen, Colour, (self.x, self.y + self.size_of_font - self.size // 3,
                                      self.size // 3, self.size), 0)
        pg.draw.rect(screen, Colour, (self.x + self.lenght_of_slider,
                                      self.y + self.size_of_font - self.size // 3,
                                      self.size // 3, self.size), 0)

    def __draw_curcle(self, x):
        """
        Рисует кружочек, показывающий состояние настройки.
        x: Координата Х, на которой распожен центр этого кружочка.
        """
        pg.draw.circle(screen, Grey_for_slider, (x, self.y + self.size_of_font), self.size, 0)
        pg.draw.circle(screen, Green, (x, self.y + self.size_of_font), self.size, 1)

    def is_slider_down(self, massive, number):
        """
        Проверяет, наведен ли курсор на настройку.
        Сохраняет новое значение параметра в файле с настройками.
        :massive: Это массив данных о положении курсора на экране.
        :number: Это номер настройки в списке settings_list класса Settings (начиная с нуля).
        :return: Новое значение параметра.
        """
        a = self.size * 1.5
        c = self.lenght_of_slider
        if self.x <= massive[0] <= self.x + c and \
                self.y + a <= massive[1] <= self.y + 3 * a:
            self.parametr = int((massive[0] - self.x) / c * 100)
            save_sets_in_file(number, self.parametr)
        return self.parametr


def text_blit(x, y, text, colour, size_of_font):
    """
    Добавяет текст на экран.
    x: Координата Х верней левой точки области с текстом.
    y: Координата У верней левой точки области с текстом.
    text: Текст, который буде выведен на экране.
    colour: Цвет шрифта.
    size_of_font: Размер шрифта.
    """
    font = pg.font.Font(None, size_of_font)  # Задает шрифт.
    text = font.render(text, True, colour)
    # Добавляет текст на кнопку на координатах x, y.
    screen.blit(text, [x, y])


def save_sets_in_file(number, parametr):
    try:
        with open("Resources\Sets_saves\sets.txt", 'r') as file:
            Sets = file.readlines()[0].split()
            Sets[number] = str(int(parametr))
        with open("Resources\Sets_saves\sets.txt", 'w') as out_file:
            line_with_sets = ''
            for i in range(len(Sets)):
                line_with_sets += Sets[i] + ' '
            out_file.write(line_with_sets)
    except:
        raise FileNotFoundError("Файл с настройками поврежден. Проверьте Resources\Sets_saves\sets.txt")


if __name__ == '__main__':
    print("Этот модуль не для отдельного использования.\nВключен режим тестирования модуля")

    W = width_screen  # Размеры экрана для модуля главного меню.
    H = height_screen  # Ширина для модуля главного меню.

    pg.init()
    sc = pg.display.set_mode((W, H))
    sc.fill((100, 150, 200))
    print('Проверим модуль погрузки основных данных.')
    final = "Load_cicle .... Инициализирован."
    try:
        Loader = Load_cicle(sc)
    except:
        final = "FAIL/Ошибка - mistake of initialisation/Ошибка инициализации."
    print(final)

    print('Проверка main_menu_init()')
    Loader.main_menu_init()
    if 0 < Loader.persent_of_load > 1:
        print('FAIL/ОШИБКА - Число процедур загрузки больше, чем указано в начале функции.')
    else:
        print("ОК")

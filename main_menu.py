import pygame as pg
import sys
from Music_module import Audio_source
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
        self.but_init(self.W // 2, self.y_but, "Начать", self.but_size)
        self.but_init(self.W // 2, self.y_but, "Продолжить", self.but_size)
        self.but_init(self.W // 2, self.y_but, "Настройки", self.but_size)

    def draw(self):
        """
        Отрисовывает элементы главного меню.
        :return: Новые элементы.
        """
        pos_of_mouse = pg.mouse.get_pos()
        for num in range(len(self.buts)):
            # Проверка на наведение курсора, и на то, что это первый кадр, когда курсор на кнопке
            if self.buts[num].is_down != self.buts[num].is_but_down(pos_of_mouse) and \
                    self.buts[num].is_but_down(pos_of_mouse):
                self.audio.Sound_play(self.audio.sound_when_cursor_under_button)
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
                    (x - 3*a, y - a/2, 6 * a, a),
                    0, 2 * self.pi, 13)
        font = pg.font.Font(None, self.size_of_font)  # Задает шрифт.
        text = font.render(self.Text, True, (255, 255, 255))
        # Добавляет текст на кнопку на координатах x, y.
        sc.blit(text, [x - int((len(self.Text)/2) * self.size_of_font//3),
                       y - int(self.size_of_font / 3)])

    def is_but_down(self, massive):
        """
        Проверяет, наведена ли мышь на кнопку
        :param massive: Массив координат мыши.
        :return: 1, если мышь нажата, иначе 0.
        """
        a = int(self.size / 2)
        if self.y - a/2 < massive[1] < self.y + a/2 and \
                self.W//2 - 3*a < massive[0] < self.W//2 + 3*a:
            self.COLOR = self.BUT_LOAD
            self.is_down = 1
            return 1
        else:
            self.COLOR = self.BACK_LOAD
            self.is_down = 0
            return 0


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
        r = int(self.size/2)
        pg.draw.arc(sc, self.GREEN_LOAD,
                    (x - r, y - r, 2 * r, 2 * r),
                    0, 2 * self.pi * self.persent_of_load/100, 13)
        font = pg.font.Font(None, self.size_of_font)  # Задает шрифт.
        text = font.render(str(int(self.persent_of_load)) + "%", True, (255, 255, 255))
        # Добавляет текст на шкалу на координатах x, y.
        sc.blit(text, [x - self.size_of_font/3, y - self.size_of_font/3])

    def draw_all_load(self):
        """
        Меняет цвет фона и рисует процесс загрузки.
        :return: фон, процесс загрузки.
        """
        pg.draw.rect(self.sc, self.BACK_LOAD, (0, 0, self.W, self.H), 0)
        self.draw_cicle(self.W//2, self.H//2)

    def main_menu_init(self):
        """
        Запускает главное меню и загружает все, что необходимо для работы игры в переменные.
        Паралельно отрисовывает процесс загрузки.
        :return: Главное меню и процесс его загрузки.
        """
        count = 11
        part = int(1 / count * 100)
        self.draw_all_load()  # 0
        pg.display.update()

        self.LK = pg.image.load('Resources\Textures\ЛК.jpg')  # 1
        self.persent_of_load += part
        self.draw_all_load()
        pg.display.update()

        self.audio = Audio_source()  # 2
        self.persent_of_load += part
        self.draw_all_load()
        pg.display.update()

        self.audio.sound_when_cursor_under_button_init()  # 3
        self.persent_of_load += part
        self.draw_all_load()
        pg.display.update()

        self.menu = Menu(self.audio, self.sc)  # 4
        self.persent_of_load += part
        self.draw_all_load()
        pg.display.update()

        self.audio.sound_if_button_down_init()  # 5
        self.persent_of_load += part
        self.draw_all_load()
        pg.display.update()

        self.audio.steps_init()  # 6
        self.persent_of_load += part
        self.draw_all_load()
        pg.display.update()

        self.audio.running_init()  # 7
        self.persent_of_load += part
        self.draw_all_load()
        pg.display.update()

        self.audio.plus_anything_init()  # 8
        self.persent_of_load += part
        self.draw_all_load()
        pg.display.update()

        self.audio.shortness_init()  # 9
        self.persent_of_load += part
        self.draw_all_load()
        pg.display.update()

        self.audio.exhalation_init()  # 10
        self.persent_of_load += part
        self.draw_all_load()
        pg.display.update()

        self.audio.checkpoint_init()  # 11
        self.persent_of_load += part
        self.draw_all_load()
        pg.display.update()
        # Помни, что нужно увеличить count, если добавил процедур загрузки.


def test__module_menu():
    """
    Часть бывшего внутреннего тестировщика.
    :return: окно пайгейм.
    """
    W = 400
    H = 300

    sc = pg.display.set_mode((W, H))
    sc.fill((100, 150, 200))

    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()

        pg.time.delay(20)


def __Menu_func__test__():
    """
    Запускает меню для тестирования модуля.
    :return: меню.
    """
    laod = Load_cicle(sc)

    laod.main_menu_init()

    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
        sc.blit(laod.LK, (0, -100))  # Поправить, если будет новое разрешение.
        laod.menu.draw()
        pg.time.delay(60)
        pg.display.update()


if __name__ == '__main__':
    print("Этот модуль не для отдельного использования.\nВключен режим тестирования модуля")

    W = width_screen  # Размеры экрана для модуля главного меню.
    H = height_screen  # Ширина для модуля главного меню.

    sc = pg.display.set_mode((W, H))
    sc.fill((100, 150, 200))
    pg.init()

    __Menu_func__test__()


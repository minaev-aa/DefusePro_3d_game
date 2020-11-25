import pygame as pg
import sys
from Music_module import Audio_source

GREEN_LOAD = (10, 200, 20)
BACK_LOAD = (250, 235, 205)  # Цвет для фона экрана загрузки.
BUT_LOAD = (240, 225, 215)  # Цвет для нажатой кнопки экрана загрузки.

W = 1300
H = 731
pi = 3.14


class Menu():
    def __init__(self, audio):
        """
        Это конструктор главного меню.
        :param audio: обьект, делающий звук.
        """
        self.size_of_font = 30
        self.but_size = 120
        self.buts = []
        self.audio = audio
        self.y_but = H//2
        # Создадим кнопок.
        self.but_init(W // 2, self.y_but, "Начать", self.but_size)
        self.but_init(W // 2, self.y_but, "Продолжить", self.but_size)
        self.but_init(W // 2, self.y_but, "Настройки", self.but_size)

    def draw(self):
        pos_of_mouse = pg.mouse.get_pos()
        for num in range(len(self.buts)):
            # Проверка на наведение курсора, и на то, что это первый кадр, когда курсор на кнопке
            if self.buts[num].is_down != self.buts[num].is_but_down(pos_of_mouse) and \
                    self.buts[num].is_but_down(pos_of_mouse):
                self.audio.Sound_play(self.audio.sound_when_cursor_under_button)
            self.buts[num].draw()


    def but_init(self, x, y, text, size):
        self.buts.append(Button(size, x, y, self.audio))
        l = len(self.buts)
        self.buts[l - 1].Text = text
        self.y_but += int(0.7 * size)


class Button():
    def __init__(self, size, x, y, audio):
        """
        Это конструктор класса кнопок.
        :param size: ширина кнопки.
        :param x и y: Координаты центра кнопки.
        :param audio: обьект, делающий звук.
        """
        self.size_of_font = 30
        self.size = size
        self.Text = "Введите текст"
        self.y = y
        self.x = x
        self.COLOR = BACK_LOAD
        self.audio = audio
        self.is_down = 0

    def draw(self):
        """
        Рисует кнопку.
        :param x и y: Координаты центра кнопки.
        :return: кнопку на экране.
        """
        x = self.x
        y = self.y
        a = int(self.size / 2)
        pg.draw.arc(sc, self.COLOR,
                    (x - 3*a, y - a/2, 6 * a, a),
                    0, 2 * pi, 13)
        font = pg.font.Font(None, self.size_of_font)  # Задает шрифт.
        text = font.render(self.Text, True, (255, 255, 255))
        # Добавляет текст на кнопку на координатах x, y.
        sc.blit(text, [x - int(1.5 * self.size_of_font), y - int(self.size_of_font / 3)])

    def is_but_down(self, massive):
        """
        Проверяет, наведена ли мышь на кнопку
        :param massive: Массив координат мыши.
        :return: 1, если мышь нажата, иначе 0.
        """
        a = int(self.size / 2)
        if self.y - a/2 < massive[1] < self.y + a/2 and \
                W//2 - 3*a < massive[0] < W//2 + 3*a:
            self.COLOR = BUT_LOAD
            self.is_down = 1
            return 1
        else:
            self.COLOR = BACK_LOAD
            self.is_down = 0
            return 0


class Load_cicle():
    """
    Это класс обьекта, являющегося индификатором процесса загрузки.
    """
    def __init__(self):
        self.persent_of_load = 0
        self.scale = 1
        self.size = 150
        self.size_of_font = 30

    def draw_cicle(self, x, y):
        """
        Рисует шкалу загрузки.
        :param x и y: Координаты центра экрана, на котором рисуется шкала.
        :return: шкалу загрузки на экране.
        """

        r = int(self.size/2)
        pg.draw.arc(sc, GREEN_LOAD,
                    (x - r, y - r, 2 * r, 2 * r),
                    0, 2 * pi * self.persent_of_load/100, 13)
        font = pg.font.Font(None, self.size_of_font)  # Задает шрифт.
        text = font.render(str(int(self.persent_of_load)) + "%", True, (255, 255, 255))
        # Добавляет текст на шкалу на координатах x, y.
        sc.blit(text, [x - self.size_of_font/3, y - self.size_of_font/3])

    def draw_all_load(self):
        """
        Меняет цвет фона и рисует процесс загрузки.
        :return: фон, процесс загрузки.
        """
        pg.draw.rect(sc, BACK_LOAD, (0, 0, W, H), 0)
        self.draw_cicle(W//2, H//2)

    def main_menu_init(self):
        """
        Запускает главное меню и загружает все, что необходимо для работы игры в переменные.
        Паралельно отрисовывает процесс загрузки.
        :return: Главное меню и процесс его загрузки.
        """
        count = 5
        part = int(1 / count * 100)
        self.draw_all_load()  # 0
        pg.display.update()

        self.LK = pg.image.load('Textures\ЛК.jpg')  # 1
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

        self.menu = Menu(self.audio)  # 4
        self.persent_of_load += part
        self.draw_all_load()
        pg.display.update()

        self.audio.sounf_if_button_down_init()  # 5
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


def test():
    W = 400
    H = 300

    sc = pg.display.set_mode((W, H))
    sc.fill((100, 150, 200))

    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()

        pg.time.delay(20)


if __name__ == '__main__':
    print("Этот модуль не для отдельного использования.\nВключен режим тестирования модуля")

    sc = pg.display.set_mode((W, H))
    sc.fill((100, 150, 200))
    pg.init()

    laod = Load_cicle()

    laod.main_menu_init()

    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
        sc.blit(laod.LK, (0, -100))
        # but.is_but_down(pg.mouse.get_pos())
        # but.draw()
        laod.menu.draw()
        # laod.draw_all_load()
        # laod.persent_of_load += 1
        pg.time.delay(60)
        pg.display.update()



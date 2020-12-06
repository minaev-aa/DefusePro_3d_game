import pygame as pg
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
        self.but_init(self.W // 2, self.y_but, "Подключиться", self.but_size)
        self.but_init(self.W // 2, self.y_but, "Создать свой сервер", self.but_size)
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
        font = pg.font.Font(None, self.size_of_font)  # Задает шрифт.
        text = font.render(self.Text, True, (255, 255, 255))
        # Добавляет текст на кнопку на координатах x, y.
        sc.blit(text, [x - int((len(self.Text) / 2) * self.size_of_font // 3),
                       y - int(self.size_of_font / 3)])

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
                    self.opposite_persent_of_load, 2 * self.pi * self.persent_of_load / 100, 13)
        font = pg.font.Font(None, self.size_of_font)  # Задает шрифт.
        text = font.render(str(int(self.persent_of_load)) + "%", True, (255, 255, 255))
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
        count = 12
        self.persent_of_load = 0
        self.draw_all_load()  # 0 - номер процедуры подгрузки.
        pg.display.update()

        self.LK = pg.image.load('Resources\Textures\ЛК.jpg')  # 1
        self.__upd__main_load(count)

        self.audio = Audio_source()  # 2
        self.__upd__main_load(count)

        self.menu = Menu(self.audio, self.sc)  # 3
        self.__upd__main_load(count)

        Dict_of_audio_inits = {self.audio.sound_when_cursor_under_button_init(): '1',
                               self.audio.sound_if_button_down_init(): '2',
                               self.audio.steps_init():  '3',
                               self.audio.running_init(): '4',
                               self.audio.plus_anything_init(): '5',
                               self.audio.shortness_init(): '6',
                               self.audio.exhalation_init(): '7',
                               self.audio.checkpoint_init(): '8'}
        # Инициализация звуков.
        for num in range(len(Dict_of_audio_inits)):  # 4 - 11
            Dict_of_audio_inits.get(str(num))
            self.__upd__main_load(count)

        file = open('Resources\Sets_saves\sets.txt', 'r')  # 12
        Sets = file.readlines()
        self.audio.is_sounds_on = int(Sets[0].split()[0])
        file.close()
        self.__upd__main_load(count)
        # Помни, что нужно увеличить count, если добавил процедур загрузки.

        # Массив звуков.
        self.Audios = [self.audio.steps,
                       self.audio.running,
                       self.audio.plus_anythings,
                       self.audio.sound_when_cursor_under_button,
                       self.audio.sound_if_button_down,
                       self.audio.shortness,
                       self.audio.exhalation,
                       self.audio.checkpoint]

        # Массив начал игры звука.
        self.steps_starts = [self.audio.steps_start_time,
                          self.audio.running_start_time,
                          self.audio.plus_anything_start_time,
                          self.audio.sound_when_cursor_under_button_start_time,
                          self.audio.sound_if_button_down_start_time,
                          self.audio.shortness_start_time,
                          self.audio.exhalation_start_time,
                          self.audio.checkpoint_start_time]

        # Массив длительностей звуков.
        self.durations = [steps_duration,
                          running_duration,
                          plus_anything_duration,
                          sound_when_cursor_under_button_duration,
                          sound_if_button_down_duration,
                          shortness_duration,
                          exhalation_duration,
                          checkpoint_duration]

    def __upd__main_load(self, count):
        """
        Process of load.
        """
        self.persent_of_load += 1 // count
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

    def main(self):
        """
        Определяет размеры и настроки для окна настроек.
        Здесь можно добавить пунктов настройки фунцией self.setting_point.
        """
        self.x = width_screen // 2
        self.y = height_screen // 2
        self.a = self.size
        self.setting_point('Звук', self.size)

    def draw_set_win(self):
        """
        Рисует окно настроек.
        """
        b = 0.65 * self.a
        c = self.a // 4
        pygame.draw.rect(self.sc, BACK_LOAD, (self.x - self.a, self.y - self.a, 2 * self.a, 2 * self.a), 0)
        pygame.draw.rect(self.sc, Black, (self.x - self.a, self.y - self.a, 2 * self.a, 2 * self.a), 2)
        font = pg.font.Font(None, self.size_of_font)  # Задает шрифт.
        text = font.render('ВЫХОД', True, White)
        # Добавляет текст на нужных координатах x, y.
        self.sc.blit(text, [self.x + b, self.y - b - c])
        text = font.render(' ESC', True, White)
        # Добавляет еще текста сразу под предыдущим.
        self.sc.blit(text, [self.x + b, self.y - b - c + self.size_of_font])
        for num in range(len(self.points)):
            self.points[num].draw()

    def setting_point(self, text, size):
        """
        Добавляет настройку.
        """
        a = int(0.8 * size)
        self.points.append(Points_of_settings(self.sc, 1))
        self.points[len(self.points) - 1].Text = text
        self.points[len(self.points) - 1].x = width_screen // 2 - a
        self.y0 += self.delta
        self.points[len(self.points) - 1].y = self.y0 - a


class Points_of_settings():
    """
    Это класс отдельных настроек для окна настроек.
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

    def is_point_down(self, massive):
        """
        Проверяет, нажали ли на настройку.
        :massive: это массив данных о положении курсора на экране.
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
            try:
                with open("Resources\Sets_saves\sets.txt", 'w') as out_file:
                    out_file.write(str(int(self.parametr)))
            except:
                raise FileNotFoundError("Файл с настройками не найден. Проверьте Resources\Sets_saves\sets.txt")

        return self.parametr


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
    if Loader.persent_of_load > 1:
        print('FAIL/ОШИБКА - Число процедур загрузки больше, чем указано в начале функции.')
    else:
        print("ОК")




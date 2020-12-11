import pygame as pg
from settings import *
import minigames.super_minigame
import random


class game5(minigames.super_minigame.SuperMinigame):
    def __init__(self, Mistake, TimeAll):
        """
        Класс миниигры номер 5.
        """
        minigames.super_minigame.SuperMinigame.__init__(self, screen, TimeAll)
        self.W = width_screen
        self.H = height_screen
        self.mistakes = Mistake
        self.symbols = []
        self.len_of_alpabet = 27
        # Подтянем текстуры кнопок.
        for num in range(self.len_of_alpabet):
            slash = "\ "
            self.symbols.append(pg.image.load('Resources\Textures\minigame5' + slash[0] + str(num + 1) + '.png'))
        # Создадим массив столбцов, где символы - номера картинок, соответвующих им.
        # ( В массиве номер на один меньше, тк счет идет с нуля).
        self.columns = [(1, 2, 3, 4, 5, 6, 7),
                        (8, 1, 7, 9, 10, 6, 11),
                        (12, 13, 9, 14, 15, 3, 10),
                        (16, 17, 18, 5, 14, 11, 19),
                        (20, 19, 18, 21, 17, 22, 23),
                        (16, 8, 24, 27, 20, 25, 26)]
        self.but_x = 230  # Координата Х опорной точки первой кнопки.
        self.but_y = 415  # Координата У опорной точки первой кнопки.
        self.deltaY = 185  # Расстояние между кнопками по координате Y.
        self.deltaX = 185  # Расстояние между кнопками по координате X.

        self.display_x = 350  # Координата X опорной точки экрана вывода символов.
        self.display_y = 100  # Координата У опорной точки экрана вывода символов.
        self.delta_disp = 100  # Расстояние между элементами на экране вывода по координате X.
        self.underline_size = 10  # Толщина подчеркивания кнопок управления при наведении курсора на них.

        # Координата верхнего левого конца нижней кнопки управления.
        # (Стирание и проверка верхности ответа).
        self.x_but_of_disp = 807
        self.y_but_of_disp = 493

        # Расстоние между кнопками управления.
        self.delta_but_on_disp = 145

        # Размер кнопок управления.
        self.size_of_disp_buts = (277, 110)
        self.count_of_symbol = 7
        self.count_of_symbol_on_keyboard = 4
        self.display = pg.image.load('Resources\Textures\minigame5\Display.png')
        self.win = 0  # Параметр правильной выполненности. ( 1 - выиграл, 0 - проиграл).

        self.question_init()

    def draw(self):
        """
        Выводит миниигру на экран.
        """
        self.screen.blit(self.display, (0, 0))  # Нарисуем текстура экрана.
        for but in range(len(self.buts)):
            self.buts[but].draw()  # Нарисуем кнопки.
        self.draw_text_on_display()
        self.draw_time()  # Рисует таймер.
        self.draw_exit()  # Рисует крестик для выхода.

    def draw_text_on_display(self):
        """
        Рисует текст (символы) на диплее.
        num: Номер символа на экране.
        """
        for i in range(len(self.writed_on_display)):
            x = self.display_x + i * self.delta_disp
            y = self.display_y
            self.screen.blit(self.symbols[self.writed_on_display[i] - 1], (x, y))  # Нарисуем символ на экране.

    def main(self):
        self.finished = False
        while not self.finished:
            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                self.time_end()
                self.esc_exit(event)

                if event.type == pygame.QUIT:
                    self.finished = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_exit(mouse_position[0], mouse_position[1])
                    num_of_down_but = self.is_buts_dawn(mouse_position)

                    if num_of_down_but != -1 and len(self.writed_on_display) < self.count_of_symbol_on_keyboard:
                        self.writed_on_display.append(self.elememts[num_of_down_but])

                    if self.is_disp_but_down(mouse_position, 2) and len(self.writed_on_display) > 0:
                        self.writed_on_display.pop()

                    if self.is_disp_but_down(mouse_position, 1) and len(self.writed_on_display) == 4:
                        if self.is_player_lost():
                            self.question_init()
                            self.mistakes += 1
                        else:
                            self.win = 1
                            self.finished = True

            self.draw()
            if self.is_disp_but_down(mouse_position, 1):
                self.draw_underlining_for_disp_buts(Green, 1)
            if self.is_disp_but_down(mouse_position, 2):
                self.draw_underlining_for_disp_buts(DarkRed, 2)

            pygame.time.delay(60)
            pygame.display.update()
        return (self.win, self.mistakes)

    def choose_elements_in_column(self):
        """
        Создает массив номеров кнопок в столбце, который угадывается в игре.
        :ruturn: Массив номеров кнопок в столбце, который угадывается в игре ( номера считаются с 1).
        """
        # Т к все кнопки выбираются случайно из еще не выведенных на экран.
        # Создан массив, который создержит выведенные кнопки.
        used = []
        for num in range(self.count_of_symbol_on_keyboard):
            num_in_massive = random.randint(0, self.count_of_symbol - num - 1)
            used.append(self.choose_element(num_in_massive, used) + 1)
        return used

    def choose_element(self, num, used):
        """
        num - Номер элемента в кортеже елементов столбца.
        used - Массив уже выведенных значений.
        :return: Выводит номер элемента в кортеже элементов столбца, среди еще не выведенных.
         Пример: если (1, 2, 4, 5) - кортеж, num = 1, а элемент 2 уже был выведен (есть в used).
                Тогда функция проверит номер первого элемента 0 != 1, а 1 в used нет =>
                Она пойдет дальше. Пропустит 2, т к она есть в used.
                И вернет 2 - номер второго (num + 1) невыведенного элемента в массиве.
        """
        for el in range(self.count_of_symbol):
            if el + 1 in used:
                num += 1
            if el == num:
                return el

    def give_texture_for_buts(self):
        """
        Создает массив текстур, которые должны быть у кнопок на экране.
        И массив значений, которые этим текстурам соответствуют.
        """
        self.but_textures = []
        self.elememts = []
        for i in range(self.count_of_symbol_on_keyboard):
            self.elememts.append(self.columns[self.num_of_columns - 1][self.elememts_for_buts[i] - 1])
            self.but_textures.append(self.symbols[self.elememts[i] - 1])

    def find_right_answer(self):
        """
        Эта функция ищет массив правильных ответов в этой игре.
        :return: Возращает массив с нужной последовательностью номеров текстур элементов,
                 которые должен ввести игрок.
        """
        not_sorted = []
        answer = []
        for num in range(len(self.elememts_for_buts)):
            not_sorted.append(self.elememts_for_buts[num])
        not_sorted.sort()
        for num in range(len(not_sorted)):
            answer.append(self.columns[self.num_of_columns - 1][not_sorted[num] - 1])
        return answer

    def question_init(self):
        """
        Выбирает задание для игрока.
        """
        # Выбираем стоблец для угадывания.
        self.num_of_columns = random.randint(1, 6)
        # Создадим массив обьектов кнопок.
        self.buts = []
        # Получим случайно сгенерированный массив кнопок.
        self.elememts_for_buts = self.choose_elements_in_column()
        # Переведем их в более удобный массив.
        # Создадим массим текстур для вывода на экран.
        self.give_texture_for_buts()
        self.writed_on_display = []  # Массив элементов на экране в игре.
        self.right_answer = self.find_right_answer()
        # Координаты кнопок в величинах (Строка, Столбец).
        coords = [(1, 1), (2, 1), (1, 2), (2, 2)]
        # Инициализируем кнопки.
        for i in range(self.count_of_symbol_on_keyboard):
            self.button_init(screen, self.but_textures[i], coords[i][0], coords[i][1])

    def button_init(self, screen, texture, line, column):
        """
        Инициализирует кнопку на экране.
        screen: Экран, на котором рисуется игра.
        texture: Текстура кнопки.
        line: Строка на клавиатуре, в которой рисуется кнопка.
        column: Столбец на клавиатуре, в которой рисуется кнопка.
        """
        x = self.but_x + (line - 1) * self.deltaX
        y = self.but_y + (column - 1) * self.deltaY
        self.buts.append(Button(screen, texture, x, y))

    def is_buts_dawn(self, massive):
        """
        Проверяет, есть ди курсор над мышкой, или нет.
        massive: Массив положения мышки.
        return: возравращает номер кнопки, если над кнопками, -1, если нет.
        """
        but_down = -1
        for num in range(len(self.buts)):
            if self.buts[num].is_button_down(massive):
                but_down = num
        return but_down

    def is_disp_but_down(self, massive, line):
        """
        Проверяет, навел ли игрок курсор на доп кнопки.
        :return: 1, если навел и  0, если не навел.
        """
        x = self.x_but_of_disp
        y = self.y_but_of_disp - (line - 1) * self.delta_but_on_disp
        a = self.size_of_disp_buts[0]
        b = self.size_of_disp_buts[1]
        if x <= massive[0] <= x + a and y <= massive[1] <= y + b:
            return 1
        else:
            return 0

    def is_player_lost(self):
        """
        Проверяет, верно ли игрок ввел значения с клавиатуры.
        :return: 1, если ошибся и 0Ю если не ошибся.
        """
        mistakes = 0
        for i in range(self.count_of_symbol_on_keyboard):
            if self.writed_on_display[i] != self.right_answer[i]:
                mistakes += 1
        if mistakes > 0:
            return 1
        else:
            return 0

    def draw_underlining_for_disp_buts(self, colour, line):
        """
        Рисует обводку вокруг кнопок.
        """
        pg.draw.rect(screen, colour, (self.x_but_of_disp,
                                      self.y_but_of_disp - self.delta_but_on_disp * (line - 1),
                                      self.size_of_disp_buts[0],
                                      self.size_of_disp_buts[1]),
                     self.underline_size)


class Button():
    def __init__(self, screen, texture, x, y):
        """
        Инициализация класса кнопок клавиутуры.
        """
        self.texture = texture
        self.screen = screen
        self.x = x  # Координаты верней левой точки.
        self.y = y  # Координаты верней левой точки.
        self.size = 90

    def draw(self):
        """
        Рисует кнопки.
        """
        self.screen.blit(self.texture, (self.x, self.y))

    def is_button_down(self, massive):
        """
        Проверяет, наведет ли курсор на кнопку.
        massive: Массив положения мышки.
        return: возравращает 1, если над кнопками, 0, если нет.
        """
        if self.x <= massive[0] <= self.x + self.size and \
                self.y <= massive[1] <= self.y + self.size:
            return 1
        else:
            return 0


if __name__ == '__main__':
    print("Этот модуль не для отдельного использования. \nВключен режим тестрования модуля.")
    pg.init()
    screen = pg.display.set_mode((width_screen, height_screen))
    screen.fill((100, 150, 200))
    TimeAll = time.time()
    g = game5(0, TimeAll)

    # Проверим функцию choose_elements_in_column()
    errors = 0
    print("Проверка функции choose_elements_in_column()")
    massive = g.choose_elements_in_column()
    for i in range(100):
        for num_of_el in range(len(massive)):
            # Проверим границы значений.
            if 0 > massive[num_of_el] > 8:
                print("Ошибка в границах номеров должный быть цифры с 1 по 7.")
                errors += 1
            # Проверим верность типа вывода функции.
            try:
                int(massive[num_of_el])
            except:
                print("Элементы должны быть INT.")
                errors += 1
            if int(massive[num_of_el]) != massive[num_of_el]:
                print("Элементы должны быть целыми (INT).")
                errors += 1

            # Проверим, повтряется ли функция (не должна).
            coincidences = 0
            for num_of_el2 in range(len(massive)):
                if num_of_el != num_of_el2:
                    if massive[num_of_el] == massive[num_of_el2]:
                        coincidences += 1
                        errors += 1
            if coincidences > 0:
                print("Выбор элементов работает неверно.")

    print("Ошибок с функцией choose_elements_in_column() необнаружено.")

    g.main()

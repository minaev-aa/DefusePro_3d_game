import pygame as pg
import sys


class Audio_source():
    def __init__(self):
        """
        Этот обьект делает звук.
        """
        self.background_volume = 1  # Уровень громкости фона.
        self.volume = 1  # Уровень громкости звуков.
        self.step_of_init = 0  # степень подгрузки данных.
        self.is_background_music_on = 1  # Проверка на включенность фоновой мелодии.
        self.is_sounds_on = 1  # Проверка на включенность звуков.
        self.count_of_sound_effects = 8  # Количество шагов подгрузки данных.

        # Проверим работу подсчета данных для реализации окна загрузки игры.
        assert self.step_of_init == 1  # Изменено кол-во данных в модуле звуков и мелодий,\
        # нарушена работа подсчета этих данных.

    # Инициализация звуковых эффектов.
    def steps_init(self):
        self.steps = pg.mixer.Sound('Music_and_sound\Format_ogg\шаги - 2.ogg')
        self.step_of_init += 1 / self.count_of_sound_effects

    def running_init(self):
        self.running = pg.mixer.Sound('Music_and_sound\Format_ogg\Бег - 6 шагов.ogg')
        self.step_of_init += 1 / self.count_of_sound_effects

    def plus_anything_init(self):
        self.plus_anythings = pg.mixer.Sound('Music_and_sound\Format_ogg\плюс чего-то.ogg')
        self.step_of_init += 1 / self.count_of_sound_effects

    def sound_when_cursor_under_button_init(self):
        self.sound_when_cursor_under_button = pg.mixer.Sound('Music_and_sound\Format_ogg\Курсор_на_кнопке.ogg')
        self.step_of_init += 1 / self.count_of_sound_effects

    def sounf_if_button_down_init(self):
        self.sounf_if_button_down = pg.mixer.Sound('Music_and_sound\Format_ogg\Нажатие_на_кнопку.ogg')
        self.step_of_init += 1 / self.count_of_sound_effects

    def shortness_init(self):
        self.shortness = pg.mixer.Sound('Music_and_sound\Format_ogg\Отдышка.ogg')
        self.step_of_init += 1 / self.count_of_sound_effects

    def exhalation_init(self):
        self.exhalation = pg.mixer.Sound('Music_and_sound\Format_ogg\Довольный выдох.ogg')
        self.step_of_init += 1 / self.count_of_sound_effects

    def checkpoint_init(self):
        self.checkpoint = pg.mixer.Sound('Music_and_sound\Format_ogg\Чекпоинт.ogg')
        self.step_of_init += 1 / self.count_of_sound_effects

    def Sound_play(self, Audio):
        """
        Включает звук.
        :param Audio: переменная, в которой лежит звук, который необходимо включить.
        :return:  Включение звука, если это разрешено в настройках игры.
        """
        if self.is_sounds_on:  # Проверка на включение звуков в настройках игры.
            Audio.play()

    def Background_music_on_AfraidSound(self):
        """
        Меняет фоновый звук на керамический гул, если включен фоновый звук в настройках.
        :return: Смена фонового звука, если он включен в настройках.
        """
        if self.is_background_music_on:
            pg.mixer.music.load('Music_and_sound\Format_ogg\страшный гул.ogg')
            pg.mixer.music.play(-1)
            pg.mixer.music.set_volume(self.background_volume * 0.8)


def test(obj, obj1):
    """
    Функция для проверки корректности работы класса.
    :param obj: переменная со звуком, который можно будет включить по левой кнопке мыши.
    :return:  включит звук по левой кнопке мыши.
    """
    # pg.mixer.music.load('Music_and_sound\Format_ogg\страшный гул.ogg')
    # pg.mixer.music.play(-1)

    sound1 = pg.mixer.Sound('Music_and_sound\Format_ogg\шаги - 2.ogg')
    sound2 = pg.mixer.Sound('Music_and_sound\Format_ogg\Бег - 6 шагов.ogg')

    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()

            elif i.type == pg.KEYUP:
                if i.key == pg.K_1:
                    pg.mixer.music.pause()
                    # pygame.mixer.music.stop()
                elif i.key == pg.K_2:
                    pg.mixer.music.unpause()
                    # pygame.mixer.music.play()
                    pg.mixer.music.set_volume(0.1)
                elif i.key == pg.K_3:
                    pg.mixer.music.unpause()
                    # pygame.mixer.music.play()
                    pg.mixer.music.set_volume(1)

            elif i.type == pg.MOUSEBUTTONUP:
                if i.button == 1:
                    obj.play()
                elif i.button == 3:
                    obj1.play()

        pg.time.delay(20)


if __name__ == '__main__':
    print("Эта функция позволяет оценить работу модуля звука "
          " и разобраться в работе функций фонового звука и сторонних звуков.")

    pg.init()
    sc = pg.display.set_mode((400, 300))

    object1 = Audio_source()
    test(object1.plus_anythings, object1.sound_when_cursor_under_button)

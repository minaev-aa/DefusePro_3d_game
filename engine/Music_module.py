import pygame as pg
import sys
import time


class Audio_source():
    def __init__(self):
        """
        Этот обьект инициализирует звук.
        self.is_sounds_on             Проверка на включенность звуков.
        steps_init()
        sound_when_cursor_under_button_init()
        sound_if_button_down_init()
        Sound_play(Audio, duration, start_time)
        """
        self.is_sounds_on = 1  # Проверка на включенность звуков.

    # Инициализация звуковых эффектов.
    def steps_init(self):
        self.steps = pg.mixer.Sound('Resources\Music_and_sound\Format_ogg\Steps.ogg')
        self.steps_start_time = 0

    def sound_when_cursor_under_button_init(self):
        self.sound_when_cursor_under_button = pg.mixer.Sound('Resources\Music_and_sound\Format_ogg\Cursor_under_button.ogg')
        self.sound_when_cursor_under_button_start_time = 0

    def sound_if_button_down_init(self):
        self.sound_if_button_down = pg.mixer.Sound('Resources\Music_and_sound\Format_ogg\Button_down.ogg')
        self.sound_if_button_down_start_time = 0

    def Sound_play(self, Audio, duration, start_time):
        """
        Включает звук.
        :param Audio: переменная, в которой лежит звук, который необходимо включить.
        :return:  Включение звука, если это разрешено в настройках игры, время старта.
        """
        if self.is_sounds_on:  # Проверка на включение звуков в настройках игры.
            if start_time + duration <= time.time():
                Audio.play()

    def check_sound(self, duration, start_time):
        """
        Проверяет возможность включения звука.
        :param Audio: переменная, в которой лежит звук, который необходимо включить.
        :param duration: Длительность звука.
        :param start_time: Последнее время включения.
        :return: Новое время старта.
        """
        if self.is_sounds_on:  # Проверка на включение звуков в настройках игры.
            if start_time + duration <= time.time():
                start_time = time.time()

        return start_time


def test(obj, obj1):
    """
    Функция для проверки корректности работы класса.
    :param obj: переменная со звуком, который можно будет включить по левой кнопке мыши.
    :return:  включит звук по левой кнопке мыши.
    """
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
    object1.sound_if_button_down_init()
    object1.sound_if_button_down_init()
    test(object1.sound_if_button_down, object1.sound_if_button_down)

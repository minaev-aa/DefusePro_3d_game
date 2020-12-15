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
        self.sound_when_cursor_under_button = pg.mixer.Sound(
                'Resources\Music_and_sound\Format_ogg\Cursor_under_button.ogg')
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
        # Проверка на включение звуков в настройках игры.
        if self.is_sounds_on and start_time + duration <= time.time():
            Audio.play()

    def check_sound(self, duration, start_time):
        """
        Проверяет возможность включения звука.
        :param Audio: переменная, в которой лежит звук, который необходимо включить.
        :param duration: Длительность звука.
        :param start_time: Последнее время включения.
        :return: Новое время старта.
        """
        # Проверка на включение звуков в настройках игры.
        if self.is_sounds_on and start_time + duration <= time.time():
            start_time = time.time()

        return start_time



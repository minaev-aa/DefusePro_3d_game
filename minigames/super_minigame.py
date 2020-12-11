import time
import pygame
from settings import *


class SuperMinigame():
    def __init__(self, screen, TimeAll):
        self.screen = screen
        self.Time = Time
        self.font = pygame.font.SysFont(None, 100)
        self.text = self.font.render(str(self.Time) + ' сек', True, Black)  # Текст таймера.
        self.finished = False
        self.TimeAll = TimeAll

    def text_box(self, text, color_text, size_text, color_rect, top, size):
        """
        Рисует окошко с текстом посередине.

        @param text: текст
        @type text: str
        @param color_text: цвет текста
        @type color_text: RGB (int, int, int)
        @param size_text: размер шрифта
        @type size_text: int
        @param color_rect: цвет окоша
        @type color_rect: RGB (int, int, int)
        @param top: Верхняя левая вершина
        @type top: (int, int)
        @param size: Размер: (ширина, высота)
        @type size: (int, int)
        """
        pygame.draw.rect(self.screen, color_rect, (top, size))
        font = pygame.font.SysFont('serif', size_text)
        text2 = font.render(text, 1, color_text)
        rect = text2.get_rect(center=((top[0] + size[0] // 2), (top[1] + size[1] // 2)))
        self.screen.blit(text2, rect)

    def draw_exit(self):
        """
        Рисует крестик выхода.
        """
        button = pygame.image.load('Resources\\Textures\\button.png')
        surf4 = pygame.Surface((50, 50))
        surf4.blit(button, (0, 0))
        self.screen.blit(surf4, (width_screen - 60, 0))

    def draw_time(self):
        """
        Рисует таймер
        """
        self.text = self.font.render(str(self.Time) + ' сек', True, Black)
        surf1 = pygame.Surface((300, 120))
        surf1.fill(White)
        text_rect = self.text.get_rect(center=surf1.get_rect().center)
        self.text = self.font.render(str(self.Time - round(time.time() - self.TimeAll)) + ' сек', True, Black)
        surf1.fill(White)
        surf1.blit(self.text, text_rect)
        self.screen.blit(surf1, (0, 0))

    def time_end(self):
        """
        Если время вышло, то выключает миниигру.
        """
        if self.Time - round(time.time() - self.TimeAll) == 0:
            self.finished = True

    def click_exit(self, x, y):
        '''
        Проверка нажатия на кнопку выхода
        '''
        if 1140 < x < 1190:
            if 0 < y < 50:
                self.finished = True

    def esc_exit(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.finished = True

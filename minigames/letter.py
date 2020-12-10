import pygame
from settings import *

pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))


class Letter:
    '''
    Класс рисования подсказок
    sc :param определяет экран на котором рисуют
    Time :param время в игре таймер
    num :param номер подсказки
    '''

    def __init__(self, sc, num):
        self.sc = sc
        self.textures = {'o': pygame.image.load('Resources/Textures/game1.png').convert(),
                         'd': pygame.image.load('Resources/Textures/game2.png').convert(),
                         't': pygame.image.load('Resources/Textures/game3.png').convert(),
                         'c': pygame.image.load('Resources/Textures/game4.png').convert(),
                         'p': pygame.image.load('Resources/Textures/game5.png').convert(),
                         }
        self.Time = Time
        self.x, self.y = 0, 0
        self.num = num
        self.font = pygame.font.SysFont(None, 100)
        self.text = self.font.render(str(self.Time) + ' сек', True, Black)

    def click(self):
        '''
        :return: Проверка на попадание по кнопке выхода
        '''
        if 1140 < self.x < 1190:
            if 0 < self.y < 50:
                return True

    def draw(self):
        '''
        :return: Рисует подсказку, кнопку, и таймер
        '''
        finished = False
        self.sc.fill(White)
        self.text = self.font.render(str(self.Time) + ' сек', True, Black)
        surf1 = pygame.Surface((300, 120))
        surf1.fill(White)
        button = pygame.image.load('Resources\\Textures\\button.png')
        surf2 = pygame.Surface((800, 800))
        surf2.blit(self.textures[self.num], (0, 0))
        self.sc.blit(surf2, (299, 0))
        surf4 = pygame.Surface((50, 50))
        surf4.blit(button, (0, 0))
        self.sc.blit(surf4, (width_screen - 60, 0))
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.MOUSEMOTION:
                    self.x, self.y = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.click():
                        finished = True
            self.text = self.font.render(str(self.Time - round(time.time()-TimeAll)) + ' сек', True, Black)
            if self.Time - round(time.time()-TimeAll) == 0:
                finished = True
            text_rect = self.text.get_rect(center=surf1.get_rect().center)
            surf1.fill(White)
            surf1.blit(self.text, text_rect)
            self.sc.blit(surf1, (0, 0))
            pygame.display.update()


if __name__ == '__main__':
    Letter(screen, 'o').draw()

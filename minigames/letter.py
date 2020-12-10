import pygame
from minigames.super_minigame import *
from settings import *

pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))


class Letter(SuperMinigame):
    '''
    Класс рисования подсказок
    sc :param определяет экран на котором рисуют
    Time :param время в игре таймер
    num :param номер подсказки
    '''

    def __init__(self, sc, num):
        super().__init__(screen)
        self.sc = sc
        self.textures = {'o': pygame.image.load('Resources/Textures/game1.png').convert(),
                         'd': pygame.image.load('Resources/Textures/game2.png').convert(),
                         't': pygame.image.load('Resources/Textures/game3.png').convert(),
                         'c': pygame.image.load('Resources/Textures/game4.png').convert(),
                         'p': pygame.image.load('Resources/Textures/game5.png').convert(),
                         }
        self.x, self.y = 0, 0
        self.num = num

    def draw(self):
        '''
        :return: Рисует подсказку, кнопку, и таймер
        '''
        self.sc.fill(White)
        surf2 = pygame.Surface((800, 800))
        surf2.blit(self.textures[self.num], (0, 0))
        self.sc.blit(surf2, (299, 0))
        self.draw_exit()
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                if event.type == pygame.MOUSEMOTION:
                    self.x, self.y = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_exit(self.x, self.y)
            if self.Time - round(time.time()-TimeAll) == 0:
                self.finished = True
            self.draw_time()
            pygame.display.update()


if __name__ == '__main__':
    Letter(screen, 'o').draw()

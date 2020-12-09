import pygame
from settings import *
import time

pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))


class game2:
    '''
    Класс второй минии игры - кнопка
    sn :param серийный номер
    Mistake :param количество ошибок
    '''
    def __init__(self, sn, Mistake):
        self.sc = screen
        self.textures = pygame.image.load('Resources/Textures/tex6X6.png').convert()
        self.Time = Time
        self.x, self.y = 0, 0
        self.font = pygame.font.SysFont(None, 100)
        self.text = self.font.render(str(self.Time) + ' сек', True, Black)
        self.describe = (random.choices(['Detonate', '   Hold', '  Abort', '  Boom', ' Defuse']))[0]
        self.colorb = (random.choices([Blue, Red, White, Black, Yellow]))[0]
        self.colorl = (random.choices([Blue, Red, White, Black, Yellow]))[0]
        self.sn = sn
        self.localtime = 0
        self.mistakes = Mistake
        self.finished = False
        self.correct = 0
        self.surf2 = pygame.Surface((800, 800))
        self.holds = 0

    def click(self):
        '''
        :return: проверка нажатия на кнопку выхода
        '''
        if 1140 < self.x < 1190:
            if 0 < self.y < 50:
                return True

    def right(self):
        '''
        :return: Проверка последовательности действий
        '''
        pygame.draw.rect(screen, self.colorl, (350, 250, 50, 300))
        pygame.display.update()
        if (self.colorb == Blue and self.describe == '  Abort') or (self.sn % 2 == 1 and self.colorb == White) or (
                    self.colorb == Yellow):
            self.holds = 1
        if (self.sn % 2 == 0 and self.describe == 'Detonate') or (self.describe == '   Hold' and self.colorb == Red):
            self.holds = 2
        else:
            if self.localtime + 2 < int(time.time()):
                self.holds = 1
            else:
                self.mistake()

    def mistake(self):
        '''
        :return: Добавление ошибки
        '''
        self.mistakes += 1

    def check(self, n):
        '''
        :param n: определение соответствия последней цифры таймера
        :return:
        '''
        timet = Time - round(time.time()-TimeAll)
        if ((timet - (timet % 100) - (timet % 10)) / 100) == n or (
            ((timet % 100) - (timet % 10)) / 10) == n or (timet % 10) == n:
            self.finished = True
            self.correct = 1
        else:
            self.mistake()

    def hold(self):
        '''
        :return: Удержание кнопки, проверка дальнейших условий
        '''
        if self.colorl == Blue:
            self.check(4)
        elif self.colorl == White:
            self.check(1)
        elif self.colorl == Yellow:
            self.check(5)
        else:
            self.check(1)

    def draw(self):
        '''
        :return: Отрисовка миниигры, кнопки и таймера
        '''
        self.sc.fill(White)
        self.text = self.font.render(str(self.Time) + ' сек', True, Black)
        surf1 = pygame.Surface((300, 120))
        surf1.fill(White)
        button = pygame.image.load('Resources\\Textures\\button.png')
        self.surf2.fill(White)
        pygame.draw.rect(self.surf2, Grey, (0, 200, 600, 400))
        pygame.draw.circle(self.surf2, self.colorb, (400, 400), 150)
        f2 = pygame.font.SysFont('serif', 48)
        text = f2.render(self.describe, False,
                         (0, 180, 0))
        pygame.draw.rect(self.surf2, Grey, (50, 250, 50, 300))
        self.surf2.blit(text, (320, 365))
        self.sc.blit(self.surf2, (300, 0))
        surf4 = pygame.Surface((50, 50))
        surf4.blit(button, (0, 0))
        self.sc.blit(surf4, (width_screen - 60, 0))
        while not self.finished:
            timet = Time - round(time.time()-TimeAll)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                if event.type == pygame.MOUSEMOTION:
                    self.x, self.y = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.click():
                        self.finished = True
                    else:
                        if (590 < self.x < 790) and (300 < self.y < 492):
                            self.localtime = timet
                            self.right()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.holds == 1:
                        if self.localtime > timet + 2:
                            self.hold()
                        else:
                            self.mistake()
                    if self.holds == 2:
                        if self.localtime < timet + 2:
                            self.finished = True
                            self.correct = 1
                        else:
                            self.mistake()
            self.text = self.font.render(str(self.Time - round(time.time()-TimeAll)) + ' сек', True, Black)
            if self.Time - round(time.time()-TimeAll) == 0:
                print(self.Time, self.localtime)
                self.finished = True
            text_rect = self.text.get_rect(center=surf1.get_rect().center)
            surf1.fill(White)
            surf1.blit(self.text, text_rect)
            self.sc.blit(surf1, (0, 0))
            pygame.display.update()
        return (self.correct, self.mistakes)


if __name__ == '__main__':

    print(game2(sn, Mistake).draw())  # Изменяет время и количество ошибок гловально. Выдаёт статус задания 1 значит выполнено

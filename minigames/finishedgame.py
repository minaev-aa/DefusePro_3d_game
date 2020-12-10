from settings import *
from minigames.super_minigame import *


pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))


class fingame(SuperMinigame):
    '''
    Класс рисования текстур
    '''

    def __init__(self, n):
        super().__init__(screen)
        self.n = n
        self.sc = screen
        self.x, self.y = 0, 0

    def draw(self):
        '''
        :return: Рисует подсказку, кнопку, и таймер
        '''
        self.sc.fill(White)
        f2 = pygame.font.SysFont('serif', 80)
        if self.n == 0:
            text1 = f2.render('Задание успешно выполнено', False, Black)
            self.draw_exit()
        if self.n == 1:
            text1 = f2.render('Вы проигали', False, Black)
        if self.n == 2:
            text1 = f2.render('Вы Победили', False, Black)
        self.sc.blit(text1, (100, 330))
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                if event.type == pygame.MOUSEMOTION:
                    self.x, self.y = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.n == 0:
                        self.click_exit(self.x, self.y)
            if self.n == 0:
                self.draw_time()
                if self.Time - round(time.time() - TimeAll) == 0:
                    self.finished = True
            pygame.display.update()


if __name__ == '__main__':
    fingame(0).draw()

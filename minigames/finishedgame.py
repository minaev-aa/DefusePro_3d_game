from settings import *

pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))


class fingame():
    '''
    Класс рисования текстур
    '''

    def __init__(self):
        self.sc = screen
        self.Time = Time
        self.x, self.y = 0, 0
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
        f2 = pygame.font.SysFont('serif', 80)
        text1 = f2.render('Задание успешно выполнено', False, Black)
        self.sc.blit(text1, (100, 330))
        surf1.fill(White)
        button = pygame.image.load('Resources\\Textures\\button.png')
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
            self.text = self.font.render(str(self.Time - round(time.time() - TimeAll)) + ' сек', True, Black)
            if self.Time - round(time.time() - TimeAll) == 0:
                finished = True
            text_rect = self.text.get_rect(center=surf1.get_rect().center)
            surf1.fill(White)
            surf1.blit(self.text, text_rect)
            self.sc.blit(surf1, (0, 0))
            pygame.display.update()


if __name__ == '__main__':
    fingame().draw()

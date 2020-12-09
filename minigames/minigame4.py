from settings import *

pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))


class game4:
    '''
    Класс второй минии игры - кнопка
    Mistake :param количество ошибок
    '''
    def __init__(self, Mistake):
        self.sc = screen
        self.n = 1
        self.Time = Time
        self.x, self.y = 0, 0
        self.font = pygame.font.SysFont(None, 100)
        self.text = self.font.render(str(self.Time) + ' сек', True, Black)
        self.t = (random.choices(['1', '2', '3', '4']))[0]
        self.code = ['1', '2', '3', '4']
        self.num = []
        self.znach = []
        self.mistakes = Mistake
        self.finished = False
        self.correct = 0
        self.surf2 = pygame.Surface((800, 800))

    def click(self):
        '''
        :return: проверка нажатия на кнопку выхода
        '''
        if 1140 < self.x < 1190:
            if 0 < self.y < 50:
                return True
        if 350 < self.x < 545:
            if 400 < self.y < 500:
                return '1'
        if 350 < self.x < 545:
            if 520 < self.y < 620:
                return '3'
        if 555 < self.x < 750:
            if 400 < self.y < 500:
                return '2'
        if 555 < self.x < 750:
            if 520 < self.y < 620:
                return '4'

    def mistake(self):
        '''
        :return: Добавление ошибки
        '''
        self.num.clear()
        self.n = 0
        self.znach.clear()
        pygame.draw.rect(self.surf2, White, (475, 200, 100, 420))
        self.sc.blit(self.surf2, (300, 0))
        self.mistakes += 1

    def right(self):
        '''
        :return: Проверка на правильность выбоа. Отрисовка номера раунда
        '''
        if self.n == 1:
            if (int(self.num[0]) == 2) and (int(self.t) == 1):
                pygame.draw.rect(self.surf2, Green, (485, 535, 80, 50))
                self.sc.blit(self.surf2, (300, 0))
            elif int(self.num[0]) == int(self.t):
                pygame.draw.rect(self.surf2, Green, (485, 535, 80, 50))
                self.sc.blit(self.surf2, (300, 0))
            else:
                self.mistake()
        if self.n == 2:
            if ((int(self.znach[1]) == 4) and (int(self.t) == 1)) or (
                        (int(self.num[1]) == int(self.num[0])) and (int(self.t) in [2, 4])) or (
                        (int(self.num[1]) == 1) and (int(self.t) == 3)):
                pygame.draw.rect(self.surf2, Green, (485, 535, 80, 50))
                pygame.draw.rect(self.surf2, Green, (485, 460, 80, 50))
                self.sc.blit(self.surf2, (300, 0))
            else:
                self.mistake()
        if self.n == 3:
            if ((int(self.znach[2]) == int(self.znach[1])) and (int(self.t) == 1)) or (
                        (int(self.znach[2]) == int(self.znach[0])) and (int(self.t) == 2)) or (
                            (int(self.num[2]) == 3) and (int(self.t) == 3) or (int(self.znach[2]) == 4) and (
                                int(self.t) == 4)):
                pygame.draw.rect(self.surf2, Green, (485, 385, 80, 50))
                pygame.draw.rect(self.surf2, Green, (485, 535, 80, 50))
                pygame.draw.rect(self.surf2, Green, (485, 460, 80, 50))
                self.sc.blit(self.surf2, (300, 0))
            else:
                self.mistake()
        if self.n == 4:
            if ((int(self.num[3]) == int(self.num[0])) and (int(self.t) == 1)) or (
                        (int(self.num[3]) == 1) and (int(self.t) == 2)) or (
                        (int(self.num[3]) == int(self.num[1])) and (int(self.t) in [3, 4])):
                pygame.draw.rect(self.surf2, Green, (485, 385, 80, 50))
                pygame.draw.rect(self.surf2, Green, (485, 535, 80, 50))
                pygame.draw.rect(self.surf2, Green, (485, 460, 80, 50))
                pygame.draw.rect(self.surf2, Green, (485, 310, 80, 50))
                self.sc.blit(self.surf2, (300, 0))
            else:
                self.mistake()
        if self.n == 5:
            if (int(self.znach[4]) == int(self.znach[int(self.t) - 1]) and int(self.t) in [1, 2]) or (
                        (int(self.znach[4]) == int(self.znach[3])) and int(self.t) == 3) or (
                        (int(self.znach[4]) == int(self.znach[2])) and int(self.t) == 4):
                pygame.draw.rect(self.surf2, Green, (485, 385, 80, 50))
                pygame.draw.rect(self.surf2, Green, (485, 535, 80, 50))
                pygame.draw.rect(self.surf2, Green, (485, 460, 80, 50))
                pygame.draw.rect(self.surf2, Green, (485, 310, 80, 50))
                pygame.draw.rect(self.surf2, Green, (485, 235, 80, 50))
                self.sc.blit(self.surf2, (300, 0))
            else:
                self.mistake()

    def change(self):
        '''
        :return: Изменение числа на экране
        '''
        pygame.draw.rect(self.surf2, White, (50, 200, 400, 150))
        f = pygame.font.SysFont('serif', 128)
        self.t = (random.choices(['1', '2', '3', '4']))[0]
        text = f.render(self.t, False, Black)
        self.surf2.blit(text, (220, 200))
        self.sc.blit(self.surf2, (300, 0))
        pygame.display.flip()

    def Dall(self):
        '''
        :return: Отрисовка игры. Изменение номеров кнопок
        '''
        self.surf2.fill(White)
        random.shuffle(self.code)
        pygame.draw.rect(self.surf2, Grey, (0, 150, 600, 520))
        pygame.draw.rect(self.surf2, White, (50, 200, 400, 150))
        f2 = pygame.font.SysFont('serif', 64)
        text1 = f2.render(self.code[0], False, Black)
        f3 = pygame.font.SysFont('serif', 64)
        text2 = f3.render(self.code[1], False, Black)
        f4 = pygame.font.SysFont('serif', 64)
        text3 = f4.render(self.code[2], False, Black)
        f5 = pygame.font.SysFont('serif', 64)
        text4 = f5.render(self.code[3], False, Black)
        f = pygame.font.SysFont('serif', 128)
        text = f.render(self.t, False, Black)
        self.surf2.blit(text, (220, 200))
        pygame.draw.rect(self.surf2, White, (475, 200, 100, 420))
        pygame.draw.rect(self.surf2, White, (50, 400, 195, 100))
        pygame.draw.rect(self.surf2, White, (255, 400, 195, 100))
        pygame.draw.rect(self.surf2, White, (50, 520, 195, 100))
        pygame.draw.rect(self.surf2, White, (255, 520, 195, 100))
        self.surf2.blit(text1, (135, 410))
        self.surf2.blit(text2, (335, 410))
        self.surf2.blit(text3, (135, 530))
        self.surf2.blit(text4, (335, 530))
        self.sc.blit(self.surf2, (300, 0))

    def Manager(self):
        '''
        :return: Отрисовка миниигры, кнопки и таймера
        '''
        self.sc.fill(White)
        self.text = self.font.render(str(self.Time) + ' сек', True, Black)
        surf1 = pygame.Surface((300, 120))
        surf1.fill(White)
        self.Dall()
        button = pygame.image.load('Resources\\Textures\\button.png')
        timet = Time - round(time.time() - TimeAll)
        surf4 = pygame.Surface((50, 50))
        surf4.blit(button, (0, 0))
        self.sc.blit(surf4, (width_screen - 60, 0))
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                if event.type == pygame.MOUSEMOTION:
                    self.x, self.y = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.click() in ['1', '2', '3', '4']:
                        self.num.append(self.click())
                        self.znach.append(self.code[int(self.click()) - 1])
                        self.Dall()
                        self.right()
                        self.change()
                        self.n += 1
                    if self.click() == True:
                        self.finished = True
            if self.n == 6:
                self.correct = 1
                self.finished = True
            self.text = self.font.render(str(self.Time - round(time.time() - TimeAll)) + ' сек', True, Black)
            if self.Time - round(time.time() - TimeAll) == 0:
                self.finished = True
            text_rect = self.text.get_rect(center=surf1.get_rect().center)
            surf1.fill(White)
            surf1.blit(self.text, text_rect)
            self.sc.blit(surf1, (0, 0))
            pygame.display.update()
        return (self.correct, self.mistakes)


if __name__ == '__main__':
    print(game4(sn,
                Mistake).Manager())  # Изменяет время и количество ошибок гловально. Выдаёт статус задания 1 значит выполнено

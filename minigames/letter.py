from settings import *
import minigames.super_minigame

pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))


class Letter(minigames.super_minigame.SuperMinigame):
    '''
    Класс рисования подсказок
    :param sc: определяет экран на котором рисуют
    :param TimeAll: время начала игры
    :param num: номер подсказки
    :param  textures: словарь с картинками подсказок
    '''

    def __init__(self, sc, num, TimeAll):
        super().__init__(screen, TimeAll)
        self.sc = sc
        self.textures = {'o': pygame.image.load('Resources/Textures/game1.png').convert(),
                         'd': pygame.image.load('Resources/Textures/game2.png').convert(),
                         't': pygame.image.load('Resources/Textures/game3.png').convert(),
                         'c': pygame.image.load('Resources/Textures/game4.png').convert(),
                         'p': pygame.image.load('Resources/Textures/game5.png').convert(),
                         }
        self.x, self.y = 0, 0
        self.num = num

    def manager(self):
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
                self.esc_exit(event)
                if event.type == pygame.MOUSEMOTION:
                    self.x, self.y = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_exit(self.x, self.y)
            if self.Time - round(time.time() - self.TimeAll) == 0:
                self.finished = True
            self.draw_time()
            pygame.display.update()


if __name__ == '__main__':
    TimeAll = time.time()
    Letter(screen, 'o', TimeAll).manager()

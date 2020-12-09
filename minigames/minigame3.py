import pygame
from settings import *
from settings_for_minigame3 import *
import time
import random

pygame.init()
surface = pygame.display.set_mode((width_screen, height_screen))



class Manager:
    def __init__(self, screen):
        self.wait_space = wait
        self.wait_1 = wait
        self.wait_2 = 3 * wait
        self.wait_end_liter = 7 * wait - self.wait_1
        self.wait_end_word = 20 * wait - self.wait_end_liter
        self.frequency = 3.505
        self.i_word = 0
        self.elipce_tipe = Black
        self.screen = screen
        self.finished = False
        self.Mistake = 0
        self.i_frequency = 0
        self.result = 0
        self.random_word()
        self.split()
        print(self.word)


    def random_word(self):
        self.i_word = random.randint(0, len(words) - 1)
        self.word = words[self.i_word]

    def my_wait(self, time):

        self.screen.fill(White)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.finished = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos[0], pos[1]
                self.event_bottom(x, y)
                self.end(x, y)
        pygame.time.wait(time)
        self.draw_frequency(str(self.frequency) + ' MHz')
        self.draw_bottom()
        self.draw_frequency_scale()
        self.draw_end()
        self.my_ellipse()
        pygame.display.flip()

    def my_super_wait(self, time):
        for n in range(time// FPS):
            if self.finished:
                break
            self.my_wait(FPS)

    def split(self):
        end = ''
        for i in self.word:
            end = end + i + '='
        self.word_split = list(end)

    def my_ellipse(self):
        pygame.draw.ellipse(self.screen, self.elipce_tipe, ((width_screen // 10, height_screen // 10), (width_screen // 3, height_screen // 10)))
        pygame.display.flip()


    def draw_frequency(self, text):
        pygame.draw.rect(self.screen, Black, ((2 * width_screen//10, 5 * height_screen//10), (6 * width_screen//10, 2 * height_screen//10)))
        font = pygame.font.SysFont('serif', 48)
        text2 = font.render(text, 1, White)
        rect = text2.get_rect(center=(5 * width_screen//10, 6*height_screen//10))
        self.screen.blit(text2, rect)

    def event_bottom(self, x, y):
        if 1* width_screen // 10 - width_screen // 10 // 10 < x < 2 * width_screen // 10 + - width_screen // 10 // 10 \
                and 5 * height_screen // 10 < y < 7 * height_screen //10:
            self.i_frequency -= 1
            if self.i_frequency < 0:
                self.i_frequency = len(frequency_list) - 1
            self.frequency = frequency_list[self.i_frequency]
        if 8* width_screen // 10 + width_screen // 10 // 10 < x < 9 * width_screen // 10 + width_screen // 10 // 10 \
                and 5 * height_screen // 10 < y < 7 * height_screen //10:

            self.i_frequency += 1
            if self.i_frequency >= len(frequency_list):
                self.i_frequency = 0
            self.frequency = frequency_list[self.i_frequency]

    def draw_bottom(self):
        pygame.draw.polygon(self.screen, Black, ((2 * width_screen // 10 - width_screen // 10 // 10, 5 * height_screen // 10),\
                                            (1 * width_screen // 10, (5+7) * height_screen // 20),\
                                            (2 * width_screen // 10 - width_screen // 10 // 10, 7 * height_screen // 10)))
        pygame.draw.polygon(self.screen, Black, ((8 * width_screen // 10 + width_screen // 10 // 10, 5 * height_screen // 10), \
                                            (9 * width_screen // 10, (5 + 7) * height_screen // 20), \
                                            (8 * width_screen // 10 + width_screen // 10 // 10, 7 * height_screen // 10)))

    def draw_bulp(self):
        for i in self.word_split:
            if i == '.':
                self.elipce_tipe = Yellow
                self.my_super_wait(self.wait_1)

                self.elipce_tipe = Black
                self.my_super_wait(self.wait_space)

            if i == '=':
                self.elipce_tipe = Black
                self.my_super_wait(self.wait_end_word)

            if i == '_':
                self.elipce_tipe = Yellow
                self.my_super_wait(self.wait_2)

                self.elipce_tipe = Black
                self.my_super_wait(self.wait_space)



    def draw_frequency_scale(self):
        percent = int(self.frequency * 1000 % 1000 - 500)
        left = 1 * width_screen // 10
        right = 9 * width_screen // 10
        up = 3 * height_screen // 10
        bottom = 4 * height_screen // 10

        pygame.draw.rect(self.screen, Black, (left, up, right - left, bottom - up), 5)
        pygame.draw.rect(self.screen, Black, (left + (right - left)*(percent)//100 - 20, up, 20, bottom - up))
        n = 10
        for i in range(n):
            pygame.draw.rect(self.screen, Black, (left + (right - left)*(i) // n, up, 10, (bottom - up) // 4))

    def end(self, x, y):
        if top_end[0] < x < top_end[0] + size_end[0] and top_end[1] < y < top_end[1] + size_end[1]:
            if self.i_frequency == self.i_word:
                print('Ты выиграл')
                self.result = 1
            else:
                print('Нет')
                self.Mistake += 1


    def draw_end(self):
        pygame.draw.rect(self.screen, Green, (top_end, size_end))
        font = pygame.font.SysFont('serif', 48)
        text2 = font.render('TX', 1, White)
        rect = text2.get_rect(center = ((top_end[0] + size_end[0]//2) , (top_end[1] + size_end[1]//2)))
        self.screen.blit(text2, rect)

    def Manager(self):
        seconds_begin = time.time()
        clock = pygame.time.Clock()
        while not self.finished:
            clock.tick(FPS)
            self.my_super_wait(self.wait_end_word)
            self.draw_bulp()
        seconds_end = time.time()
        delta_time = seconds_end - seconds_begin
        return self.Mistake, self.result, delta_time


Mn = Manager(surface)
mistake, result, delta_time = Mn.Manager()
print(mistake, result, delta_time)
pygame.quit()

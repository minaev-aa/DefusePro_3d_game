import pygame
from settings import *
import time
import random

pygame.init()
surface = pygame.display.set_mode((width_screen, height_screen))

wait = 200
wait_space = wait
wait_1 = wait
wait_2 = 3 * wait
wait_end_liter = 7 * wait - wait_1
wait_end_word = 20 * wait - wait_end_liter
frequency = 3.505
frequency_list = [3.505, 3.515, 3.522, 3.532, 3.535, 3.542, 3.552, 3.555, 3.565, 3.572, 3.575, 3.582, 3.592, 3.595, 3.600]
i = 0
elipce_tipe = Black

A = '._'
B = '_...'
C = '_._.'
D = '_..'
E = '.'
F = '.._.'
G = '__.'
H = '....'
I = '..'
J = '.___'
K = '_._'
L = '._..'
M = '__'
N = '_.'
O = '___'
P = '.__.'
Q = '__._'
R = '._.'
S = '...'
T = '_'
U = '.._'
V = '..._'
W = '.__'
X = '_.._'
Y = '_.__'
Z = '__..'
words = [[S, H, E, L, L], [H, A, L, L, S], [S, L, I, C, K], [T, R, I, C, K], [B, O, X, E, S], [L, E, A, K, S], \
         [S, T, R, O, B, E], [B, I, S, T, R, O], [F, L, I, C, K], [B, O, M, B, S], [B, R, E, A, K], [B, R, I, C, K], \
         [S, T, E, A, K], [S, T, I, C, K], [V, E, C, T, O, R], [B, E, A, T, S]]

top_end = (3 * width_screen//10, 8 * height_screen//10)
size_end = (4 * width_screen//10, 1 * height_screen//10)
#(2 * width_screen//10, 5 * height_screen//10), (6 * width_screen//10, 2 * height_screen//10)

def random_word():
    i = random.randint(0, len(words) - 1)
    word_split = words[i]
    return word_split, i

def my_wait(time, i_word, elipce_tipe, screen, Mistake):
    global wait_1, wait_2, wait_end_liter, wait_end_word, wait_space
    finished = False
    screen.fill(White)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            wait_space = 1
            wait_1 = 1
            wait_2 = 1
            wait_end_liter = 1
            wait_end_word = 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x, y = pos[0], pos[1]
            event_bottom(x, y, screen)
            Mistake = end(x, y, i_word, Mistake)
    pygame.time.wait(time)
    draw_frequency(str(frequency) + ' MHz', screen)
    draw_bottom(screen)
    draw_frequency_scale(frequency, screen)
    draw_end(screen)
    my_ellipse(elipce_tipe, screen)
    pygame.display.flip()
    return finished, Mistake

def my_super_wait(time, i_word, elipce_tipe, screen, Mistake):
    finished = True
    for n in range(time // FPS):
        finished, Mistake = my_wait(FPS, i_word, elipce_tipe, screen, Mistake)
        if finished:
            break
    #if finished:
     #   print('lox')
    return finished, Mistake

def split(word):
    end = ''
    for i in word:
        end = end + i + '='
    return list(end)

def my_ellipse(color, screen):
    pygame.draw.ellipse(screen, color, ((width_screen // 10, height_screen // 10), (width_screen // 3, height_screen // 10)))
    pygame.display.flip()


def draw_frequency(text, screen):
    pygame.draw.rect(screen, Black, ((2 * width_screen//10, 5 * height_screen//10), (6 * width_screen//10, 2 * height_screen//10)))
    font = pygame.font.SysFont('serif', 48)
    text2 = font.render(text, 1, White)
    rect = text2.get_rect(center=(5 * width_screen//10, 6*height_screen//10))
    screen.blit(text2, rect)

def event_bottom(x, y, screen):
    global i, frequency
    if 1* width_screen // 10 - width_screen // 10 // 10 < x < 2 * width_screen // 10 + - width_screen // 10 // 10 \
            and 5 * height_screen // 10 < y < 7 * height_screen //10:
        i -= 1
        if i < 0:
            i = len(frequency_list) - 1
        frequency = frequency_list[i]
    if 8* width_screen // 10 + width_screen // 10 // 10 < x < 9 * width_screen // 10 + width_screen // 10 // 10 \
            and 5 * height_screen // 10 < y < 7 * height_screen //10:

        i += 1
        if i >= len(frequency_list):
            i = 0
        frequency = frequency_list[i]

def draw_bottom(screen):
    pygame.draw.polygon(screen, Black, ((2 * width_screen // 10 - width_screen // 10 // 10, 5 * height_screen // 10),\
                                        (1 * width_screen // 10, (5+7) * height_screen // 20),\
                                        (2 * width_screen // 10 - width_screen // 10 // 10, 7 * height_screen // 10)))
    pygame.draw.polygon(screen, Black, ((8 * width_screen // 10 + width_screen // 10 // 10, 5 * height_screen // 10), \
                                        (9 * width_screen // 10, (5 + 7) * height_screen // 20), \
                                        (8 * width_screen // 10 + width_screen // 10 // 10, 7 * height_screen // 10)))

def draw_bulp(word, i_word, screen, Mistake):
    #global elipce_tipe
    word_split = split(word)
    for i in word_split:
        if i == '.':
            elipce_tipe = Yellow
            finished, Mistake = my_super_wait(wait_1, i_word, elipce_tipe, screen, Mistake)

            elipce_tipe = Black
            finished, Mistake = my_super_wait(wait_space, i_word, elipce_tipe, screen, Mistake)

        if i == '=':
            elipce_tipe = Black
            finished, Mistake = my_super_wait(wait_end_liter, i_word, elipce_tipe, screen, Mistake)

        if i == '_':
            elipce_tipe = Yellow
            finished, Mistake = my_super_wait(wait_2, i_word, elipce_tipe, screen, Mistake)

            elipce_tipe = Black
            finished, Mistake = my_super_wait(wait_space, i_word, elipce_tipe, screen, Mistake)
    return finished, Mistake


def draw_frequency_scale(frequency, screen):
    percent = int(frequency * 1000 % 1000 - 500)
    left = 1 * width_screen // 10
    right = 9 * width_screen // 10
    up = 3 * height_screen // 10
    bottom = 4 * height_screen // 10

    pygame.draw.rect(screen, Black, (left, up, right - left, bottom - up), 5)
    pygame.draw.rect(screen, Black, (left + (right - left)*(percent)//100 - 20, up, 20, bottom - up))
    n = 10
    for i in range(n):
        pygame.draw.rect(screen, Black, (left + (right - left)*(i) // n, up, 10, (bottom - up) // 4))

def end(x, y, i_word, Mistake):
    if top_end[0] < x < top_end[0] + size_end[0] and top_end[1] < y < top_end[1] + size_end[1]:
        if i == i_word:
            print('Ты выиграл')
        else:
            print('Нет')
            Mistake += 1
    return Mistake


def draw_end(screen):
    pygame.draw.rect(screen, Green, (top_end, size_end))
    font = pygame.font.SysFont('serif', 48)
    text2 = font.render('TX', 1, White)
    rect = text2.get_rect(center = ((top_end[0] + size_end[0]//2) , (top_end[1] + size_end[1]//2)))
    screen.blit(text2, rect)
    pass

def Manager( screen, finished = False):
    Mistake = 0
    clock = pygame.time.Clock()
    word, i_word = random_word()
    while not finished:
        #screen.fill(White)
        clock.tick(FPS)
        #draw_frequency(str(frequency))
        #draw_bottom()
        #draw_frequency_scale(frequency)
        finished, Mistake = my_super_wait(wait_end_word, i_word, elipce_tipe, screen, Mistake)
        #my_ellipse(Black)
        finished, Mistake = draw_bulp(word, i_word, screen, Mistake)
        pygame.display.flip()
        #my_super_wait(wait_end_word)
    return Mistake



mistake = Manager(surface)
print(mistake)
pygame.quit()

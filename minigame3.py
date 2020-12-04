import pygame
from settings import *
import time

pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))

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

def my_wait(time):
    global finished, wait_1, wait_2, wait_end_liter, wait_end_word, wait_space
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
            event_bottom(x, y)
    pygame.time.wait(time)
    draw_frequency(str(frequency))
    draw_bottom()
    draw_frequency_scale(frequency)
    my_ellipse(elipce_tipe)
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x, y = pos[0], pos[1]
            event_bottom(x, y)
    '''

    pygame.display.flip()

def my_super_wait(time):
    for n in range(time // FPS):
        my_wait(FPS)
        if finished:
            break

def split(word):
    end = ''
    for i in word:
        end = end + i + '='
    return list(end)

def my_ellipse(color):
    pygame.draw.ellipse(screen, color, ((width_screen // 10, height_screen // 10), (width_screen // 3, height_screen // 10)))
    pygame.display.flip()


def draw_frequency(text):
    pygame.draw.rect(screen, Black, ((2 * width_screen//10, 5 * height_screen//10), (6 * width_screen//10, 2 * height_screen//10)))
    font = pygame.font.SysFont('serif', 48)
    text2 = font.render(text, 1, White)
    screen.blit(text2, (2 * width_screen//10, 5 * height_screen//10))

def event_bottom(x, y):
    global i, frequency
    if 1* width_screen // 10 - width_screen // 10 // 10 < x < 2 * width_screen // 10 + - width_screen // 10 // 10 \
            and 5 * height_screen // 10 < y < 8* height_screen //10:
        i -= 1
        if i < 0:
            i = len(frequency_list) - 1
        frequency = frequency_list[i]
    if 8* width_screen // 10 + width_screen // 10 // 10 < x < 9 * width_screen // 10 + width_screen // 10 // 10 \
            and 5 * height_screen // 10 < y < 8* height_screen //10:

        i += 1
        if i >= len(frequency_list):
            i = 0
        frequency = frequency_list[i]

def draw_bottom():
    pygame.draw.polygon(screen, Black, ((2 * width_screen // 10 - width_screen // 10 // 10, 5 * height_screen // 10),\
                                        (1 * width_screen // 10, (5+7) * height_screen // 20),\
                                        (2 * width_screen // 10 - width_screen // 10 // 10, 7 * height_screen // 10)))
    pygame.draw.polygon(screen, Black, ((8 * width_screen // 10 + width_screen // 10 // 10, 5 * height_screen // 10), \
                                        (9 * width_screen // 10, (5 + 7) * height_screen // 20), \
                                        (8 * width_screen // 10 + width_screen // 10 // 10, 7 * height_screen // 10)))

word_split = split([S, H, E, L, L])
print(split([S,H,E,L,L]))
def draw(word_split):
    global elipce_tipe
    for i in word_split:
        if i == '.':
            #my_ellipse(Yellow)
            elipce_tipe = Yellow
            my_super_wait(wait_1)

            #my_ellipse(Black)
            elipce_tipe = Black
            my_super_wait(wait_space)



        if i == '=':
            elipce_tipe = Black
            my_super_wait(wait_end_liter)


        if i == '_':
            elipce_tipe = Yellow
            my_super_wait(wait_2)

            elipce_tipe = Black
            my_super_wait(wait_space)


def draw_frequency_scale(frequency):
    percent = int(frequency * 1000 % 1000 - 500)
    left = 1 * width_screen // 10
    right = 9 * width_screen // 10
    up = 3 * height_screen // 10
    bottom = 4 * height_screen // 10

    pygame.draw.rect(screen, Black, (left, up, right - left, bottom - up), 5)
    pygame.draw.rect(screen, Black, (left + (right - left)*(percent)//100, up, 20, bottom - up))
    n = 10
    for i in range(n):
        pygame.draw.rect(screen, Black, (left + (right - left)*(i) // n, up, 10, (bottom - up) // 4))

clock = pygame.time.Clock()
finished = False
while not finished:
    screen.fill(White)
    clock.tick(FPS)
    draw_frequency(str(frequency))
    draw_bottom()
    draw_frequency_scale(frequency)
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x, y = pos[0], pos[1]
            event_bottom(x, y)
    '''
    my_super_wait(wait_end_word)
    #my_ellipse(Black)
    draw(word_split)
    pygame.display.flip()
    #my_super_wait(wait_end_word)

pygame.quit()


from settings import *

pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))
FPS = 30


def game1(sc, sn):
    count = [0, 0, 0, 0, 0]
    colors = [Blue, Red, White, Black, Yellow]
    k = random.randint(3, 6)
    num = k
    # Первое зачение вкл/выкл провода, второе цвет провода, третье и четвёртое координаты начала и конца провода
    line = [[False, None, [408, 299], [797, 299]], [False, None, [408, 339],
                                                    [797, 339]], [False, None, [408, 379], [797, 379]],
            [False, None, [408, 419], [797, 419]], [False, None, [408, 459],
                                                    [797, 459]], [False, None, [408, 499], [797, 499]]]
    i = random.randint(0, 5)
    while k != 0:
        if line[i][0] == False:
            line[i][0] = (random.choices([True, False]))[0]
            if line[i][0]:
                line[i][1] = (random.choices(colors))[0]
                for m in range(5):
                    if line[i][1] == colors[m]:
                        count[m] += 1
                k -= 1
        i += 1
        i = i % 6
    line_print(line, sc)
    right = correct(line, count, num, sn)
    return (line, right)


def numer(line, num):
    m = 0
    n = [None] * 8
    for i in range(6):
        if line[i][0]:
            if line[i][1] == Blue:
                n[6] = i
            if line[i][1] == Red:
                n[7] = i
            m += 1
        if m == 1:
            if n[0] == None:
                n[0] = i
        if m == 2:
            if n[1] == None:
                n[1] = i
        if m == 3:
            if n[2] == None:
                n[2] = i
        if m == 4:
            if n[3] == None:
                n[3] = i
        if m == 5:
            if n[4] == None:
                n[4] = i
        if m == 6:
            if n[5] == None:
                n[5] = i
    return n


def correct(line, color, num, sn):
    n = 0
    for i in range(6):
        if line[i][0]:
            n += 1
    tline = 0
    linennum = numer(line, num)
    if num == 3:
        if color[1] == 0:
            tline = linennum[1]
        if line[linennum[2]][1] == White:
            tline = linennum[2]
        if color[0] > 1:
            tline = linennum[6]
        else:
            tline = linennum[2]
    if num == 4:
        if color[1] > 1:
            if sn % 2 == 1:
                tline = linennum[7]
        if color[1] == 0:
            if line[linennum[3]][1] == Yellow:
                tline = linennum[0]
        if color[0] == 1:
            tline = linennum[0]
        if color[4] > 1:
            tline = linennum[3]
        else:
            tline = linennum[1]
    if num == 5:
        if line[linennum[4]][1] == Black:
            if sn % 2 == 1:
                tline = linennum[3]
        if color[1] == 1:
            if color[4] > 1:
                tline = linennum[0]
        if color[3] == 0:
            tline = linennum[1]
        else:
            tline = linennum[0]
    if num == 6:
        if color[4] == 0:
            if sn % 2 == 1:
                tline = linennum[2]
        if color[4] == 1:
            if color[2] > 1:
                tline = linennum[3]
        if color[1] == 0:
            tline = linennum[5]
        else:
            tline = linennum[3]
    return tline


def line_print(line, sc):
    dog_surf = pygame.image.load('Resources/Textures/plata.png').convert()
    dog_surf.set_colorkey((255, 255, 255))
    scale = pygame.transform.scale(
            dog_surf, (dog_surf.get_width(),
                       dog_surf.get_height()))
    scale_rect = scale.get_rect(
            topleft=(0, 0))
    scr = pygame.Surface((width_screen, height_screen))
    scr.fill((8, 217, 131))
    for p in range(6):
        if line[p][0]:
            pygame.draw.line(scr, line[p][1],
                             line[p][2],
                             line[p][3], 16)
    pygame.draw.rect(scr, (191, 145, 57),
                     (width_screen // 3 - 38, height_screen // 3, width_screen // 26, height_screen // 3))
    pygame.draw.rect(scr, (191, 145, 57),
                     (5 * width_screen // 8 + 47, height_screen // 3, width_screen // 26, height_screen // 3))

    scr.set_alpha(150)
    scale.blit(scr, (0, 0))
    sc.blit(scale, scale_rect)
    pygame.display.update()


def cut(sc, out, x, y):
    k = 8
    rez = 10
    surf = pygame.Surface((389, 2 * k))
    if 408 < x < 797:
        for i in range(6):
            if 299 + (40 * i) - k < y < 299 + (40 * i) + k:
                if out[i][0]:
                    surf.fill((8, 217, 131))
                    pygame.draw.line(surf, out[i][1], (0, k), (x - out[i][2][0] - rez, k), 20)
                    pygame.draw.line(surf, out[i][1], (x - out[i][2][0] + rez, k), (389, k), 20)
                    sc.blit(surf, (408, 300 + (40 * i) - k))
                    pygame.display.update()
                    return i
        return -1


def drawglobal(sc, result, light):
    button = pygame.image.load('Resources\\Textures\\button.png')
    surf4 = pygame.Surface((50, 50))
    surf4.blit(button, (0, 0))
    screen.blit(surf4, (width_screen - 60, 0))
    surf5 = pygame.Surface((100, 100))
    filter = pygame.surface.Surface((100, 100))
    if result == 1:
        surf5.fill(Green)
        filter.fill((Green))
    if result == 0:
        surf5.fill(Red)
        filter.fill(pygame.color.Color('Grey'))
    filter.blit(light, (0, 0))
    surf5.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
    surf5.set_colorkey(Grey)
    pygame.display.flip()
    sc.blit(surf5, (width_screen // 2 + 243, height_screen // 2 - 50))
    pygame.display.update()


def click(x, y):
    if 1140 < x < 1190:
        if 0 < y < 50:
            return True


def mistake(Mistake):
    Mistake += 1


def Manager(finished, sn, Mistake, TimeAll):
    font = pygame.font.SysFont(None, 100)
    text = font.render(str(Time) + ' сек', True, Black)
    surf1 = pygame.Surface((300, 120))
    surf1.fill(White)
    light = pygame.image.load('Resources\\Textures\\circle.png')
    result = 0
    x, y = 0, 0
    clock = pygame.time.Clock()
    out = game1(screen, sn)
    true = out[1]
    while not finished:
        clock.tick(FPS)
        drawglobal(screen, result, light)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                finished = True
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if click(x, y):
                    finished = True
                cuts = cut(screen, out[0], x, y)
                if cuts == true:
                    result = 1
                if cuts != None:
                    if cuts != -1:
                        if cuts != true:
                            mistake(Mistake)
        text = font.render(str(Time - round(time.time() - TimeAll)) + ' сек', True, Black)
        if Time - round(time.time() - TimeAll) == 0:
            finished = True
        text_rect = text.get_rect(center=surf1.get_rect().center)
        surf1.fill(White)
        surf1.blit(text, text_rect)
        screen.blit(surf1, (0, 0))
    return (result, Mistake)


if __name__ == '__main__':
    TimeAll = time.time()
    print(Manager(False, sn,
                  Mistake,
                  TimeAll))  # Изменяет время и количество ошибок гловально. Выдаёт статус задания 1 значит выполнено
    print(Mistake)
    print(Time)

import pygame as pg
import sys


def test():

    W = 400
    H = 300

    sc = pg.display.set_mode((W, H))
    sc.fill((100, 150, 200))

    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()

        pg.time.delay(20)


class Menu():
    def __init__(self):
        pass

W = 1400
H = 1300

sc = pg.display.set_mode((W, H))
sc.fill((100, 150, 200))

dog_surf = pg.image.load('Textures\ЛК.jpg')

sc.blit(dog_surf, 0, 0)

pg.display.update()
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    pg.time.delay(20)




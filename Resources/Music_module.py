import pygame as pg
import sys


if __name__ == '__main__':
    """
    Эта функция позволяет оценить работу модуля звука и разобраться в работе функций фонового звука и сторонних звуков.
    """
    pg.init()
    sc = pg.display.set_mode((400, 300))

    pg.mixer.music.load('Music_and_sound\Format_ogg\страшный гул.ogg')
    pg.mixer.music.play(-1)

    sound1 = pg.mixer.Sound('Music_and_sound\Format_ogg\шаги - 2.ogg')
    sound2 = pg.mixer.Sound('Music_and_sound\Format_ogg\Бег - 6 шагов.ogg')

    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()

            elif i.type == pg.KEYUP:
                if i.key == pg.K_1:
                    pg.mixer.music.pause()
                    # pygame.mixer.music.stop()
                elif i.key == pg.K_2:
                    pg.mixer.music.unpause()
                    # pygame.mixer.music.play()
                    pg.mixer.music.set_volume(0.1)
                elif i.key == pg.K_3:
                    pg.mixer.music.unpause()
                    # pygame.mixer.music.play()
                    pg.mixer.music.set_volume(1)

            elif i.type == pg.MOUSEBUTTONUP:
                if i.button == 1:
                    sound1.play()
                elif i.button == 3:
                    sound2.play()

        pg.time.delay(20)

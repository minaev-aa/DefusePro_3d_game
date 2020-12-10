import pygame as pg
from settings import *

class game():
    def __init__(self):
        """
        Класс миниигры номер 5.
        """
        self.W = width_screen
        self.H = height_screen
        self.symbols = []
        self.len_of_alpabet = 27
        for num in range(self.len_of_alpabet):
            slash = "\ "
            self.symbols.append(pg.image.load('Resources\Textures\minigame5\m1.png'))




if __name__ == '__main__':
    g = game()
    print(g.symbols)
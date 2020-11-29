import pygame
from settings import *

class Minigame:
    def __init__(self, audio, sc):
    """
    Это конструктор главного меню.
    :param audio: обьект, делающий звук.
    :param sc: Экран, на котором рисуется игра.
    """
    self.size_of_font = 30
    self.but_size = 120
    self.buts = []
    self.audio = audio
    self.W = width_screen  # Размеры экрана для модуля главного меню.
    self.H = height_screen  # Ширина для модуля главного меню.
from settings import *

text_map = [
    '000p000000006000000000',
    '00.....0.........0...0',
    '7...00...0...000...0.0',
    '00.0....0..0...0..01.0',
    '2..0....0..0..0.0....0',
    '0.00.0.0.0...0...0.000',
    '0....0.....0...0.....3',
    '6.00...0...5.0...0.0.0',
    '0..00c...0.0.000...0.0',
    '00...00.0..0.0....0..0',
    'o..0.0..00....0.0..0.d',
    '00....0.0.0.0.0.....00',
    '0..0...........0.0...7',
    '040000000000t000000000'
]

# Задание карты в текстовом формате и передача информации
def map_create(text_map):
    map = {}
    active_in_map = {}
    chars = ['1', '2', '3', '4', '5', 'o', 'd', 't', 'c', 'p']
    for j, row in enumerate(text_map):
        for i, char in enumerate(row):
            if char != '.':
                if char in ['0', '6', '7']:
                    map[(i * cube, j * cube)] = char
                for k in chars:
                    if char == k:
                        map[(i * cube, j * cube)] = k
                        active_in_map[(i * cube, j * cube)] = k
    return map, active_in_map

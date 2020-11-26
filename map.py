from settings import *

text_map = [
    'WWWWWWWWWWWW',
    'W.W....W...W',
    'W.W.WW...W.W',
    'W.......WW.W',
    'W..W....W..W',
    'W..W...W.W.W',
    'W....W.....W',
    'WWWWWWWWWWWW'
]
sprite1_data = (1, 200, 300, 'Resources\\Sprayt\\guard_good.png') # Маштаб, х, y, файл


map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            map.add((i * cube, j * cube))
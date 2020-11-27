from settings import *

sprite1_data = (1, 200, 300, 'Resources\\Sprayt\\guard_good.png') # Маштаб, х, y, файлsw

text_map = [
    '111121111111',
    '1......1...1',
    '1..111...1.1',
    '1....1..11.1',
    '1..1....1..1',
    '1..1...1.1.1',
    '1....1.....1',
    '1121111111111'
]

map = {}
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            if char == '1':
                map[(i * cube, j * cube)] = '1'
            elif char == '2':
                map[(i * cube, j * cube)] = '2'
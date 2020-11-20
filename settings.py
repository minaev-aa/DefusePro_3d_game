import math
width_screen = 1200
height_screen = 500
FPS = 60
width_cube = 10
height_cube = 10
cube = 100

fov = math.pi / 3
pol_fov = fov / 2
count_ray = 120
mdepth = 800
d_angle = fov / count_ray
distance = count_ray / (2 * math.tan(count_ray))
proec_k = 3 * distance * cube
size = width_screen // count_ray



player_speed = 1
player_angle = 0 #начальный угол смотрит вверх по миникарте
player_angle_change_speed = 0.01
x_player = 500
y_player = 300
radius_player = 5

White = (255, 255, 255)
Green = (0, 100, 0)
Black = (0, 0, 0)
Yellow = (255, 255, 0)
Blue = (0, 0, 255)
Red = (255, 0, 0)
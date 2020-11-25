import math
width_screen = 1200
height_screen = 800
FPS = 60
cube = 100

fov = math.pi / 3
pol_fov = fov / 2
count_ray = 300
mdepth = 800
d_angle = fov / count_ray
distance = count_ray / (2 * math.tan(pol_fov))
proec_k =  3 * distance * cube
size = width_screen // count_ray
min_alpha = 0.000001

player_speed = 6
player_angle = 0 #начальный угол смотрит вверх по миникарте
player_angle_change_speed = 0.04
player_pos = (width_screen //2 ,height_screen//2)

White = (255, 255, 255)
Green = (0, 100, 0)
Black = (0, 0, 0)
Yellow = (255, 255, 0)
Blue = (0, 0, 255)
Red = (255, 0, 0)
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
proec_k = 3 * distance * cube
size = width_screen // count_ray
min_alpha = 0.000001

player_speed = 6
player_angle = min_alpha  # начальный угол смотрит вверх по миникарте
player_angle_change_speed = 0.04
player_pos = (width_screen // 2, height_screen // 2)

texture_size = 600
texture_k = texture_size // cube

size_sprite = 100

scale_minimap = 5
player_radius = 5
player_length = 4  # длинна той штуки, которая торчит из игрока на миникарте для указание направления взгляда
player_width = 2  # ширина этой штуки

White = (255, 255, 255)
Green = (0, 100, 0)
Black = (0, 0, 0)
Yellow = (255, 255, 0)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Grey = (40, 40, 40)

# Длительность звуковых файлов.
steps_duration = 1.5
running_duration = 1.5
plus_anything_duration = 1.2
sound_when_cursor_under_button_duration = 0.2
sound_if_button_down_duration = 1.2
shortness_duration = 2.2
exhalation_duration = 4.4
checkpoint_duration = 1.2
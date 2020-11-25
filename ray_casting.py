import pygame
from settings import *
from map import *

def mapping(a, b):
    return (a // cube) * cube, (b // cube) * cube

def ray_casting(sc, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - pol_fov
    for ray in range(count_ray):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else min_alpha
        cos_a = cos_a if cos_a else min_alpha
        # verticals
        x, dx = (xm + cube, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, width_screen, cube):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in map:
                break
            x += dx * cube

        # horizontals
        y, dy = (ym + cube, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, height_screen, cube):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in map:
                break
            y += dy * cube

        # projection
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, min_alpha)
        proj_height = proec_k / depth
        color = Green
        pygame.draw.rect(sc, color, (ray * size, height_screen // 2 - proj_height // 2, size, proj_height))
        cur_angle += d_angle

import pygame
from settings import *
from map import *


def mapping(a, b):
    return (a // cube) * cube, (b // cube) * cube


def ray_casting(sc, player_pos, player_angle, texturs):
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
            deep_v = (x - ox) / cos_a
            yv = oy + deep_v * sin_a
            m = mapping(x + dx, yv)
            if m in map:
                textur_v = map[m]
                break
            x += dx * cube

        # horizontals
        y, dy = (ym + cube, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, height_screen, cube):
            deep_h = (y - oy) / sin_a
            xh = ox + deep_h * cos_a
            m = mapping(xh, y + dy)
            if m in map:
                textur_h = map[m]
                break
            y += dy * cube

        # projection
        deep, shift, textur = (deep_v, yv, textur_v) if deep_v < deep_h else (deep_h, xh, textur_h)
        shift = int(shift) % cube
        deep *= math.cos(player_angle - cur_angle)
        deep = max(deep, min_alpha)
        proj_height = min(int(proec_k / deep), 2 * height_screen)
        color = Green
        pygame.draw.rect(sc, color, (ray * size, height_screen // 2 - proj_height // 2, size, proj_height))
        cur_angle += d_angle

        wall = texturs[textur].subsurface(shift * texture_k, 0, texture_k, texture_size)
        wall = pygame.transform.scale(wall, (size, proj_height))
        sc.blit(wall, (ray * size, height_screen // 2 - proj_height // 2))

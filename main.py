import pygame
from levels import level_1

TILE_SIZE = 40
COLORS = {
    " ": (0, 0, 0),       # пустой проход - чёрный
    "W": (255, 255, 255), # стены - белый
    "D": (0, 0, 255),     # двери - синий
    "K": (255, 255, 0),   # ключи - жёлтый
    "E": (0, 255, 0),     # выход - зелёный
    "P": (255, 0, 0)      # игрок - красный
}

def draw_level(screen, level):
    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            color = COLORS.get(tile, (0, 0, 0))
            pygame.draw.rect(screen, color, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

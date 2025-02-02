import pygame

import sys

from setting import MainSettings

from player_ship import Ship

pygame.init()

# 设置
screen_setting = MainSettings(
    1200,
    800,
    (230, 230, 230),
    60
)

# 平衡值
balance_k = screen_setting.width / screen_setting.height

# 屏幕
screen = pygame.display.set_mode(
    (
        screen_setting.width,
        screen_setting.height
    )
)
pygame.display.set_caption("电棍笑传")
screen.fill(screen_setting.bg_color)
clock = pygame.time.Clock()

# 玩家
ship = Ship(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ship.location.y -= screen_setting.height / 20
            if event.key == pygame.K_s:
                ship.location.y += screen_setting.height / 20
            if event.key == pygame.K_a:
                ship.location.x -= screen_setting.width / (20 * balance_k)
            if event.key == pygame.K_d:
                ship.location.x += screen_setting.width / (20 * balance_k)

    ship.place_ship()

    pygame.display.flip()
    clock.tick(60)
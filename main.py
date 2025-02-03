import pygame

import sys

from setting import MainSettings

from player_ship import Ship

from weapon import Weapon

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

clock = pygame.time.Clock()

# 玩家
ship = Ship(screen)
bullet_list = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ship.rect.y = max(
                    ship.rect.y - screen_setting.height / 20,
                    0
                )
            if event.key == pygame.K_s:
                ship.rect.y = min(
                    ship.rect.y + screen_setting.height / 20,
                    screen_setting.height - 50
                )
            if event.key == pygame.K_a:
                ship.rect.x = max(
                    ship.rect.x - screen_setting.width / (20 * balance_k),
                    0
                )
            if event.key == pygame.K_d:
                ship.rect.x = min(
                    ship.rect.x + screen_setting.width / (20 * balance_k),
                    screen_setting.width - 50
                )
            if event.key == pygame.K_j:
                bullet = Weapon(ship, "images/bullet.png", screen)
                bullet_list.append(bullet)

    screen.fill(screen_setting.bg_color)
    ship.place_ship()
    for bullet in bullet_list:
        screen.blit(bullet.image, bullet.rect)
        bullet.weapon_fire()

    pygame.display.flip()
    clock.tick(60)
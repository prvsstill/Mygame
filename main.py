import pygame
import sys
from setting import MainSettings
from player_ship import Ship
from weapon import Weapon
import time

pygame.init()
pygame.mixer.init()

# 设置
screen_setting = MainSettings(
    1200,
    800,
    (230, 230, 230),
    60
)

# 平衡值
balance_k = screen_setting.width / screen_setting.height

# 音频
sound_atomic_bomb = pygame.mixer.Sound("audio/atomic_bomb.wav")
pygame.mixer.music.load("music/open.mp3")

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

# 文字
text_font = pygame.font.SysFont(None, 36)
text_color = (30, 30, 30)
text_hp = text_font.render("HP: " + str(ship.hp), True, text_color)
text_mp = text_font.render("MP: " + str(ship.mp), True, text_color)
text_hp_rect = text_hp.get_rect()
text_mp_rect = text_mp.get_rect()
text_hp_rect.midtop = screen.get_rect().midtop
text_mp_rect.midtop = text_hp_rect.midbottom

# 主程序及循环

pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pygame.mixer.music.stop()
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
                bullet = Weapon(
                    ship, "images/bullet.png", screen, speed=3
                )
                bullet_list.append(bullet)
            if event.key == pygame.K_k:
                if ship.mp >= 10:
                    ship.mp -= 10
                    text_mp = text_font.render(
                        "MP: " + str(ship.mp), True, text_color
                    )
                    bullet = Weapon(
                        ship, "images/atomic_bomb.png", screen, speed=1
                    )
                    bullet_list.append(bullet)
                    sound_atomic_bomb.play()
                else:
                    pass

    screen.fill(screen_setting.bg_color)
    screen.blit(text_hp, text_hp_rect)
    screen.blit(text_mp, text_mp_rect)
    ship.place_ship()
    for bullet in bullet_list:
        screen.blit(bullet.image, bullet.rect)
        bullet.weapon_fire()
        if bullet.rect.centery < 0:
            bullet_list.remove(bullet)
        if bullet.is_atomic_bomb:
            bullet.speed += 0.1

    pygame.display.flip()
    clock.tick(screen_setting.frequency)
import pygame
import sys
from setting import MainSettings
from player_ship import Ship
from weapon import Weapon
from enemy_ship import EnemyShip
import time

# 初始化
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
enemy_bullet_list = []

# 敌人
dingdong = EnemyShip(screen, ship)

# 文字
text_font = pygame.font.SysFont(None, 36)
text_color = (30, 30, 30)
text_hp = text_font.render("HP: " + str(ship.hp), True, text_color)
text_mp = text_font.render("MP: " + str(ship.mp), True, text_color)
text_hp_rect = text_hp.get_rect()
text_mp_rect = text_mp.get_rect()
text_hp_rect.midtop = screen.get_rect().midtop
text_mp_rect.midtop = text_hp_rect.midbottom

# 死亡otto
otto = Ship(screen)
otto.image = pygame.image.load("images/古神.png")
original_width, original_height = pygame.image.load("images/古神.png").get_size()

screen_rect = screen.get_rect()

scale = 0.2
scale_speed = 0.1

otto.image = pygame.transform.scale(
    otto.image, (
        int(original_width * scale),
        int(original_height * scale)
    )
)
is_waao_played = False
dingdong_played = False

# 主程序及循环

# pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and not ship.dead:
                ship.moving_up = True
            elif event.key == pygame.K_s and not ship.dead:
                ship.moving_down = True
            elif event.key == pygame.K_a and not ship.dead:
                ship.moving_left = True
            elif event.key == pygame.K_d and not ship.dead:
                ship.moving_right = True
            elif event.key == pygame.K_j and not ship.dead:
                bullet = Weapon(
                    ship, "images/bullet.png", screen, speed=3
                )
                bullet_list.append(bullet)
            elif event.key == pygame.K_k and not ship.dead:
                if ship.mp >= 30:
                    ship.mp -= 30
                    bullet = Weapon(
                        ship, "images/atomic_bomb.png", screen, speed=1, ap=100
                    )
                    bullet_list.append(bullet)
                    sound_atomic_bomb.play()
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                ship.moving_up = False
            elif event.key == pygame.K_s:
                ship.moving_down = False
            elif event.key == pygame.K_a:
                ship.moving_left = False
            elif event.key == pygame.K_d:
                ship.moving_right = False

    ship.move_ship()
    dingdong.move()
    screen.fill(screen_setting.bg_color)
    ship.place_ship()
    dingdong.place()
    dingdong.victory(ship)

    if dingdong.rect.x == ship.rect.x:
        enemy_bullet_list.append(Weapon(dingdong, "images/bullet.png", screen))

    for enemy_bullet in enemy_bullet_list:
        screen.blit(enemy_bullet.image, enemy_bullet.rect)
        enemy_bullet.rect.y += 1

    screen.blit(text_hp, text_hp_rect)
    screen.blit(text_mp, text_mp_rect)

    if dingdong.is_dead:
        enemy_bullet_list.clear()
        screen.blit(
            pygame.font.SysFont(None, 100).render(
                "You win", True, (255, 0, 0)
            ),(600, 300)
        )
        if not dingdong_played:
            time.sleep(0.5)
            pygame.mixer.Sound("audio/win.wav").play()
            dingdong_played = True

    for bullet in bullet_list:
        if dingdong.hit(bullet):
            bullet_list.remove(bullet)

    for bullet in enemy_bullet_list:
        if ship.hit(bullet):
            enemy_bullet_list.remove(bullet)


    for bullet in bullet_list:
        screen.blit(bullet.image, bullet.rect)
        bullet.weapon_fire()
        if bullet.rect.centery < 0:
            bullet_list.remove(bullet)
        if bullet.is_atomic_bomb:
            bullet.speed += 0.1

    if ship.hit(dingdong):
        ship.hp = 0
        ship.dead = True

    text_hp = text_font.render("HP: " + str(ship.hp), True, text_color)
    text_mp = text_font.render("MP: " + str(ship.mp), True, text_color)
    if ship.hp <= 0 or ship.dead:
        otto.rect.center = screen_rect.center
        otto.place_ship()
        ship.dead = True
        if not is_waao_played:
            pygame.mixer.music.load("music/waao.wav")
            pygame.mixer.music.play()
        is_waao_played = True
        if scale < 2:
            scale += scale_speed
            otto.image = pygame.transform.scale(
                otto.image, (
                    int(original_width * scale),
                    int(original_height * scale)
                )
            )
            otto.rect = otto.image.get_rect()

    pygame.display.flip()
    clock.tick(screen_setting.frequency)
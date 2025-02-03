import pygame
import sys
from setting import MainSettings
from player_ship import Ship
from weapon import Weapon

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
                if ship.mp >= 10:
                    ship.mp -= 10
                    bullet = Weapon(
                        ship, "images/atomic_bomb.png", screen, speed=1
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

    text_hp = text_font.render("HP: " + str(ship.hp), True, text_color)
    text_mp = text_font.render("MP: " + str(ship.mp), True, text_color)
    if ship.hp <= 0:
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
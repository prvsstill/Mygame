import pygame

class Ship:

    def __init__(self, screen, hp=None, ap=None, mp=None):
        #生命值和攻击力
        if hp:
            self.hp = hp
        else:
            self.hp = 100
        if ap:
            self.ap = ap
        else:
            self.ap = 5
        if mp:
            self.mp = mp
        else:
            self.mp = 100

        self.screen = screen
        self.screen_rect = screen.get_rect()

        original_image = pygame.image.load("images/古神.png")
        self.image = pygame.transform.scale(
            original_image, (50, 50)
        )
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # 移动标志
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.speed = 4

        self.dead = False

    def place_ship(self):
        self.screen.blit(self.image, self.rect)

    def move_ship(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
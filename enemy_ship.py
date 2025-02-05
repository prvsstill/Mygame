import pygame

import weapon

class EnemyShip:

    def __init__(self, screen, player, hp=None):
        if hp:
            self.hp = hp
        else:
            self.hp = 250

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load("images/叮咚鸡.jpg")
        self.rect = self.image.get_rect()

        self.player = player
        self.bullet = weapon.Weapon(self, "images/bullet.png", screen)
        self.bullet_rect = self.bullet.image.get_rect()
        self.bullet_rect. midtop = self.rect.midbottom

        self.rect.midtop = self.screen_rect.midtop

        self.hp_image = pygame.font.SysFont(None, 36).render(
            "HP: " + str(self.hp), True, (30, 30, 30)
        )
        self.hp_rect = self.hp_image.get_rect()
        self.hp_rect.midtop = self.rect.midbottom

        self.is_dead = False


    def move(self):
        if not self.is_dead:
            if 5 >= self.player.rect.centerx - self.rect.centerx >= -50 \
                    and self.rect.x <= self.screen_rect.right - 75:
                self.rect.x += 3
            elif -5 <= self.player.rect.centerx - self.rect.centerx <= 50 \
                    and self.rect.x >= self.screen_rect.left + 75:
                self.rect.x -= 3
            else:
                self.rect.y += 2
            self.hp_rect.midtop = self.rect.midbottom
        if self.hp <= 0:
            self.is_dead = True

    def place(self):
        if not self.is_dead:
            self.screen.blit(self.image, self.rect)
            self.screen.blit(self.hp_image, self.hp_rect)

    def hit(self, bullet):
        if self.rect.left <= bullet.rect.centerx <= self.rect.right\
            and self.rect.top <= bullet.rect.centery <= self.rect.bottom:
            self.hp -= bullet.ap
            self.hp_image = pygame.font.SysFont(None, 36).render(
                "HP: " + str(self.hp), True, (30, 30, 30)
            )
            return True

    def victory(self, player):
        if self.hp >= 0 and self.rect.y >= self.screen_rect.bottom:
            player.dead = True

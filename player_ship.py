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
        self.image = pygame.image.load("images/古神.png")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def place_ship(self):
        self.screen.blit(self.image, self.rect)
import pygame

class Weapon:

    def __init__(self, ship, path, screen, ap=None, speed=None):
        if ap:
            self.ap = ap
        else:
            self.ap = 10

        if speed:
            self.speed = speed
        else:
            self.speed = 2

        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.midbottom = ship.rect.midtop

    def weapon_fire(self):
        self.rect.y -= self.speed
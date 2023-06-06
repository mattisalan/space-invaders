import pygame
from pygame.locals import *

from constants import BULLET_SPEED


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position: list[int]) -> None:
        super().__init__()
        self.image = pygame.image.load("img/bullet.png").convert_alpha()
        self.rect = self.image.get_rect(center=position)

        # Variable for keeping track of the floating point position
        self.y = self.rect.y
        
    def update(self, dt) -> None:
        self.y -= BULLET_SPEED * dt
        self.rect.y = round(self.y)
        if self.rect.bottom < 0:
            self.kill()

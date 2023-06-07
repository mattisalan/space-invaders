import pygame
from pygame.locals import *

from constants import BULLET_SPEED, SCREEN_HEIGHT


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position: list[int], image, dir: int=1) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)

        # Variable for keeping track of the floating point position
        self.y = self.rect.y
        # Direction of the movement (up=1, down=-1)
        self.dir = dir
        
    def update(self, dt) -> None:
        self.y -= self.dir * BULLET_SPEED * dt
        self.rect.y = round(self.y)
        # Kill if out of screen
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()

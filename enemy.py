import random

import pygame
from pygame.locals import *

from constants import *


class Enemy(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("img/enemy1.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.centerx = random.randint(50, SCREEN_WIDTH - 50)
        self.rect.centery = 0

        # Variables for floating point position
        self.x = self.rect.x
        self.y = self.rect.y

    def move_down(self, dt) -> None:
        self.y += ENEMY_SPEED * dt
        self.rect.y = round(self.y)
        # Need to be killed when out of screen / game over

    def update(self, dt) -> None:
        self.move_down(dt)
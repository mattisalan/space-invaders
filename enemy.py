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

    def get_new_bullet_position(self):
        return [self.rect.centerx, self.rect.bottom]

    def move_down(self, dt) -> None:
        self.y += ENEMY_SPEED * dt
        self.rect.y = round(self.y)
        # Need to be killed when out of screen / game over

    def check_bullet_collision(self, bullets_group):
        bullet_hit = pygame.sprite.spritecollideany(self, bullets_group)
        if bullet_hit is not None:
            bullet_hit.kill()
            self.kill()

    def update(self, bullets_group, dt) -> None:
        self.move_down(dt)
        self.check_bullet_collision(bullets_group)
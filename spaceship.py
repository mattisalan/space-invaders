import pygame
from pygame.locals import *

from constants import *


class Spaceship(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("img/spaceship.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        # Initial position
        self.rect.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100]
        # variable for floating point position
        self.x = self.rect.x

    def move_right(self, dt) -> None:
        self.x += SPACESHIP_SPEED * dt
        # Do not let spaceship go out of screen
        if self.x > SCREEN_WIDTH - self.rect.width:
            self.x = SCREEN_WIDTH - self.rect.width
        self.rect.x = round(self.x)

    def move_left(self, dt) -> None:
        self.x -= SPACESHIP_SPEED * dt
        if self.x < 0:
            self.x = 0
        self.rect.x = round(self.x)

import pygame
from pygame.locals import *

from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Spaceship(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("img/spaceship.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        # Initial position
        self.rect.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100]
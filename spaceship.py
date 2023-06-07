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

        self.lives = MAX_HEALTH

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

    def get_new_bullet_pos(self) -> list[int]:
        return [self.rect.centerx, self.rect.top]
    
    def check_if_hit(self, enemy_bullets_group, enemies_group) -> bool:
        bullet_hit = pygame.sprite.spritecollideany(self, enemy_bullets_group)
        if bullet_hit is not None:
            bullet_hit.kill()
            self.lives -= 1

        enemy_hit = pygame.sprite.spritecollideany(self, enemies_group)
        if enemy_hit is not None:
            enemy_hit.kill()
            self.lives -= 1

        # Lose health if enemy gets to the bottom of the screen
        for enemy in enemies_group.sprites():
            if enemy.rect.top > SCREEN_HEIGHT:
                self.lives -= 1
                enemy.kill()

        if self.lives == 0:
            return True
        
        return False

    def draw_healtbar(self, screen) -> None:
        health_ratio = self.lives / MAX_HEALTH
        pygame.draw.rect(screen, RED, (self.rect.x, self.rect.bottom + 10, self.rect.width, 10))
        pygame.draw.rect(screen, GREEN, (self.rect.x, self.rect.bottom + 10, health_ratio * self.rect.width, 10))
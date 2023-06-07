import time
import random

import pygame
from pygame.locals import *

from constants import *
from spaceship import Spaceship
from bullet import Bullet
from enemy import Enemy


def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders")

    background = pygame.image.load("img/bg.png").convert()
    bullet = pygame.image.load("img/bullet.png").convert_alpha()
    enemy_bullet = pygame.image.load("img/enemy_bullet.png").convert_alpha()

    # Game objects
    spaceship = Spaceship()
    spaceship_group = pygame.sprite.GroupSingle(spaceship)
    bullets_group = pygame.sprite.Group()
    enemies_group = pygame.sprite.Group()
    enemy_bullets_group = pygame.sprite.Group()

    # Timers
    previous_time = time.time() # Delta time
    last_bullet = time.time() # Player shooting
    enemy_spawn_time = time.time() # Enemy spawn
    last_enemy_bullet = time.time() # Enemy shooting

    # GAME LOOP
    while True:
        # Delta time
        time_now = time.time()
        dt = time_now - previous_time
        previous_time = time_now

        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        
        keys = pygame.key.get_pressed()
        # Movement
        if keys[K_LEFT]:
            spaceship.move_left(dt)
        if keys[K_RIGHT]:
            spaceship.move_right(dt)
        # Shooting
        if keys[K_UP]:
            current_bullet = time.time()
            if current_bullet - last_bullet > BULLET_COOLDOWN:
                bullets_group.add(Bullet(spaceship.get_new_bullet_pos(), bullet))
                last_bullet = current_bullet

        # GAME LOGIC
        
        # Spawn enemies
        enemy_spawn_time_now = time.time()
        if enemy_spawn_time_now - enemy_spawn_time > SPAWN_TIME:
            enemies_group.add(Enemy())
            enemy_spawn_time = enemy_spawn_time_now

        enemy_bullet_now = time.time()
        if enemies_group and (enemy_bullet_now - last_enemy_bullet > ENEMY_BULLET_COOLDOWN):
            # Chooce enemy that shoots randomly
            enemy = random.choice(enemies_group.sprites())
            enemy_bullets_group.add(Bullet(enemy.get_new_bullet_position(), enemy_bullet, -1))
            last_enemy_bullet = enemy_bullet_now # Update timer

        bullets_group.update(dt)
        enemy_bullets_group.update(dt)
        enemies_group.update(bullets_group, dt)
        spaceship.check_if_hit(enemy_bullets_group, enemies_group)

        # RENDER GRAPHICS
        screen.blit(background, (0, 0))
        spaceship_group.draw(screen)
        bullets_group.draw(screen)
        enemy_bullets_group.draw(screen)
        enemies_group.draw(screen)

        # Update screen
        pygame.display.flip()

        # FPS limit
        clock.tick(FPS)


if __name__ == "__main__":
    main()
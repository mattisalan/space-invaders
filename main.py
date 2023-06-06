import time

import pygame
from pygame.locals import *

from constants import *
from spaceship import Spaceship
from bullet import Bullet


def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders")

    background = pygame.image.load("img/bg.png").convert()
    # Game objects
    spaceship = Spaceship()
    spaceship_group = pygame.sprite.GroupSingle(spaceship)
    bullets_group = pygame.sprite.Group()

    previous_time = time.time()
    last_bullet = time.time()
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
                bullets_group.add(Bullet(spaceship.get_new_bullet_pos()))
                last_bullet = current_bullet

        # GAME LOGIC
        bullets_group.update(dt)

        # RENDER GRAPHICS
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        spaceship_group.draw(screen)
        bullets_group.draw(screen)

        # Update screen
        pygame.display.flip()

        # FPS limit
        clock.tick(FPS)


if __name__ == "__main__":
    main()
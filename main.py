import pygame
from pygame.locals import *

from constants import *
from spaceship import Spaceship


def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders")

    background = pygame.image.load("img/bg.png").convert()
    # Game objects
    spaceship = Spaceship()
    spaceship_group = pygame.sprite.GroupSingle(spaceship)

    # GAME LOOP
    while True:
        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            
        # GAME LOGIC

        # RENDER GRAPHICS
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        spaceship_group.draw(screen)

        # Update screen
        pygame.display.flip()

        # FPS limit
        clock.tick(FPS)


if __name__ == "__main__":
    main()
import pygame
from pygame.locals import *

from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGH))
    pygame.display.set_caption("Space Invaders")

    background = pygame.image.load("img/bg.png")

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

        # Update screen
        pygame.display.flip()

        # FPS limit
        clock.tick(FPS)

        
if __name__ == "__main__":
    main()
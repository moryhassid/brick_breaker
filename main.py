import time
from pygame import draw
import pygame
import random

BACKGROUND_COLOR = (255, 255, 255)

if __name__ == '__main__':
    pygame.init()

    # font = pygame.font.Font('fonts/ChrustyRock-ORLA.ttf', 32)
    white = (255, 255, 255)
    green = (0, 255, 0)
    brick_color = (185, 206, 212)
    blue = (0, 0, 128)

    WIDTH_SCREEN = 1080
    HEIGHT_SCREEN = 550

    # pygame setup
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    screen.fill(BACKGROUND_COLOR)

    # left, top, width, height
    # brick1 = pygame.Rect(left=50, top=50, width=80, height=30)

    for left_idx in range(15):
        brick1 = pygame.Rect(left_idx * 60, 50, 50,20)

        draw.rect(surface=screen,
                  color=brick_color,
                  rect=brick1)

    # Very important each frame we should use to  put your work on screen
    pygame.display.flip()
    time.sleep(5)

    pygame.quit()

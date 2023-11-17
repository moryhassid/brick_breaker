import time
from pygame import draw
import pygame
import random

BACKGROUND_COLOR = (255, 255, 255)
BRICK_HEIGHT = 20
BRICK_WIDTH = 42
NUMBER_OF_BRICK_ROWS = 4
NUMBER_OF_BRICKS_IN_ROW = 18

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

    # The following loop create a row of bricks
    for row in range(NUMBER_OF_BRICK_ROWS):
        for number_of_brick in range(NUMBER_OF_BRICKS_IN_ROW):
            # (left, top, width, height)
            brick = pygame.Rect(number_of_brick * 60 + 10, 50 + row * 25, BRICK_WIDTH, BRICK_HEIGHT)
            draw.rect(surface=screen,
                      color=brick_color,
                      rect=brick)

    # Very important each frame we should use to  put your work on screen
    pygame.display.flip()
    time.sleep(5)

    pygame.quit()

import time
from pygame import draw
import pygame
import math
import random

BACKGROUND_COLOR = (255, 255, 255)
BALL_COLOR = (139, 170, 173)
RACKET_COLOR = (0, 0, 0)
BRICK_HEIGHT = 20
BRICK_WIDTH = 42
NUMBER_OF_BRICK_ROWS = 4
NUMBER_OF_BRICKS_IN_ROW = 18
RADIUS_SIZE = 15
RACKET_HEIGHT = 10
RACKET_WIDTH = 80


def start_new_game():
    game_screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    center_ball_position = pygame.Vector2(game_screen.get_width() / 2, game_screen.get_height() / 2)
    return center_ball_position


def is_ball_hitting_the_racket(player_racket, current_ball_position):
    # Here is the constraint for the x axis
    # We are declaring on a ball position compared to racket position
    result = player_racket.x + RADIUS_SIZE <= current_ball_position.x <= player_racket.x + RACKET_WIDTH - RADIUS_SIZE
    return result


if __name__ == '__main__':

    pygame.init()
    clock = pygame.time.Clock()
    # font = pygame.font.Font('fonts/ChrustyRock-ORLA.ttf', 32)
    white = (255, 255, 255)
    green = (0, 255, 0)
    brick_color = (185, 206, 212)
    blue = (0, 0, 128)

    WIDTH_SCREEN = 1080
    HEIGHT_SCREEN = 550

    # pygame setup
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

    # Initialization:
    racket = pygame.Rect(WIDTH_SCREEN / 2, HEIGHT_SCREEN - 20, RACKET_WIDTH, RACKET_HEIGHT)
    ball_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    step_y = 10

    while True:
        screen.fill(BACKGROUND_COLOR)
        # The following loop create a row of bricks
        for row in range(NUMBER_OF_BRICK_ROWS):
            for number_of_brick in range(NUMBER_OF_BRICKS_IN_ROW):
                # (left, top, width, height)
                brick = pygame.Rect(number_of_brick * 60 + 10,
                                    50 + row * 25,
                                    BRICK_WIDTH,
                                    BRICK_HEIGHT)

                draw.rect(surface=screen,
                          color=brick_color,
                          rect=brick)

        ball = pygame.draw.circle(screen, BALL_COLOR, ball_position, RADIUS_SIZE)

        # Handle_in_case_ball_hitting_the_ground
        if ball_position.y > HEIGHT_SCREEN - RADIUS_SIZE:
            print("You have reached the ground")
            ball_position = start_new_game()

        if ball_position.y > HEIGHT_SCREEN - 20 - RADIUS_SIZE:
            if is_ball_hitting_the_racket(player_racket=racket,
                                          current_ball_position=ball_position):
                # Changing direction of the ball
                step_y *= -1
                print('debug')

        # only for starting
        ball_position.x += 5  # random.randint(1, 5)
        ball_position.y += step_y  # random.randint(1, 10)

        draw.rect(surface=screen,
                  color=RACKET_COLOR,
                  rect=racket)

        for event in pygame.event.get():
            # here we are checking if the user wants to exit the game
            if event.type == pygame.QUIT:
                print('Mory is closing the game')
                exit(0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            print('Right was pressed')
            racket.move_ip(5, 0)
        elif keys[pygame.K_LEFT]:
            print('Left was pressed')
            racket.move_ip(-5, 0)

        pygame.draw.rect(screen, RACKET_COLOR, racket)

        # Very important each frame we should use to  put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate independent physics.
        dt = clock.tick(20) / 1000

    pygame.quit()

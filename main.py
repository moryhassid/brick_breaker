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
TOTAL_BRICKS = NUMBER_OF_BRICK_ROWS * NUMBER_OF_BRICKS_IN_ROW
RADIUS_SIZE = 15
RACKET_HEIGHT = 10
RACKET_WIDTH = 100
STEP_SIZE_OF_RACKET = 10
CEILING_GAP = 50
LEFT_SIDE_GAP = 10
CHANGE_SPEED_EVERY_X_BRICKS = 6


class Brick:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = True

    def get_brick_edge_in_x_axis(self):
        return LEFT_SIDE_GAP + self.x * 60

    def get_brick_edge_in_y_axis(self):
        return CEILING_GAP + self.y * 25 + BRICK_HEIGHT

    def is_ball_can_hit_the_brick(self, ball_position):
        if (self.get_brick_edge_in_y_axis() + RADIUS_SIZE >= ball_position.y and
                self.get_brick_edge_in_x_axis() < ball_position.x < self.get_brick_edge_in_x_axis() + BRICK_WIDTH):
            print(f'The Ball hit the brick (x ={self.x}, y = {self.y})')
            return True

        return False


def start_new_game():
    game_screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    center_ball_position = pygame.Vector2(game_screen.get_width() / 2, game_screen.get_height() / 2)
    return center_ball_position


def is_ball_hitting_the_racket(player_racket, current_ball_position):
    # Here is the constraint for the x axis
    # We are declaring on a ball position compared to racket position
    result = player_racket.x + RADIUS_SIZE <= current_ball_position.x <= player_racket.x + RACKET_WIDTH - RADIUS_SIZE
    return result


def is_ball_near_ground(ball_position_currently):
    return ball_position_currently.y >= HEIGHT_SCREEN - RACKET_HEIGHT - RADIUS_SIZE


def is_ball_hit_the_right_wall(ball_position_currently):
    return ball_position_currently.x >= WIDTH_SCREEN - RADIUS_SIZE


def is_ball_hit_the_left_wall(ball_position_currently):
    return ball_position_currently.x <= RADIUS_SIZE


def is_ball_hit_the_ceiling(ball_position_currently):
    return ball_position_currently.y <= RADIUS_SIZE


def init_position_for_all_bricks():
    bricks = []
    for row in range(NUMBER_OF_BRICK_ROWS):
        row_bricks = []
        for number_of_brick in range(NUMBER_OF_BRICKS_IN_ROW):
            # (left, top, width, height)
            current_brick = Brick(x=number_of_brick, y=row)
            row_bricks.append(current_brick)
        bricks.append(row_bricks)

    return bricks


def draw_bricks_on_screen():
    # The following loop create a row of bricks
    for row in range(NUMBER_OF_BRICK_ROWS):
        for number_of_brick in range(NUMBER_OF_BRICKS_IN_ROW):
            # (left, top, width, height)
            if bricks[row][number_of_brick].visible:
                brick = pygame.Rect(LEFT_SIDE_GAP + number_of_brick * 60,
                                    CEILING_GAP + row * 25,
                                    BRICK_WIDTH,
                                    BRICK_HEIGHT)

                draw.rect(surface=screen,
                          color=brick_color,
                          rect=brick)


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
    ball_speed_y = 10
    ball_speed_x = -5
    bricks_down_counter = 0
    bricks = init_position_for_all_bricks()
    speed_has_changed = False

    counter_ball_reached_the_ground = 0

    while True:
        screen.fill(BACKGROUND_COLOR)

        draw_bricks_on_screen()

        ball = pygame.draw.circle(screen, BALL_COLOR, ball_position, RADIUS_SIZE)

        # Handle_in_case_ball_hitting_the_ground
        if ball_position.y > HEIGHT_SCREEN - RADIUS_SIZE:
            print("You have reached the ground")
            ball_position = start_new_game()

        if is_ball_near_ground(ball_position_currently=ball_position):
            if is_ball_hitting_the_racket(player_racket=racket,
                                          current_ball_position=ball_position):
                # Changing direction of the ball
                ball_speed_y *= -1
                print('debug')
            else:
                counter_ball_reached_the_ground += 1
                if counter_ball_reached_the_ground < 3:
                    ball_position = start_new_game()
                else:
                    print('Game Over')
                    font = pygame.font.SysFont(None, 55)
                    game_over_text = font.render('Game Over', True, (255, 0, 0))
                    screen.blit(game_over_text, (screen.get_width() // 2 - 100, screen.get_height() // 2))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    print('Mory is closing the game')
                    pygame.quit()
                    exit(0)

        if is_ball_hit_the_right_wall(ball_position_currently=ball_position):
            print('You have hit the right wall')
            ball_speed_x *= -1

        if is_ball_hit_the_left_wall(ball_position_currently=ball_position):
            print('You have hit the left wall')
            ball_speed_x *= -1

        for row in range(NUMBER_OF_BRICK_ROWS):
            for number_of_brick in range(NUMBER_OF_BRICKS_IN_ROW):

                pygame.display.set_caption(f'Number of bricks down: {bricks_down_counter},'
                                           f' speed has changed: {speed_has_changed}, '
                                           f'{counter_ball_reached_the_ground}/3 Lives')

                if (bricks[row][number_of_brick].visible is True and
                        bricks[row][number_of_brick].is_ball_can_hit_the_brick(ball_position=ball_position)):
                    bricks[row][number_of_brick].visible = False
                    speed_has_changed = False
                    if bricks_down_counter > 0 and bricks_down_counter % CHANGE_SPEED_EVERY_X_BRICKS == 0:
                        speed_has_changed = True
                        ball_speed_y += 3

                    bricks_down_counter += 1
                    ball_speed_y *= -1

        if bricks_down_counter == TOTAL_BRICKS:
            print('Congrats you have finished the Game!! 😊')
            exit(0)

        if is_ball_hit_the_ceiling(ball_position_currently=ball_position):
            print('You have hit the left wall')
            ball_speed_y *= -1

        # only for starting
        ball_position.x += ball_speed_x
        ball_position.y += ball_speed_y

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
            print(f'{racket.x=}')
            if racket.x < WIDTH_SCREEN - RACKET_WIDTH:
                racket.move_ip(STEP_SIZE_OF_RACKET, 0)
        elif keys[pygame.K_LEFT]:
            print('Left was pressed')
            print(f'{racket.x=}')
            if racket.x > 0:
                racket.move_ip(-STEP_SIZE_OF_RACKET, 0)
        elif keys[pygame.K_ESCAPE]:
            print('Mory is closing the game, he has pressed Escape button')
            exit(0)

        pygame.draw.rect(screen, RACKET_COLOR, racket)

        # Very important each frame we should use to  put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate independent physics.
        dt = clock.tick(20) / 1000

    pygame.quit()

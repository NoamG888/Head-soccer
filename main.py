import pygame
from constants import *
from Text import Text


# displays an image on the screen
def add_image(image_path, x_position, y_position, width, height):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (width, height))
    screen.blit(image, (x_position, y_position))


# displays images on the screen using the "add_image" function
def goal_check(ball_rect, left_goal_rect, right_goal_rect, goal_counter1, goal_counter2):
    if ball_rect.right <= left_goal_rect.right and ball_rect.top >= left_goal_rect.bottom:
        goal_counter2.text += 1
        ball_rect = pygame.Rect((WINDOW_WIDTH-70) // 2, 50, 70, 70)
        return ball_rect
    if ball_rect.left >= right_goal_rect.left and ball_rect.top >= right_goal_rect.bottom:
        goal_counter1.text += 1
        ball_rect = pygame.Rect((WINDOW_WIDTH-50) // 2, 50, 70, 70)
        return ball_rect
    return ball_rect


def walls_ball_movement(ball_rect):
    if ball_rect.left < 0 or ball_rect.right > WINDOW_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > WINDOW_HEIGHT - 50:
        ball_speed[1] = -ball_speed[1]


# in charge of the ball's movement after a player hits it
def ball_movement(ball_rect, player_rect):
    if pygame.Rect.colliderect(ball_rect, player_rect):
        if player_rect.right >= ball_rect.centerx >= player_rect.left and player_rect.bottom >= ball_rect.centery >= player_rect.top:
            ball_speed[0] = -ball_speed[0]
            ball_speed[1] = -ball_speed[1]
        elif player_rect.right >= ball_rect.centerx >= player_rect.left:
            ball_speed[1] = -ball_speed[1]
        elif player_rect.bottom >= ball_rect.centery >= player_rect.top:
            ball_speed[0] = -ball_speed[0]
        else:
            ball_speed[0] = -ball_speed[0]
            ball_speed[1] = -ball_speed[1]


def player_movement(event, player1_loc, player2_loc):
    if event.key == pygame.K_RIGHT:
        player1_loc[0] += 10
    if event.key == pygame.K_LEFT:
        player1_loc[0] -= 10

    if event.key == pygame.K_d:
        player2_loc[0] += 10
    if event.key == pygame.K_a:
        player2_loc[0] -= 10

    return player1_loc, player2_loc


def jump(direction, loc):
    if direction == "up":
        if loc[1] <= PLAYER_MIN_Y:
            direction = "down"
        else:
            loc[1] -= 5
        pygame.time.delay(10)
        return direction, loc
    else:
        if loc[1] >= PLAYER_MAX_Y:
            direction = ""
        else:
            loc[1] += 5
        return direction, loc


def main():
    global screen
    pygame.init()
    player1_loc = [700, 600]
    player2_loc = [100, 600]
    player1_dir = ""
    player2_dir = ""
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # ball parameters
    ball = pygame.image.load("images/Untitled-3.png")
    ball = pygame.transform.scale(ball, (50, 50))
    ball_rect = ball.get_rect()
    global ball_speed
    ball_speed = [3, 3]
    square1 = pygame.Rect(player1_loc[0], player1_loc[1], 100, 100)
    square2 = pygame.Rect(player2_loc[0], player2_loc[1], 100, 100)
    left_goal_top = pygame.Rect(0, WINDOW_HEIGHT / 2, 220, 5)
    right_goal_top = pygame.Rect(WINDOW_WIDTH - 250, WINDOW_HEIGHT / 2, 220, 5)
    goal_counter1 = Text(0, 250, 50, 100, WHITE, ARIEL)
    goal_counter2 = Text(0, WINDOW_WIDTH - 250, 50, 100, WHITE, ARIEL)
    # run loop
    running = True
    while running:
        ball_rect = goal_check(ball_rect, left_goal_top, right_goal_top, goal_counter1, goal_counter2)
        # ball movement
        ball_rect = ball_rect.move(ball_speed)
        walls_ball_movement(ball_rect)
        ball_movement(ball_rect, square1)
        ball_movement(ball_rect, square2)
        ball_movement(ball_rect, left_goal_top)
        ball_movement(ball_rect, right_goal_top)
        if player1_dir == "up" or player1_dir == "down":
            player1_dir, player1_loc = (player1_dir, player1_loc)
        if player2_dir == "up" or player2_dir == "down":
            player2_dir, player2_loc = (player2_dir, player2_loc)
        pygame.display.flip()
        pygame.time.wait(3)
        # display screen
        field = pygame.image.load("images/מגרש.gif")
        field = pygame.transform.scale(field, (WINDOW_WIDTH, WINDOW_HEIGHT))
        screen.blit(field, (0, 0))
        pygame.draw.rect(screen, (0, 150, 0), square1)
        pygame.draw.rect(screen, (150, 0, 0), square2)
        # display ball
        screen.blit(ball, ball_rect)
        goal_counter1.display(screen)
        goal_counter2.display(screen)
        # checks for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                # controls player movement
                if event.key == pygame.K_UP:
                    player1_dir = "up"
                if event.key == pygame.K_w:
                    player2_dir = "up"
                player1_loc, player2_loc = player_movement(event, player1_loc, player2_loc)
                square1 = pygame.Rect(player1_loc[0], player1_loc[1], 100, 100)
                square2 = pygame.Rect(player2_loc[0], player2_loc[1], 100, 100)
                pygame.draw.rect(screen, (0, 150, 0), square1)
                pygame.draw.rect(screen, (150, 0, 0), square2)
        # updates the screen
        pygame.display.flip()
    # quits the game
    pygame.quit()


# runs "main" function

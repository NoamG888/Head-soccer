import pygame
from constants import *


# displays an image on the screen
def add_image(image_path, x_position, y_position, width, height):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (width, height))
    screen.blit(image, (x_position, y_position))


# displays images on the screen using the "add_image" function
def load_images():
    pass


# in charge of the ball's movement after a player hits it
def ball_movement(ball_rect, player_rect1, player_rect2):
    if ball_rect.left < 0 or ball_rect.right > WINDOW_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > WINDOW_HEIGHT:
        ball_speed[1] = -ball_speed[1]

    if pygame.Rect.colliderect(ball_rect, player_rect1):
        if player_rect1.right >= ball_rect.centerx >= player_rect1.left:
            ball_speed[1] = -ball_speed[1]
        else:
            ball_speed[0] = -ball_speed[0]
    if pygame.Rect.colliderect(ball_rect, player_rect2):
        if player_rect2.right >= ball_rect.centerx >= player_rect2.left:
            ball_speed[1] = -ball_speed[1]
        else:
            ball_speed[0] = -ball_speed[0]


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
        loc[1] -= 20
        pygame.time.delay(20)
        return direction, loc
    else:
        if loc[1] >= PLAYER_MAX_Y:
            direction = "up"
        loc[1] += 20
        return direction, loc


def main():
    global screen
    pygame.init()
    player1_loc = [700, 300]
    player2_loc = [100, 300]
    player1_dir = "up"
    player2_dir = "up"
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # ball parameters
    ball = pygame.image.load("images/Untitled-3.png")
    ball = pygame.transform.scale(ball, (70, 70))
    ball_rect = ball.get_rect()
    global ball_speed
    ball_speed = [2, 2]
    square1 = pygame.Rect(player1_loc[0], player1_loc[1], 100, 100)
    square2 = pygame.Rect(player2_loc[0], player2_loc[1], 100, 100)
    # run loop
    running = True
    while running:
        # ball movement
        ball_rect = ball_rect.move(ball_speed)
        ball_movement(ball_rect, square1, square2)
        pygame.display.flip()
        pygame.time.wait(10)
        # display screen
        field = pygame.image.load("images/מגרש.gif")
        field = pygame.transform.scale(field, (900, 506.25))
        screen.blit(field, (0, 0))
        pygame.draw.rect(screen, (0, 150, 0), square1)
        pygame.draw.rect(screen, (150, 0, 0), square2)
        # display ball
        screen.blit(ball, ball_rect)
        # checks for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # controls player movement
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
main()

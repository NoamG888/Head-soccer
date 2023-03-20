import pygame
from constants import *
from Buttons import Buttons


# displays an image on the screen
def add_image(image_path, x_position, y_position, width, height):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (width, height))
    screen.blit(image, (x_position, y_position))


# displays images on the screen using the "add_image" function
def load_images():
    pass


# in charge of the ball's movement after a player hits it
def ball_movement(ball_rect, ball_speed, player_rect):
    if ball_rect.left < 0 or ball_rect.right > WINDOW_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > WINDOW_HEIGHT:
        ball_speed[1] = -ball_speed[1]
    if player_rect.bottom >= ball_rect.top >= player_rect.top:
        if ball_rect.left == player_rect.right or ball_rect.right == player_rect.left:
            ball_speed[0] = -ball_speed[0]
    if player_rect.left <= ball_rect.left <= player_rect.right:
        if ball_rect.top == player_rect.bottom or ball_rect.bottom == player_rect.top:
            ball_speed[1] = -ball_speed[1]


def player_movement():
    pass


def main():
    global screen
    pygame.init()
    player1_loc = []
    player2_loc = []
    player1_dir = "up"
    player2_dir = "up"
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # ball parameters
    ball = pygame.image.load("C:/Users/noamg/Downloads/walk-0.png")
    ball_rect = ball.get_rect()
    ball_speed = [2, 2]
    square = pygame.Rect(300, 100, 400, 200)
    # run loop
    running = True
    while running:
        # ball movement
        ball_movement(ball_rect, ball_speed, square)
        ball_rect = ball_rect.move(ball_speed)
        pygame.time.wait(5)
        # display screen
        screen.fill(WHITE)
        pygame.draw.rect(screen, (0, 150, 0), square)
        # display ball
        screen.blit(ball, ball_rect)
        # update screen
        pygame.display.flip()
        # checks for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # controls player movement
                player1_dir, player1_loc, player2_dir, player2_loc = player_movement(event, player1_loc, player2_loc, player1_dir, player2_dir)
        # updates the screen
        pygame.display.flip()
    # quits the game
    pygame.quit()


# runs "main" function
main()

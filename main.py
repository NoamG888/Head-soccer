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
def ball_movement(player_x, player_y, ball_x, ball_y, ball, player):
    pass


def player_movement():
    pass


def main():
    global screen
    pygame.init()
    keys_player1 = [False, False, False]
    keys_player2 = [False, False, False]
    player1_loc = []
    player2_loc = []
    direction1 = "up"
    direction2 = "up"
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    ball = pygame.image.load("C:/Users/noamg/Downloads/walk-0.png")
    ball_rect = ball.get_rect()
    ball_speed = [2, 2]
    running = True
    while running:
        ball_rect = ball_rect.move(ball_speed)
        if ball_rect.left < 0 or ball_rect.right > WINDOW_WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball_rect.top < 0 or ball_rect.bottom > WINDOW_HEIGHT:
            ball_speed[1] = -ball_speed[1]
        screen.fill(WHITE)
        screen.blit(ball, ball_rect)
        pygame.display.flip()
        pygame.time.wait(10)
        ball_speed[0] - 0.1, ball_speed[1] - 0.1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                player_movement(keys_player1, keys_player2, event, player1_loc, player2_loc, direction1, direction2)
        pygame.display.flip()
    pygame.quit()


main()

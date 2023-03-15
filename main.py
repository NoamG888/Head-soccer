import pygame
from constants import *
# from Buttons import Buttons


# displays an image on the screen
def add_image(image_path, x_position, y_position, width, height):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (width, height))
    screen.blit(image, (x_position, y_position))


# displays images on the screen using the "add_image" function
def load_images():
    pass


def ball_movement():
    pass


def player_movement(keys_player1, keys_player2, pressed_key, player1_loc, player2_loc, direction1, direction2):
    # check the keys for player 1
    if pressed_key == pygame.K_RIGHT:
        keys_player1[0] = True
    elif pressed_key == pygame.K_LEFT:
        keys_player1[1] = True
    elif pressed_key == pygame.K_UP:
        keys_player1[2] = True

    # check the keys for player 2

    elif pressed_key == pygame.K_d:
        keys_player2[0] = True
    elif pressed_key == pygame.K_a:
        keys_player2[1] = True
    elif pressed_key == pygame.K_w:
        keys_player2[2] = True

    # moving the players locations
    if keys_player1[0]:
        player1_loc[0] += 5
    if keys_player1[1]:
        player1_loc[0] -= 5
    if keys_player1[2]:
        direction1 = jump(player1_loc, direction1)

    if keys_player2[0]:
        player2_loc[0] += 5
    if keys_player2[1]:
        player2_loc[0] -= 5
    if keys_player2[2]:
        direction2 = jump(player2_loc, direction2)


def jump(player_loc, direction):
    if direction == "up":
        if player_loc[1] > PLAYER_MIN_Y:
            player_loc[1] -= 5
        else:
            direction = "down"
    if direction == "down":
        if player_loc[1] < PLAYER_MAX_Y:
            player_loc[1] += 5
        else:
            direction = "up"
    return direction


def main():
    global screen
    pygame.init()
    keys_player1 = [False, False, False]
    keys_player2 = [False, False, False]
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    player1_loc = []
    player2_loc = []
    direction1 = "up"
    direction2 = "up"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                player_movement(keys_player1, keys_player2, event, player1_loc, player2_loc, direction1, direction2)
    pygame.quit()


main()

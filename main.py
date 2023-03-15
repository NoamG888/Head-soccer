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


def ball_movement():
    pass


def player_movement():
    pass


def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()


main()

import pygame
from constants import *


class Player:

    def __init__(self, player_width, player_height, image_path, player_keys, direction, player_loc):
        self.player_width = player_width
        self.player_height = player_height
        self.image_path = image_path
        self.player_keys = player_keys
        self.direction = direction
        self.player_loc = player_loc

    def player_movement(self, player_keys, player1_player_loc):
        if player_keys[0] and player1_player_loc[0] <= X_RIGHT_GOAL - 100:
            self.player_loc[0] += 10
        if player_keys[1] and player1_player_loc[0] >= X_LEFT_GOAL + 250:
            self.player_loc[0] -= 10
        return self.player_loc

    def change_keys_true(self, event, player_keys):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.player_keys[0] = True
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.player_keys[1] = True
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.player_keys[2] = True

        return self.player_keys

    def change_keys_false(self, event, player_keys):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            player_keys[0] = False
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            player_keys[1] = False

        return self.player_keys

    def jump(self, direction, player_loc):
        if direction:
            if player_loc[1] <= PLAYER_MIN_Y:
                direction = False
            else:
                player_loc[1] -= 5
            return self.direction, self.player_loc
        if not direction:
            if player_loc[1] <= PLAYER_MAX_Y:
                player_loc[1] += 5
            return self.direction, self.player_loc

import pygame
from constants import *
from Text import Text


# displays an image on the screen
def add_image(image_path, x_position, y_position, width, height):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (width, height))
    screen.blit(image, (x_position, y_position))


def goal_check(ball_rect, left_goal_rect, right_goal_rect, goal_counter1, goal_counter2, goal_text):
    if ball_rect.right <= left_goal_rect.right and ball_rect.top >= left_goal_rect.bottom:
        goal_counter2.text += 1
        goal_text.display(screen)
        ball_rect = pygame.Rect(0, 50, 70, 70)
        pygame.display.update()
        pygame.time.delay(3000)
        return ball_rect
    if ball_rect.left >= right_goal_rect.left and ball_rect.top >= right_goal_rect.bottom:
        goal_counter1.text += 1
        goal_text.display(screen)
        ball_rect = pygame.Rect(WINDOW_WIDTH - 70, 50, 70, 70)
        pygame.display.update()
        pygame.time.delay(3000)
        return ball_rect
    return ball_rect


def walls_ball_movement(ball_rect):
    if ball_speed[0] > 0:
        ball_speed[0] = 3.5
    else:
        ball_speed[0] = -3.5
    if ball_rect.left < 0 or ball_rect.right > WINDOW_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > WINDOW_HEIGHT - 50:
        ball_speed[1] = -ball_speed[1]


# in charge of the ball's movement after a player hits it
def ball_movement(ball_rect, player_rect):
    if ball_speed[1] < 3.5:
        ball_speed[1] += 0.015
    if pygame.Rect.colliderect(ball_rect, player_rect):
        if ball_speed[1] < 0:
            ball_speed[1] = -3.5
        else:
            ball_speed[1] = 3.5
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


def change_keys_true(event, player1_keys, player2_keys):
    if event.key == pygame.K_RIGHT:
        player1_keys[0] = True
    if event.key == pygame.K_LEFT:
        player1_keys[1] = True
    if event.key == pygame.K_UP:
        player1_keys[2] = True

    if event.key == pygame.K_d:
        player2_keys[0] = True
    if event.key == pygame.K_a:
        player2_keys[1] = True
    if event.key == pygame.K_w:
        player2_keys[2] = True

    return player1_keys, player2_keys


def change_keys_false(event, player1_keys, player2_keys):
    if event.key == pygame.K_RIGHT:
        player1_keys[0] = False
    if event.key == pygame.K_LEFT:
        player1_keys[1] = False

    if event.key == pygame.K_d:
        player2_keys[0] = False
    if event.key == pygame.K_a:
        player2_keys[1] = False

    return player1_keys, player2_keys


def player_movement(player1_keys, player2_keys, player1_loc, player2_loc):
    if player1_keys[0] and player1_loc[0] <= X_RIGHT_GOAL - 100:
        if player1_loc[0] + 100 != player2_loc[0] or player1_loc[1] != player2_loc[1]:
            player1_loc[0] += 10

    if player1_keys[1] and player1_loc[0] >= X_LEFT_GOAL + 250:
        if player1_loc[0] != player2_loc[0] + 100 or player1_loc[1] != player2_loc[1]:
            player1_loc[0] -= 10

    if player2_keys[0] and player2_loc[0] <= X_RIGHT_GOAL - 100:
        if player1_loc[0] != player2_loc[0] + 100 or player1_loc[1] != player2_loc[1]:
            player2_loc[0] += 10

    if player2_keys[1] and player2_loc[0] >= X_LEFT_GOAL + 250:
        if player1_loc[0] + 100 != player2_loc[0] or player1_loc[1] != player2_loc[1]:
            player2_loc[0] -= 10

    return player1_loc, player2_loc


def jump(direction, loc, other_player_loc):
    if direction:
        if loc[1] <= PLAYER_MIN_Y:
            if loc[1] - 100 <= other_player_loc[1] and (loc[0] - other_player_loc[0] >= 100 or other_player_loc[0] - loc[0] >= 100):
                direction = False
            else:
                direction = True
        else:
            loc[1] -= 6
        return direction, loc
    if not direction:
        if loc[1] <= PLAYER_MAX_Y:
            if loc[1] <= other_player_loc[1] and (loc[0] - other_player_loc[0] >= 100 or other_player_loc[0] - loc[0] >= 100):
                loc[1] += 6
        return direction, loc


def counter_to_string(counter):
    min = str(counter // 60)
    sec = str(counter % 60)
    together = (min + ":" + sec)
    return together


def win_check(goal_counter1, goal_counter2):
    if goal_counter1 != goal_counter2:
        return True


def main():
    global screen
    pygame.init()
    counter_time = 90
    counter_text = counter_to_string(counter_time)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont(ARIEL, 100)
    player1_loc = [800, PLAYER_MAX_Y]
    player2_loc = [300, PLAYER_MAX_Y]
    player1_keys = [False, False, False]
    player2_keys = [False, False, False]
    player1_dir = ""
    player2_dir = ""
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # ball parameters
    ball = pygame.image.load("images/Untitled-3.png")
    ball = pygame.transform.scale(ball, (50, 50))
    ball_rect = ball.get_rect()
    global ball_speed
    ball_speed = [3.5, 3.5]
    player1_image = pygame.image.load("images/צילום-מסך-2-של-נועם.png")
    player1_image = pygame.transform.scale(player1_image, (150, 150))
    player2_image = pygame.image.load("images/צילום-מסך-2-של-נועם.png")
    player2_image = pygame.transform.scale(player2_image, (150, 150))
    left_goal_top = pygame.Rect(X_LEFT_GOAL, Y_GOAL, 220, 5)
    right_goal_top = pygame.Rect(X_RIGHT_GOAL, Y_GOAL, 220, 5)
    goal_counter1 = Text(0, 250, 50, 100, WHITE, ARIEL)
    goal_counter2 = Text(0, WINDOW_WIDTH - 250, 50, 100, WHITE, ARIEL)
    goal_text = Text("goal!!!", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 150, WHITE, ARIEL)
    # run loop
    running = True
    while running:
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
        screen.blit(player1_image, (player1_loc[0], player1_loc[1]))
        screen.blit(player2_image, (player2_loc[0], player2_loc[1]))
        # display ball
        screen.blit(ball, ball_rect)
        goal_counter1.display(screen)
        goal_counter2.display(screen)
        # checks for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.USEREVENT:
                if counter_time == 0:
                    if win_check(goal_counter1.text, goal_counter2.text):
                        pygame.quit()
                    else:
                        counter_time = 45
                else:
                    counter_time -= 1
                counter_text = counter_to_string(counter_time)
            if event.type == pygame.KEYDOWN:
                # controls player movement
                player1_keys, player2_keys = change_keys_true(event, player1_keys, player2_keys)
            if event.type == pygame.KEYUP:
                player1_keys, player2_keys = change_keys_false(event, player1_keys, player2_keys)
        player1_loc, player2_loc = player_movement(player1_keys, player2_keys, player1_loc, player2_loc)
        player1_keys[2], player1_loc = jump(player1_keys[2], player1_loc, player2_loc)
        player2_keys[2], player2_loc = jump(player2_keys[2], player2_loc, player1_loc)
        player1_rect = pygame.Rect(player1_loc[0], player1_loc[1], 150, 150)
        player2_rect = pygame.Rect(player2_loc[0], player2_loc[1], 150, 150)
        screen.blit(player1_image, (player1_loc[0], player1_loc[1]))
        screen.blit(player2_image, (player2_loc[0], player2_loc[1]))
        screen.blit(font.render(counter_text, True, WHITE), ((WINDOW_WIDTH / 2) - 100, 25))
        ball_rect = goal_check(ball_rect, left_goal_top, right_goal_top, goal_counter1, goal_counter2, goal_text)
        # ball movement
        ball_rect = ball_rect.move(ball_speed)
        walls_ball_movement(ball_rect)
        ball_movement(ball_rect, player1_rect)
        ball_movement(ball_rect, player2_rect)
        ball_movement(ball_rect, left_goal_top)
        ball_movement(ball_rect, right_goal_top)
        # updates the scree
        pygame.display.flip()
    # quits the game
    pygame.quit()


# runs "main" function
main()

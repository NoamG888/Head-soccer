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
        player1_loc[0] += 6
    if player1_keys[1] and player1_loc[0] >= X_LEFT_GOAL + 250:
        player1_loc[0] -= 6

    if player2_keys[0] and player2_loc[0] <= X_RIGHT_GOAL - 100:
        player2_loc[0] += 6
    if player2_keys[1] and player2_loc[0] >= X_LEFT_GOAL + 250:
        player2_loc[0] -= 6

    return player1_loc, player2_loc


def jump(direction, loc):
    if direction:
        if loc[1] <= PLAYER_MIN_Y:
            direction = False
        else:
            loc[1] -= 5
        return direction, loc
    if not direction:
        if loc[1] <= PLAYER_MAX_Y:
            loc[1] += 5
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
    clock = pygame.time.Clock()
    counter_time = 10
    counter_text = counter_to_string(counter_time)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont(ARIEL, 100)
    player1_loc = [900, PLAYER_MAX_Y]
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
    square1 = pygame.Rect(player1_loc[0], player1_loc[1], 100, 100)
    square2 = pygame.Rect(player2_loc[0], player2_loc[1], 100, 100)
    left_goal_top = pygame.Rect(X_LEFT_GOAL, Y_GOAL, 220, 5)
    right_goal_top = pygame.Rect(X_RIGHT_GOAL, Y_GOAL, 220, 5)
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
        player1_keys[2], player1_loc = jump(player1_keys[2], player1_loc)
        player2_keys[2], player2_loc = jump(player2_keys[2], player2_loc)
        square1 = pygame.Rect(player1_loc[0], player1_loc[1], 100, 100)
        square2 = pygame.Rect(player2_loc[0], player2_loc[1], 100, 100)
        pygame.draw.rect(screen, (0, 150, 0), square1)
        pygame.draw.rect(screen, (150, 0, 0), square2)
        screen.blit(font.render(counter_text, True, WHITE), ((WINDOW_WIDTH / 2) - 100, 25))
        # updates the scree
        pygame.display.flip()
    # quits the game
    pygame.quit()


# runs "main" function
main()

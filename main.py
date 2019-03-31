# 26 x37
import pygame
import random
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (18, 120, 12)
GREEN = (53, 222, 0)
RED = (255, 0, 0)

pygame.init()
pygame.font.init()

# Set the width and height of the screen [width, height]
size = (1263, 741)
screen = pygame.display.set_mode(size, pygame.NOFRAME)
# pygame.NOFRAME

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()
game_size = [217, 180, 554, 374]

background = pygame.image.load("Snake.png").convert()

current_pos = [1, 1]
score = 1
snake_tuple = [[1, 1]]
apple = [random.randrange(0, 36), random.randrange(0, 25)]
direction = 1
update = True
best = 0
is_game_over = False
walls = True
# 0 is up, 1 is down, 2 is left, 3 is right

zero  = pygame.image.load('zero.png').convert()
one   = pygame.image.load('one.png').convert()
two   = pygame.image.load('two.png').convert()
three = pygame.image.load('three.png').convert()
four  = pygame.image.load('four.png').convert()
five  = pygame.image.load('five.png').convert()
six   = pygame.image.load('six.png').convert()
seven = pygame.image.load('seven.png').convert()
eight = pygame.image.load('eight.png').convert()
nine  = pygame.image.load('nine.png').convert()

all_nums = [zero, one, two, three, four, five, six, seven, eight, nine]
for nums in range(len(all_nums)):
    all_nums[nums].set_colorkey((22, 50, 76))

game_over = pygame.image.load('game_over.jpg').convert()
pause = pygame.image.load('pause.png').convert()

# background = pygame.transform.scale(background, size)


def grid_pos1(grid_pos_x, grid_pos_y):
    return [int(217 + (554 / 37 * grid_pos_x)), int(180 + (374 / 26 * grid_pos_y)), int(554/37) + 1, int(374/26) + 1]


def grid_pos2(grid_pos_x, grid_pos_y):
    return [int(218+(554 / 37 * grid_pos_x)), int(181+(374 / 26 * grid_pos_y)), int(554/37 - 1), int(374/26 - 1)]


def draw_rect(grid_pos, color=DARK_GREEN, outline=1, color2=GREEN):
    pygame.draw.rect(screen, color, grid_pos1(grid_pos[0], grid_pos[1]))
    if outline == 1:
        pygame.draw.rect(screen, color2, grid_pos2(grid_pos[0], grid_pos[1]))


def draw_num(num, cursor_input):
    split_score = list(map(int, str(num)))
    cursor_pos = cursor_input
    for digit in split_score:
        if digit == 0:
            screen.blit(zero, [cursor_pos[0], cursor_pos[1] + 2])
        elif digit == 1:
            screen.blit(one, [cursor_pos[0], cursor_pos[1] + 1])
        elif digit == 2:
            screen.blit(two, cursor_pos)
        elif digit == 3:
            screen.blit(three, cursor_pos)
        elif digit == 4:
            screen.blit(four, [cursor_pos[0], cursor_pos[1] + 1])
        elif digit == 5:
            screen.blit(five, cursor_pos)
        elif digit == 6:
            screen.blit(six, [cursor_pos[0], cursor_pos[1] + 1])
        elif digit == 7:
            screen.blit(seven, cursor_pos)
        elif digit == 8:
            screen.blit(eight, cursor_pos)
        elif digit == 9:
            screen.blit(nine, [cursor_pos[0], cursor_pos[1] + 1])
        cursor_pos[0] += 11

# -------- Main Program Loop -----------

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 1:
                direction = 0
            if event.key == pygame.K_DOWN and direction != 0:
                direction = 1
            if event.key == pygame.K_LEFT and direction != 3:
                direction = 2
            if event.key == pygame.K_RIGHT and direction != 2:
                direction = 3
            if event.key == pygame.K_TAB:
                score += 4
            if event.key == pygame.K_w:
                walls = not walls
            if event.key == pygame.K_SPACE:
                if not is_game_over:
                    update = not update
                if is_game_over:
                    current_pos = [1, 1]
                    score = 1
                    snake_tuple = [[1, 1]]
                    apple = [random.randrange(0, 36), random.randrange(0, 25)]
                    direction = 1
                    update = True
                    is_game_over = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen.get_at(pygame.mouse.get_pos()) == (51, 51, 51, 255) or screen.get_at(pygame.mouse.get_pos()) == (212, 212, 212, 255):
                current_pos = [1, 1]
                score = 1
                snake_tuple = [[1, 1]]
                apple = [random.randrange(0, 36), random.randrange(0, 25)]
                direction = 1
                update = True
                is_game_over = False

            if pygame.mouse.get_pos()[0] >= 1230 and pygame.mouse.get_pos()[1] <= 20:
                done = True


    hit = 0
    for seg in snake_tuple:
        if seg[0] == apple[0] and seg[1] == apple[1]:
            score += 4
            apple = [random.randrange(0, 36), random.randrange(0, 25)]
        if current_pos == seg:
            hit += 1
        if hit == 2:
            update = False
            is_game_over = True

    if update: # Update controls this
        if direction == 0:
            current_pos[1] -= 1
            snake_tuple.append([int(current_pos[0]), int(current_pos[1])])
        if direction == 1:
            current_pos[1] += 1
            snake_tuple.append([int(current_pos[0]), int(current_pos[1])])
        if direction == 2:
            current_pos[0] -= 1
            snake_tuple.append([int(current_pos[0]), int(current_pos[1])])
        if direction == 3:
            current_pos[0] += 1
            snake_tuple.append([int(current_pos[0]), int(current_pos[1])])

    while len(snake_tuple) > score: # Keeping snake at right length
        snake_tuple.pop(0)

    # --- Game logic should go here
    screen.blit(background, [0, 0])
    # --- Drawing code should go here
    pygame.draw.rect(screen, BLACK, game_size)
    draw_rect(apple, RED, BLACK, 0)
    for segment in snake_tuple:
        draw_rect(segment)

    if ((current_pos[1] == 26 or current_pos[1] == -1) and 0 <= current_pos[0] <= 36) or (current_pos[0] == -1 and
            0 <= current_pos[1] <= 25) or ((current_pos[0] == 37 and 0 <= current_pos[1] <= 24 and not walls) or (current_pos[0] == 37 and 0 <= current_pos[1] <= 25 and walls)): # Right wall): # Hits wall
            update = False
            is_game_over = True

    if is_game_over:
        draw_rect(current_pos, WHITE, WHITE, 0)
        screen.blit(game_over, [game_size[2]/2 - game_over.get_size()[0]/2 + game_size[0], game_size[3]/2 - game_over.get_size()[1]/2 + game_size[1]])
        draw_num(score, [517, 337])
        if score > best:
            best = score

    if not is_game_over and not update:
        screen.blit(pause, [game_size[2] / 2 - pause.get_size()[0] / 2 + game_size[0],
                                game_size[3] / 2 - pause.get_size()[1] / 2 + game_size[1]])

    cursor_pos_score = [290, 572]
    cursor_pos_best = [730, 573]
    draw_num(score, cursor_pos_score)
    draw_num(best, cursor_pos_best)
    if walls:
        pygame.draw.rect(screen, BLACK, [5, 5, 2, 2])

    pygame.display.flip()

    clock.tick(13) # Frames per second
pygame.quit()

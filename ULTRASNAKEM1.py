import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
window_width, window_height = 600, 400
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Simple Snake Game')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)

# Set up the snake
snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1

# Set up the food
foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

# Initialize the game loop variables
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 35)
game_over = False
x1_change = 0
y1_change = 0
x1 = window_width / 2
y1 = window_height / 2

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], snake_block, snake_block])

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    # Check for boundary collision
    if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
        game_over = True

    # Move the snake
    x1 += x1_change
    y1 += y1_change
    game_display.fill(white)
    pygame.draw.rect(game_display, green, [foodx, foody, snake_block, snake_block])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for self collision
    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    draw_snake(snake_block, snake_list)
    pygame.display.update()

    # Check for food collision
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
        snake_length += 1

    clock.tick(snake_speed)

pygame.quit()
quit()

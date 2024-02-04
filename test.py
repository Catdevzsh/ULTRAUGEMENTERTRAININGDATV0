import pygame
import sys

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

# Font setup
font = pygame.font.Font(None, 74)

# Game states
game_states = {'menu': True, 'game': False}

# Function to show the main menu
def show_menu(screen):
    screen.fill(BLACK)
    menu_text = font.render('ULTRA PONG', True, WHITE)
    text_rect = menu_text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(menu_text, text_rect)
    pygame.display.flip()

# Function to start the game
def start_game(screen):
    # Game objects
    ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
    paddle1 = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
    paddle2 = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

    # Game variables
    ball_speed = [2, 2]
    paddle_speed = 2

    # Game loop
    while game_states['game']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_states['game'] = False
                    game_states['menu'] = True

        # Ball movement
        ball.move_ip(ball_speed)
        if ball.left < 0 or ball.right > screen_width:
            ball_speed[0] *= -1
        if ball.top < 0 or ball.bottom > screen_height:
            ball_speed[1] *= -1

        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle1.move_ip(0, -paddle_speed)
        if keys[pygame.K_DOWN]:
            paddle1.move_ip(0, paddle_speed)
        if keys[pygame.K_w]:
            paddle2.move_ip(0, -paddle_speed)
        if keys[pygame.K_s]:
            paddle2.move_ip(0, paddle_speed)

        # Ball and paddle collision
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_speed[0] *= -1

        # Drawing everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, paddle1)
        pygame.draw.rect(screen, WHITE, paddle2)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (screen_width / 2, 0), (screen_width / 2, screen_height))

        pygame.display.flip()
        clock.tick(60)

# Main loop
while True:
    if game_states['menu']:
        show_menu(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_states['menu'] = False
                    game_states['game'] = True
    elif game_states['game']:
        start_game(screen)

import pygame
import random

# Initialize Pygame
pygame.init()

# Define screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([35, 25])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - 50

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 5
        if key[pygame.K_RIGHT]:
            self.rect.x += 5

        # Keep the player on the screen
        self.rect.x = max(self.rect.x, 0)
        self.rect.x = min(self.rect.x, SCREEN_WIDTH - self.rect.width)

# Invader class
class Invader(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([35, 25])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += 1
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = -35

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0:
            self.kill()

# Create sprite groups
player = Player()
player_group = pygame.sprite.Group(player)
invaders = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create invaders
for i in range(5):
    for j in range(10):
        invader = Invader(j * 40, i * 30)
        invaders.add(invader)

# Main game loop
running = True
score = 0
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                bullets.add(bullet)
                player_group.add(bullet)

    # Update sprite groups
    player_group.update()
    invaders.update()
    bullets.update()

    # Collision detection
    for bullet in bullets:
        hit_list = pygame.sprite.spritecollide(bullet, invaders, True)
        for hit in hit_list:
            score += 10
            bullet.kill()

    # Drawing
    screen.fill(BLACK)
    player_group.draw(screen)
    invaders.draw(screen)
    bullets.draw(screen)

    # Display the score
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    # Refresh screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()

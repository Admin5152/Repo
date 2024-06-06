#Ping Pong

import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20
BALL_SPEED_X = 10
BALL_SPEED_Y = 10
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCORE_FONT_SIZE = 36

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Create the font for the score board
score_font = pygame.font.Font(None, SCORE_FONT_SIZE)

# Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dy):
        self.rect.y += dy
        # Keep paddle within bounds
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed_x = BALL_SPEED_X * random.choice([-1, 1])
        self.speed_y = BALL_SPEED_Y * random.choice([-1, 1])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Ball bounces off the top and bottom walls
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed_y *= -1

        # Ball goes out of bounds
        if self.rect.left < 0:
            right_score.add_point()
            self.reset_position()
        elif self.rect.right > SCREEN_WIDTH:
            left_score.add_point()
            self.reset_position()

        # Ball bounces off paddles
        if pygame.sprite.spritecollide(self, paddles, False):
            self.speed_x *= -1

    def reset_position(self):
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed_x *= random.choice([-1, 1])
        self.speed_y *= random.choice([-1, 1])

# Scoreboard class
class ScoreBoard:
    def __init__(self):
        self.score = 0

    def add_point(self):
        self.score += 1

    def render(self, x, y):
        score_text = score_font.render(str(self.score), True, WHITE)
        screen.blit(score_text, (x, y))

# Create paddles and ball
left_paddle = Paddle(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
right_paddle = Paddle(SCREEN_WIDTH - 30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball()

# Create sprite groups
paddles = pygame.sprite.Group()
paddles.add(left_paddle, right_paddle)

all_sprites = pygame.sprite.Group()
all_sprites.add(left_paddle, right_paddle, ball)

# Create scoreboards for each player
left_score = ScoreBoard()
right_score = ScoreBoard()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control paddles
    keys = pygame.key.get_pressed()

    # Left paddle control
    if keys[pygame.K_w]:
        left_paddle.move(-PADDLE_SPEED)
    if keys[pygame.K_s]:
        left_paddle.move(PADDLE_SPEED)

    # Right paddle control
    if keys[pygame.K_UP]:
        right_paddle.move(-PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        right_paddle.move(PADDLE_SPEED)

    # Update ball and all sprites
    all_sprites.update()

    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Render the scoreboards
    left_score.render(50, 10)
    right_score.render(SCREEN_WIDTH - 100, 10)

    pygame.display.flip()

    pygame.time.delay(30)

pygame.quit()

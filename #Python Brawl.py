#Python Brawl

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_WIDTH = 50
CHARACTER_HEIGHT = 100
CHARACTER_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting Game")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Define the Character class
class Character(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((CHARACTER_WIDTH, CHARACTER_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.is_attacking = False
        self.attack_timer = 0

    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def attack(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = 30  # Attack lasts 30 frames

    def update(self):
        if self.is_attacking:
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.is_attacking = False

# Create two characters
player1 = Character(WHITE, 100, SCREEN_HEIGHT - CHARACTER_HEIGHT - 10)
player2 = Character(WHITE, SCREEN_WIDTH - 150, SCREEN_HEIGHT - CHARACTER_HEIGHT - 10)

# Sprite groups
characters = pygame.sprite.Group()
characters.add(player1)
characters.add(player2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player 1 controls
    if keys[pygame.K_a]:
        player1.move(-CHARACTER_SPEED)
    if keys[pygame.K_d]:
        player1.move(CHARACTER_SPEED)
    if keys[pygame.K_SPACE]:
        player1.attack()

    # Player 2 controls
    if keys[pygame.K_LEFT]:
        player2.move(-CHARACTER_SPEED)
    if keys[pygame.K_RIGHT]:
        player2.move(CHARACTER_SPEED)
    if keys[pygame.K_RETURN]:
        player2.attack()

    # Update characters
    characters.update()

    # Handle attack logic
    if player1.is_attacking and player1.rect.colliderect(player2.rect):
        player2.health -= 1

    if player2.is_attacking and player2.rect.colliderect(player1.rect):
        player1.health -= 1

    # Draw everything
    screen.fill(BLACK)
    characters.draw(screen)

    # Display health
    pygame.draw.rect(screen, WHITE, [50, 50, player1.health * 2, 20])
    pygame.draw.rect(screen, WHITE, [SCREEN_WIDTH - 150, 50, player2.health * 2, 20])

    pygame.display.flip()

    clock.tick(30)  # Cap the frame rate at 30 FPS

pygame.quit()

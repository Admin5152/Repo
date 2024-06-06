#Space

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SHIP_WIDTH = 50
SHIP_HEIGHT = 50
LASER_WIDTH = 5
LASER_HEIGHT = 20
ASTEROID_WIDTH = 50
ASTEROID_HEIGHT = 50
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Spaceship class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SHIP_WIDTH, SHIP_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5

    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def shoot(self):
        laser = Laser(self.rect.centerx, self.rect.top)
        lasers.add(laser)
        all_sprites.add(laser)

# Laser class
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((LASER_WIDTH, LASER_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Asteroid class
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ASTEROID_WIDTH, ASTEROID_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - ASTEROID_WIDTH)
        self.rect.y = random.randint(-200, -ASTEROID_HEIGHT)
        self.speed = random.randint(3, 7)

    def update():
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# Create sprite groups
all_sprites = pygame.sprite.Group()
lasers = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

# Create the spaceship
spaceship = Spaceship()
all_sprites.add(spaceship)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spaceship.shoot()

    # Control spaceship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship.move(-spaceship.speed)
    if keys[pygame.K_RIGHT]:
        spaceship.move(spaceship.speed)

    # Update all sprites
    all_sprites.update()

    # Create asteroids periodically
    if random.random() < 0.02:
        new_asteroid = Asteroid()
        asteroids.add(new_asteroid)
        all_sprites.add(new_asteroid)

    # Check for collisions
    collisions = pygame.sprite.groupcollide(lasers, asteroids, True, True)
    
    # Redraw the screen
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(60)  # Cap frame rate at 60 FPS

pygame.quit()


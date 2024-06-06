#Shooter




import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FOV = math.pi / 3  # Field of View (60 degrees)
HALF_FOV = FOV / 2
NUM_RAYS = 120
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 800  # Maximum depth for raycasting
WALL_HEIGHT = 120
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_SPEED = 5
ROTATION_SPEED = 0.03

# Create a Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("3D FPS")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player properties
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_angle = 0  # Initial player angle

# Simple map representation (1 = wall, 0 = empty space)
world_map = [
    "1111111111",
    "1000000011",
    "1011011011",
    "1000010011",
    "1001011011",
    "1010010011",
    "1111111111"
]

MAP_WIDTH = len(world_map[0])
MAP_HEIGHT = len(world_map)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_w]:
        player_x += math.cos(player_angle) * PLAYER_SPEED
        player_y += math.sin(player_angle) * PLAYER_SPEED
    if keys[pygame.K_s]:
        player_x -= math.cos(player_angle) * PLAYER_SPEED
        player_y -= math.sin(player_angle) * PLAYER_SPEED
    if keys[pygame.K_a]:
        player_angle -= ROTATION_SPEED
    if keys[pygame.K_d]:
        player_angle += ROTATION_SPEED

    # Keep player within bounds of the map
    player_x = max(0, min(player_x, SCREEN_WIDTH))
    player_y = max(0, min(player_y, SCREEN_HEIGHT))

    # Raycasting logic
    screen.fill(BLACK)  # Clear the screen
    for ray in range(NUM_RAYS):
        angle = player_angle - HALF_FOV + ray * DELTA_ANGLE
        x = player_x
        y = player_y

        # Cast a ray to determine where it hits a wall
        while True:
            x += math.cos(angle)
            y += math.sin(angle)

            # Check if ray hits a wall
            map_x = int(x // 100)
            map_y = int(y // 100)

            if map_x < 0 or map_x >= MAP_WIDTH or map_y < 0 or map_y >= MAP_HEIGHT:
                break

            if world_map[map_y][map_x] == "1":
                distance = math.hypot(x - player_x, y - player_y)
                height = int(WALL_HEIGHT / (distance * math.cos(player_angle - angle)))

                # Calculate shading based on distance
                shade = 255 / distance * 3
                color = (shade, shade, shade)

                pygame.draw.rect(
                    screen,
                    color,
                    (
                        ray * (SCREEN_WIDTH // NUM_RAYS),
                        (SCREEN_HEIGHT - height) // 2,
                        SCREEN_WIDTH // NUM_RAYS,
                        height,
                    ),
                )
                break

    # Update display and control frame rate
    pygame.display.flip()
    clock.tick(60)  # Control frame rate to 60 FPS

pygame.quit()

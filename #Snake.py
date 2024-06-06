#Snake

import pygame
import random


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

BLOCK_SIZE = 20
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, WHITE, [x[0], x[1], snake_block, snake_block])

def draw_score(score):
    score_text = font_style.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [0, 0])

def game_loop():
    game_over = False
    game_close = False

    x_snake = SCREEN_WIDTH / 2
    y_snake = SCREEN_HEIGHT / 2
    x_snake_change = 0
    y_snake_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            game_over_text = font_style.render("Game Over!", True, RED)
            screen.blit(game_over_text, [250, 250])
            draw_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_snake_change = -BLOCK_SIZE
                    y_snake_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_snake_change = BLOCK_SIZE
                    y_snake_change = 0
                elif event.key == pygame.K_UP:
                    x_snake_change = 0
                    y_snake_change = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    x_snake_change = 0
                    y_snake_change = BLOCK_SIZE

        if x_snake >= SCREEN_WIDTH or x_snake < 0 or y_snake >= SCREEN_HEIGHT or y_snake < 0:
            game_close = True

        x_snake += x_snake_change
        y_snake += y_snake_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = []
        snake_head.append(x_snake)
        snake_head.append(y_snake)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        draw_score(length_of_snake - 1)

        pygame.display.update()

        if x_snake == food_x and y_snake == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

game_loop()

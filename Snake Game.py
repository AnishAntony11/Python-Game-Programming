import pygame
import time
import random


pygame.init()

white = (255, 255, 255)
w, h = 500, 500


game_display = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake_game")


clock = pygame.time.Clock()
snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 50)
score_font = pygame.font.SysFont('ubuntu', 40)

## Displaying Score
def print_scr(score):
    text = score_font.render("Score: " + str(score), True, (0, 255, 0))
    game_display.blit(text, [195, 0])

## Snake Drawing --------------------------------
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])

def run():
    game_over = False
    game_close = False

    x = w/2
    y = h/2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    food_x = round(random.randrange(0, w-snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, h-snake_size) / 10.0) * 10.0


    while not game_over:
        while game_close:
            game_display.fill((0, 0, 0))
            game_over_message = message_font.render("Game Over!", True, (255, 0, 0))
            game_display.blit(game_over_message, [w / 3, h / 3])
            print_scr(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close  = False
                    if event.key == pygame.K_2:
                        run()

                    if event.key == pygame.quit:
                        game_over = True
                        game_close = False





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size


        if x >= w or x < 0 or y >= h or y < 0:
            game_close = True

        x += x_speed
        y += y_speed



        game_display.fill((0, 0, 0))
        pygame.draw.rect(game_display, (0, 255, 0), [food_x, food_y, snake_size, snake_size])


        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        print_scr(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, w - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, h - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)


    pygame.quit()
    quit()

run()
#Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# secret = (input("Enter Your Message:"))
# s = list(secret)
# print(s)
#
# print("Your Message Is Converted Into Secret Code")
#
# print("LOADING")
# if (len(secret)>=3):
#     secret.append(len(secret[0]))
#     secret.pop(0)
#     h= "hjv"
#     secret.append(h)
#     j = "woi"
#     secret.insert(j[0])
#     print(secret)
# else:
#     print(secret.reverse())
#
#
import pygame
import time

pygame.init()

# Window dimensions
width = 800
height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake dimensions
snake_size = 10
snake_speed = 15

# Create the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    window.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])


def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = width / 2
    y1 = height / 2

    # Change in position of the snake
    x1_change = 0
    y1_change = 0

    # Create the snake body
    snake_List = []
    Length_of_snake = 1

    # Generate random coordinates for the food
    foodx = round((round(time.time() * 1000) % width - snake_size) / 10.0) * 10.0
    foody = round((round(time.time() * 1000) % height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(white)
        pygame.draw.rect(window, red, [foodx, foody, snake_size, snake_size])
        snake_Head = []


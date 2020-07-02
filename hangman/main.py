import sys, pygame
from wordpull import pullword

## global definitions and alias
SCREEN_HEIGHT = 640
SCREEN_WIDTH = 480

NEW_GAME = 0
RUNNING_GAME = 1
PLAYER_WIN = 2
PLAYER_LOSS = 3
QUIT = 4

#difficuties (health,minimum word length, max word length)
EASY = (10,5,7)
MEDIUM = (8,8,10)
HARD = (6,10,15)
MEGA_HARD = (4,4,100)

GAME_STATE = NEW_GAME

pygame.display.init()

size = width, height = SCREEN_WIDTH , SCREEN_HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hangman Game")##sets the caption above the window

blue_background = pygame.image.load('images&sprites/blue.png')##testing image loading
icon = pygame.display.set_icon(blue_background)

running = True
while running:##main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =false
    screen.fill((140,0,65))##sets background, uses RGB
    pygame.display.update()

##Board = []
##Life = 1
##while(GAME_STATE != QUIT):
##    if checkwin():
##        GAME_STATE = PLAYER_WIN
##    if checklose():
##        GAME_STATE = PLAYER_LOSS


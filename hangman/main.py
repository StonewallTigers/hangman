import sys, pygame
from wordpull import pullword

## global definitions and alias
SCREEN_HIGHT = 320
SCREEN_WIDTH = 240

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

pygame.init()

size = width, hight = 320 , 240
pygame.display.set_mode(size)


Board = []
Life = 1
while(GAME_STATE != QUIT):
    if checkwin():
        GAME_STATE = PLAYER_WIN
    if checklose():
        GAME_STATE = PLAYER_LOSS


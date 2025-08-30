
import pygame
import time
import random

gamerunning = False



def create_grid(rows, cols):
    return [["#" for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for row in grid:
        for item in row:
            print(item, end=' ')
        print()



def activatesquare(y,x):
    grid[y][x] = "X"

def deactivatesquare(y,x):
    grid[y][x]= "#"

grid = create_grid(5, 5)

activex = 2
activey = 2


def gametick():
    global activey, activex
    grid[activey][activex] = "X"
    print_grid(grid)
    direction = input("Enter direction (w/a/s/d) or 'q' to quit: ")
    if direction == 'w' and activey > 0:
        deactivatesquare(activey, activex)
        activey -= 1
        activatesquare(activey, activex)
    elif direction == 's' and activey < 4:
        deactivatesquare(activey, activex)
        activey += 1
        activatesquare(activey, activex)
    elif direction == 'a' and activex > 0:
        deactivatesquare(activey, activex)
        activex -= 1
        activatesquare(activey, activex)
    elif direction == 'd' and activex < 4:
        deactivatesquare(activey, activex)
        activex += 1
        activatesquare(activey, activex)
    elif direction == 'q':
        print("Exiting game.")
        global gamerunning
        gamerunning = False
    else:
        print("Invalid move. Try again.")

gamerunning = True
while gamerunning == True:
    gametick()
    
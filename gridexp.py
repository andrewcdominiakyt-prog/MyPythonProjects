import time
import random

gamerunning = False
score = 0
appleonboard = False

def create_grid(rows, cols):
    return [["#" for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for row in grid:
        for item in row:
            print(item, end=' ')
        print()
    print()

def apple():
    global appleonboard, grid
    if appleonboard:
        return
    while True:
        y = random.randint(0, 4)
        x = random.randint(0, 4)
        if grid[y][x] == "#":
            grid[y][x] = "A"
            appleonboard = True
            break

def activatesquare(y, x):
    grid[y][x] = "X"

def deactivatesquare(y, x):
    grid[y][x] = "#"

grid = create_grid(5, 5)

activex = 2
activey = 2

def gametick():
    global activey, activex, gamerunning, score, appleonboard

    apple()

    print_grid(grid)
    direction = input("Enter direction (w/a/s/d) or 'q' to quit: ")

    ny, nx = activey, activex
    if direction == 'w' and activey > 0:
        ny -= 1
    elif direction == 's' and activey < 4:
        ny += 1
    elif direction == 'a' and activex > 0:
        nx -= 1
    elif direction == 'd' and activex < 4:
        nx += 1
    elif direction == 'q':
        print("Exiting game.")
        gamerunning = False
        return
    else:
        print("Invalid move. Try again.")
        return

    if (ny, nx) != (activey, activex):
        if grid[ny][nx] == "A":
            score += 1
            appleonboard = False  
            print("Score:", score)

        deactivatesquare(activey, activex)
        activey, activex = ny, nx
        activatesquare(activey, activex)

gamerunning = True
activatesquare(activey, activex)  
while gamerunning:
    gametick()

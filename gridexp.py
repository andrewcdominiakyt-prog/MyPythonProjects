import random

# Safe input: clamp to 1..5
try:
    minesnumber = int(input('Enter number of apples (1-5): '))
except ValueError:
    minesnumber = 1
minesnumber = max(1, min(5, minesnumber))

gamerunning = False
score = 0
appleonboard = 0

def create_grid(rows, cols):
    return [["#" for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for row in grid:
        for item in row:
            print(item, end=' ')
        print()
    print()

def apple():
    """Place ONE apple if we still need more."""
    global appleonboard, grid, minesnumber
    if appleonboard >= minesnumber:
        return

    # pick from empty cells; avoids infinite loops
    empties = [(y, x) for y in range(5) for x in range(5) if grid[y][x] == "#"]
    if not empties:
        return
    y, x = random.choice(empties)
    grid[y][x] = "A"
    appleonboard += 1

def activatesquare(y, x):
    grid[y][x] = "X"

def deactivatesquare(y, x):
    grid[y][x] = "#"

grid = create_grid(5, 5)

activex = 2
activey = 2

def gametick():
    global activey, activex, gamerunning, score, appleonboard

    # ensure apples present up to target each tick
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
            appleonboard -= 1
            print("Score:", score)

        deactivatesquare(activey, activex)
        activey, activex = ny, nx
        activatesquare(activey, activex)

# place player and spawn apples immediately so you see them
gamerunning = True
activatesquare(activey, activex)
for _ in range(minesnumber):
    apple()

while gamerunning:
    gametick()

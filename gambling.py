
import random

#make difficulty settings before gamestart
difficultynum = int(input("""Enter Difficulty
    Easy - Press 1
    Medium - Press 2
    Hard - Press 3
> """))
if difficultynum == 1:
    difficulty = 0.1
elif difficultynum == 2:
    difficulty = 0.3
elif difficultynum == 3:
    difficulty = 0.5

# Initialize the game
gridsize = (int(input("Enter Desired Grid Size:")))
grid = [['#' for _ in range(gridsize)] for _ in range(gridsize)]
def print_grid():
    global grid
    for row in grid:
        print (" ".join(row))

numbombs = int(round((gridsize * gridsize) * difficulty))
def place_bombs():
    global numbombs, gridsize, grid
    print (numbombs, "Bombs on Grid of", (gridsize * gridsize), "spaces")
    for _ in range(numbombs):
        while True:
            x = random.randint(0, gridsize - 1)
            y = random.randint(0, gridsize - 1)
            if grid[y][x] != 'B':
                grid[y][x] = 'B'
                break
place_bombs()
print_grid()
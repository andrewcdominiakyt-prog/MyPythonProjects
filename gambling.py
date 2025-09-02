
import random

#make difficulty settings before gamestart
difficulty = 0.5

# Initialize the grid
gridsize = (int(input("Enter Desired Grid Size:")))
grid = [['#' for _ in range(gridsize)] for _ in range(gridsize)]
def print_grid(grid):
    for row in grid:
        print (" ".join(row))

numbombs = round((gridsize * gridsize) * difficulty)

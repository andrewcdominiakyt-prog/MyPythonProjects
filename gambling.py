
import random

gamerunning = False

# Difficulty settings
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

# Initialize the showngrid & hiddengrid
gridsize = (int(input("Enter Desired Grid Size:")))
grid = [['#' for _ in range(gridsize)] for _ in range(gridsize)]
showngrid = [['#' for _ in range(gridsize)] for _ in range(gridsize)]

def printshowngrid():
    global showngrid
    for row in showngrid:
        print (" ".join(row))


#mainly for debugging
def printrealgrid():
    global grid
    for row in grid:
        print (" ".join(row))

#initialize bombs
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




def playerturn():
    global grid, showngrid, gridsize, gamerunning
    while True:
        y = int(input("Enter X Selection:"))
        x = int(input("Enter Y Selection:"))
        if x > (gridsize):
            print ("Invalid Move, Try again")
        elif x > (gridsize):
            print ("Invalid Move, Try again")
        elif grid[x][y] == "@":
            print ("Square Taken, Try again")
        elif grid[x][y] == "B":
            print ("Square had a bomb. YOU LOSE")
        
            


#start game            
gamerunning = True
printrealgrid()
printshowngrid()           

playerturn()
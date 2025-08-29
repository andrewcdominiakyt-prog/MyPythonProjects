def create_grid(rows, cols):
    return [["#" for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for row in grid:
        for item in row:
            print(item, end=' ')
        print()

def modify_grid(grid, r, c):
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        grid[r][c] = "x"
    else:
        print(f"Skipping invalid cell ({r}, {c})")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
grid = create_grid(rows, cols)

r = 0
c = 0

for i in range(rows * cols):
    modify_grid(grid, r, c)
    print_grid(grid)
    print()

    c += 1
    if c >= cols:  
        c = 0
        r += 1

    if r >= rows: 
        print("Reached end of grid.")
        break


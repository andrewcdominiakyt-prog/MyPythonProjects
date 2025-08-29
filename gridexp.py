def create_grid(rows, cols):
    return [[9 for _ in range(cols)] for _ in range(rows)]

grid = create_grid(int(input("Enter number of rows:")), int(input("Enter number of columns:")))

for row in grid:
    for item in row:
        print(item, end=' ')
    print()

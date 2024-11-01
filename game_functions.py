import random

# Initialize 4x4 grid
def initialize_grid():
    grid = [[0] * 4 for _ in range(4)]
    add_new_number(grid)
    add_new_number(grid)
    return grid

# Add a new number to the grid (only adds a '2' in an empty cell)
def add_new_number(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2

# Check if there are no moves left (game over)
def check_game_over(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
    return True

# Check if the player has reached 2048
def check_win(grid):
    return any(2048 in row for row in grid)

# Implement move functions (move_left, move_right, move_up, move_down)
def move_left(grid):
    for i in range(4):
        slide_and_merge_row(grid[i])

def move_right(grid):
    for i in range(4):
        grid[i] = grid[i][::-1]
        slide_and_merge_row(grid[i])
        grid[i] = grid[i][::-1]

def move_up(grid):
    for j in range(4):
        column = [grid[i][j] for i in range(4)]
        slide_and_merge_row(column)
        for i in range(4):
            grid[i][j] = column[i]

def move_down(grid):
    for j in range(4):
        column = [grid[i][j] for i in range(4)][::-1]
        slide_and_merge_row(column)
        column.reverse()
        for i in range(4):
            grid[i][j] = column[i]

# Slide and merge a single row or column
def slide_and_merge_row(row):
    new_row = [num for num in row if num != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [num for num in new_row if num != 0]
    row[:] = new_row + [0] * (4 - len(new_row))

# Display the grid
def display_grid(grid):
    for row in grid:
        print(" ".join(str(num).center(4) if num != 0 else "." for num in row))
    print()

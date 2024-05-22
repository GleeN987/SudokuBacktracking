def find_empty_box(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None


def valid_puzzle(grid, row, col, guess):
    row_vals = grid[row]
    if guess in row_vals:
        return False
    
    col_vals = []
    for i in range(9):
        col_vals.append(grid[i][col])
    if guess in col_vals:
        return False
    
    subgrid_x = (row // 3) * 3
    subgrid_y = (col // 3) * 3
    for r in range(subgrid_x, subgrid_x+3):
        for c in range(subgrid_y, subgrid_y+3):
            if grid[r][c] == guess:
                return False
    
    return True

    

def solve_sudoku(grid):
    row, col = find_empty_box(grid)

    if row is None:
        return True
    
    for guess in range(1, 10):
        if valid_puzzle(grid, row, col, guess):
            grid[row][col] = guess
            if solve_sudoku(grid):
                return True

        grid[row][col] = 0

    return False


if __name__ == "__main__":
    grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]   
    print(solve_sudoku(grid))
    print(grid)
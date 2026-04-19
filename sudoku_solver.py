# ---------------------------------------------------------
# Program: Automatic Sudoku Solver
# Task: 03 - SkillCraft Technology
# Author: Chethan S.
# Description: Uses a backtracking algorithm to solve 9x9 Sudoku.
# ---------------------------------------------------------

def is_valid(board, row, col, num):
    # Check Row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check Column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check 3x3 Box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        if solve_sudoku(board):
                            return True
                        
                        # Backtrack if no solution found
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(board[i][j], end=" ")
        print()

# Sample Unsolved Grid (0 represents empty cells)
unsolved_grid = [
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

print("--- Original Unsolved Puzzle ---")
print_board(unsolved_grid)

if solve_sudoku(unsolved_grid):
    print("\n--- Solved Puzzle ---")
    print_board(unsolved_grid)
else:
    print("\nNo solution exists.")
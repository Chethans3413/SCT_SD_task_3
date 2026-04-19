# Sudoku Solver

An automatic Sudoku puzzle solver using backtracking algorithm written in Python.

## Overview

This program solves Sudoku puzzles automatically by employing a **backtracking algorithm**. It efficiently finds valid solutions by:
1. Finding empty cells in the grid
2. Trying numbers 1-9 in each empty cell
3. Validating placements against Sudoku rules
4. Recursively solving the rest of the puzzle
5. Backtracking when no valid number can be placed

## Features

- **Backtracking Algorithm**: Efficient constraint-based search
- **Input Validation**: Checks for invalid puzzles
- **Multiple Input Methods**: 
  - Built-in example puzzles (Easy, Medium, Hard)
  - Load from text files
  - Manual entry
- **File I/O**: Save solved puzzles to files
- **Clear Display**: Formatted grid output with 3x3 subgrid markers

## Installation

No external dependencies required! Works with Python 3.6+

```bash
python sudoku_solver.py
```

## Usage

### Running the Program

```bash
python sudoku_solver.py
```

An interactive menu will appear with these options:

**Option 1: Solve Example Puzzle**
- Choose from Easy, Medium, or Hard pre-loaded puzzles
- Program displays and solves automatically

**Option 2: Load from File**
- Provide path to a puzzle file (see File Format below)
- Program solves and optionally saves the solution

**Option 3: Manual Entry**
- Enter 9 rows of 9 numbers each
- Use 0 for empty cells
- Program validates and solves

**Option 4: Exit**

### File Format

Puzzle files should contain 9 lines, each with 9 space-separated numbers:
- Numbers 1-9 represent filled cells
- 0 represents empty cells

**Example (sample_puzzle.txt):**
```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

## Algorithm Explanation

### Backtracking Algorithm

The solver uses **depth-first search with backtracking**:

```
1. Find first empty cell (value = 0)
2. If no empty cell found:
   - Puzzle is solved, return True
3. For each number 1-9:
   a. Check if number is valid at this position (no conflicts)
   b. If valid:
      - Place the number
      - Recursively solve the rest
      - If successful, return True
      - Otherwise, remove number (backtrack)
4. If no number works, return False
```

### Validation Rules

A placement is valid if it doesn't violate Sudoku rules:
- **Row Rule**: Number doesn't appear elsewhere in the same row
- **Column Rule**: Number doesn't appear elsewhere in the same column
- **3x3 Subgrid Rule**: Number doesn't appear elsewhere in the same 3x3 box

## Time Complexity

- **Best Case**: O(1) - Already solved
- **Average Case**: O(9^(n)) where n = number of empty cells
- **Worst Case**: O(9^81) - But with constraint checking, typically much faster

Practical performance: Most puzzles solve in milliseconds to seconds

## Class Reference

### `SudokuSolver`

Main solver class.

#### Methods:

- **`__init__(grid)`**: Initialize with 9x9 puzzle grid
- **`solve()`**: Solve the puzzle, returns True if solvable
- **`is_valid(row, col, num)`**: Check if placing num is valid
- **`find_empty()`**: Find next empty cell
- **`is_valid_puzzle()`**: Validate initial puzzle state
- **`display(grid=None)`**: Print formatted grid
- **`get_solution()`**: Return solved grid
- **`reset()`**: Restore to original puzzle

### Helper Functions:

- **`load_puzzle_from_file(filename)`**: Load puzzle from text file
- **`save_solution_to_file(grid, filename)`**: Save solution to file

## Example Output

```
Original EASY Puzzle:
+---------+---------+---------+
| 5 3 . | . 7 . | . . . |
| 6 . . | 1 9 5 | . . . |
| . 9 8 | . . . | . 6 . |
+---------+---------+---------+
| 8 . . | . 6 . | . . 3 |
| 4 . . | 8 . 3 | . . 1 |
| 7 . . | . 2 . | . . 6 |
+---------+---------+---------+
| . 6 . | . . . | 2 8 . |
| . . . | 4 1 9 | . . 5 |
| . . . | . 8 . | . 7 9 |
+---------+---------+---------+

Solving...
Solved!

+---------+---------+---------+
| 5 3 4 | 6 7 8 | 9 1 2 |
| 6 7 2 | 1 9 5 | 3 4 8 |
| 1 9 8 | 3 4 2 | 5 6 7 |
+---------+---------+---------+
| 8 5 9 | 7 6 1 | 4 2 3 |
| 4 2 6 | 8 5 3 | 7 9 1 |
| 7 1 3 | 9 2 4 | 8 5 6 |
+---------+---------+---------+
| 9 6 1 | 5 3 7 | 2 8 4 |
| 2 8 7 | 4 1 9 | 6 3 5 |
| 3 4 5 | 2 8 6 | 1 7 9 |
+---------+---------+---------+
```

## Tips for Performance

1. **Constraint Propagation**: The algorithm checks validity before placement, reducing search space
2. **Order Matters**: Cells checked left-to-right, top-to-bottom (can optimize by checking most constrained first)
3. **Valid Puzzles**: Ensure input puzzles have exactly one solution

## Testing

The program includes three example puzzles of varying difficulty:
- **Easy**: ~40 empty cells
- **Medium**: ~55 empty cells  
- **Hard**: ~80 empty cells

Run the program and select option 1 to test these examples.

## Limitations

- Works only for standard 9x9 Sudoku
- Expects valid input (no error checking for malformed puzzles)
- No optimization for extremely hard puzzles with minimal clues
- Single-threaded

## Future Enhancements

- Support for other Sudoku variants (4x4, 16x16)
- Constraint propagation optimization
- Graphical user interface (GUI)
- Parallel solving for multiple puzzles
- Sudoku puzzle generator

## License

Free to use and modify.

import random

def find_next_empty(puzzle):
    # Finds the next row, column that is not filled yet
    # We are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None  # If no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    # Figures out if the guess is valid in the row, column, and 3x3 square

    # Check the row
    if guess in puzzle[row]:
        return False

    # Check the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Check the 3x3 square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # If we reach this point, the guess is valid
    return True

def solve_sudoku(puzzle):
    # Solve Sudoku using backtracking
    # Step 1: Choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # Step 1.1: If there's nowhere left, then we're done
    if row is None:
        return True

    # Step 2: If there is a place to put a number, then make a guess
    for guess in range(1, 10):  # digits 1-9
        # Step 3: Check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # Step 3.1: Place that guess on the puzzle
            puzzle[row][col] = guess
            # Step 4: Recursively attempt to solve the puzzle
            if solve_sudoku(puzzle):
                return True

        # Step 5: If not valid or if the guess doesn't solve the puzzle, backtrack
        puzzle[row][col] = -1  # Reset the guess

    # If no number 1-9 works, return False
    return False

def generate_complete_sudoku():
    # Pre-defined valid Sudoku board
    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    # Shuffle the rows within each section
    for i in range(0, 9, 3):
        random.shuffle(board[i:i+3])

    # Transpose to shuffle columns similarly
    board = [list(x) for x in zip(*board)]
    for i in range(0, 9, 3):
        random.shuffle(board[i:i+3])
    board = [list(x) for x in zip(*board)]

    return board

def remove_numbers_from_board(board, num_to_remove=40):
    # Remove 'num_to_remove' elements from the board
    for _ in range(num_to_remove):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == -1:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = -1
    return board

if __name__ == "__main__":
    complete_board = generate_complete_sudoku()
    example_board = remove_numbers_from_board(complete_board, num_to_remove=40)

    print("Sudoku Puzzle:")
    for row in example_board:
        print(row)
    
    print("\nSudoku solved successfully:")
    if solve_sudoku(example_board):
        for row in example_board:
            print(row)
    else:
        print("This Sudoku puzzle is unsolvable.")

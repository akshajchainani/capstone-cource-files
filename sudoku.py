def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def is_valid(board, row, col, num):
    # Check if the number is not in the current row
    if num in board[row]:
        return False

    # Check if the number is not in the current column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):  # Recursively solve the rest
                            return True
                        board[row][col] = 0  # Backtrack if the solution doesn't work

                return False  # If no valid number found, return False
    return True  # Puzzle solved

# Example usage
if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("Original Sudoku Puzzle:")
    print_board(puzzle)

    if solve_sudoku(puzzle):
        print("\nSolved Sudoku Puzzle:")
        print_board(puzzle)
    else:
        print("\nNo solution exists!")

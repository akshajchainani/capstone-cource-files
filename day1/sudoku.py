def print_board(board):
    """Print the Sudoku board in a readable format."""
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def get_candidates(board, row, col):
    """Get a list of valid candidates for a given cell (row, col)."""
    if board[row][col] != 0:
        return []  
    
    used = set(board[row]) | {board[i][col] for i in range(9)}
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            used.add(board[i][j])
    
    return [num for num in range(1, 10) if num not in used]

def solve_sudoku_simple_logic(board):
    """Solve the Sudoku puzzle using basic logical rules."""
    while True:
        progress = False
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    candidates = get_candidates(board, row, col)
                    if len(candidates) == 1:
                        board[row][col] = candidates[0]
                        progress = True
        
        for num in range(1, 10):
            for row in range(9):
                positions = [
                    col for col in range(9)
                    if board[row][col] == 0 and num in get_candidates(board, row, col)
                ]
                if len(positions) == 1:
                    board[row][positions[0]] = num
                    progress = True
            
            for col in range(9):
                positions = [
                    row for row in range(9)
                    if board[row][col] == 0 and num in get_candidates(board, row, col)
                ]
                if len(positions) == 1:
                    board[positions[0]][col] = num
                    progress = True
            
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    positions = []
                    for i in range(3):
                        for j in range(3):
                            row, col = box_row + i, box_col + j
                            if board[row][col] == 0 and num in get_candidates(board, row, col):
                                positions.append((row, col))
                    if len(positions) == 1:
                        r, c = positions[0]
                        board[r][c] = num
                        progress = True
        
        if not progress:
            break
    
    return all(all(cell != 0 for cell in row) for row in board)

if __name__ == "__main__":
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

    print("original Sudoku Puzzle:")
    print_board(puzzle)

    if solve_sudoku_simple_logic(puzzle):
        print("\nsolved Sudoku Puzzle:")
        print_board(puzzle)
    else:
        print("\ncould not solve the puzzle using simple logic!")

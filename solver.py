def print_board(board):
    """
    Prints the Sudoku board in a readable format
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    """
    Finds an empty cell in the board
    Returns (row, col) or None if no empty cell exists
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    
    return None

def is_valid(board, num, pos):
    """
    Checks if placing 'num' at position 'pos' is valid
    Returns True if valid, False otherwise
    """
    # Check row
    for j in range(len(board[0])):
        if board[pos[0]][j] == num and pos[1] != j:
            return False
    
    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

def solve(board):
    """
    Solves the Sudoku board using backtracking
    Returns True if solved, False if no solution exists
    """
    empty = find_empty(board)
    if not empty:
        return True  # Board is complete
    
    row, col = empty
    
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            
            if solve(board):
                return True
            
            # If placing num doesn't lead to a solution, backtrack
            board[row][col] = 0
    
    return False

# Example usage
if __name__ == "__main__":
    # 0 represents empty cells    
    example_board = [[0, 4, 7, 6, 0, 5, 0, 0, 0],
[0, 0, 0, 0, 7, 4, 1, 5, 0],
[5, 0, 2, 0, 0, 0, 0, 7, 0],
[4, 7, 1, 9, 2, 8, 0, 0, 0],
[0, 8, 0, 0, 0, 0, 0, 0, 0],
[0, 2, 0, 0, 0, 0, 8, 0, 9],
[0, 0, 0, 0, 0, 6, 0, 8, 0],
[7, 5, 0, 8, 3, 0, 0, 0, 0],
[0, 0, 8, 1, 0, 7, 2, 0, 0]
]
    
    print("Sudoku Puzzle:")
    print_board(example_board)
    print("\nSolving...\n")
    
    if solve(example_board):
        print("Sudoku Solution:")
        print_board(example_board)
        for i in range(9):
            print(example_board[i],end=',\n')
    else:
        print("No solution exists for this puzzle.")

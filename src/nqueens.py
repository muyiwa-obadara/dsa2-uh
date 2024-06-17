import numpy as np

# Initialize the board size
size: int = int(input("Enter the size of the board: "))
mode: str = input("Enter the mode (1 for Backtracking, 2 Las-Vegas): ")

while mode not in ['1', '2']:
    print("Invalid mode. Please enter a valid mode.")
    mode: str = input("Enter the mode (1 for Backtracking, 2 Las-Vegas): ")

# Construct an empty board object
board = np.array([[0]*size]*size)
boards_index: list = []
boards: list = []

# Define a function to check if the cell
# is available at the given row and column
def is_available(board: list, row: int, col: int) -> list:
    """Returns True if the board is available at the given row and column.
    
    Args:
        board (list): The board
        row (int): The row
        col (int): The column
        
    Returns:    
        bool: True if the board is available at the given row and column.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    for i, j in zip(range(row, size, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board: list, col: int) -> list:
    """Solves the N-Queens problem.
    
    Args:
        board (list): The board
        col (int): The column
        
    Returns:
        result (bool): True if the board is available at the given row and column.
    """
    if (col == size):
        board_instance_positions = []
        for row in board:
            for col in range(len(row)):
                if row[col] == 1:
                    board_instance_positions.append(col+1)
        boards_index.append(np.array(board_instance_positions))
        boards.append(np.array(board))
        return True
    result = False
    for i in range(size):
        if (is_available(board, i, col)):
            board[i][col] = 1
            if mode == "1":
                result = solve_nqueens(board, col + 1) or result
                board[i][col] = 0
            else:
                result = solve_nqueens(board, col + np.random.randint(size - 1 - col)) or result
    return result

solve_nqueens(board, 0)
print(boards_index)

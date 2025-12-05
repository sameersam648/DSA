def print_board(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()

def is_safe(board, row, col):
    N = len(board)

    for i in range(row):
        if board[i][col] == 1:
            return False

    # upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens_util(board, row):
    N = len(board)
    if row == N:
        print("One Solution:")
        print_board(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_nqueens_util(board, row + 1):   
                return True
            board[row][col] = 0                      
    return False

def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]
    if not solve_nqueens_util(board, 0):
        print("No solution exists for N =", N)

# run
solve_nqueens(8)

def print_board(board):
    """ Prints the Tic-Tac-Toe Board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """ Checks if the current player has won """
    for row in board:
        if all(s == player for s in row):
            return True
        
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-1] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    """Check if the game is a draw"""
    for row in board:
        if " " in row:
            return False
    return True

def ttt():
    """Main function to play Tic-Tac-Toe"""
    board = [[ " " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"\nPlayer {current_player}'s turn")

        try:
            row = int(input("Enter row(0-2): "))
            col = int(input("Enter colum (0-2): "))
        except ValueError:
            print("Invalid input! Enter numbers 0,1 or 2.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position! Choose row and coulmn from 0 to 2.")
            continue

        if board[row][col] != " ":
            print("Position already taken! Choose another.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"\nPlayer {current_player} wins!")
            break
        
        if is_draw(board):
            print("\nThe game is a draw!")
            break

        current_player = "0" if current_player == "X" else "X"

ttt()
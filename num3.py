import math

# Initialize the Tic-Tac-Toe board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Define constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("  1   2   3")
    for i, row in enumerate(board):
        print(f"{chr(65 + i)} {' | '.join(row)}")
        if i < 2:
            print(" ---|---|---")

# Function to check if a move is valid
def is_valid_move(board, move):
    row, col = move
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

# Function to check if the game is over and return the result
def is_game_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    if all(cell != ' ' for row in board for cell in row):
        return 'DRAW'
    return None

# Function to evaluate the board for the minimax algorithm
def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == PLAYER_X:
            return 1
        if board[0][i] == board[1][i] == board[2][i] == PLAYER_X:
            return 1
        if board[i][0] == board[i][1] == board[i][2] == PLAYER_O:
            return -1
        if board[0][i] == board[1][i] == board[2][i] == PLAYER_O:
            return -1
    if board[0][0] == board[1][1] == board[2][2] == PLAYER_X:
        return 1
    if board[0][2] == board[1][1] == board[2][0] == PLAYER_X:
        return 1
    if board[0][0] == board[1][1] == board[2][2] == PLAYER_O:
        return -1
    if board[0][2] == board[1][1] == board[2][0] == PLAYER_O:
        return -1
    return 0

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if depth == 0 or is_game_over(board):
        return evaluate(board)
    
    if is_maximizing:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = PLAYER_X
                    eval = minimax(board, depth - 1, alpha, beta, False)
                    board[row][col] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = PLAYER_O
                    eval = minimax(board, depth - 1, alpha, beta, True)
                    board[row][col] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to make a move for the computer player (using minimax)
def computer_move(board):
    best_eval = -math.inf
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = PLAYER_X
                eval = minimax(board, 8, -math.inf, math.inf, False)
                board[row][col] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

# Main game loop
while True:
    print_board(board)

    # Player's move
    while True:
        player_input = input("Enter your move (e.g., A1 or B2): ").strip().upper()
        if len(player_input) == 2 and player_input[0] in 'ABC' and player_input[1] in '123':
            row = ord(player_input[0]) - ord('A')
            col = int(player_input[1]) - 1
            if is_valid_move(board, (row, col)):
                board[row][col] = PLAYER_O
                break
        print("Invalid move. Try again.")

    result = is_game_over(board)
    if result == 'DRAW':
        print_board(board)
        print("It's a tie!")
        break
    elif result:
        print_board(board)
        print("Player O wins!")
        break

    # Computer's move
    computer_row, computer_col = computer_move(board)
    board[computer_row][computer_col] = PLAYER_X

    result = is_game_over(board)
    if result == 'DRAW':
        print_board(board)
        print("It's a tie!")
        break
    elif result:
        print_board(board)
        print("Computer X wins!")
        break


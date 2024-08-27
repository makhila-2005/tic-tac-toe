def print_board(board):
    # Print each row of the board
    for row in board:
        # Join the row elements with " | " and print the row
        print(" | ".join(row))
        # Print a separator line after each row
        print("-" * 10)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a winning condition
    for i in range(3):
        # Check if any row or column is completely filled by the player
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    # Check the two diagonals for a winning condition
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    # Initialize an empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    # Define the players
    players = ["X", "O"]
    # Start with player X
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")

    # Loop for a maximum of 9 turns (the number of cells on the board)
    for turn in range(9):
        # Print the current state of the board
        print_board(board)
        # Ask the current player for their move
        row, col = map(int, input(f"Player {players[current_player]}, enter your move (row and column): ").split())

        # Check if the selected cell is empty
        if board[row][col] == " ":
            # Place the player's mark on the board
            board[row][col] = players[current_player]
            # Check if the current player has won
            if check_winner(board, players[current_player]):
                # Print the final state of the board and declare the winner
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                return
            # Switch to the other player
            current_player = 1 - current_player
        else:
            # If the move is invalid (cell is not empty), ask the player to try again
            print("Invalid move. Try again.")

    # If all cells are filled and no player has won, declare a tie
    print_board(board)
    print("It's a tie!")

# Start the game
tic_tac_toe()
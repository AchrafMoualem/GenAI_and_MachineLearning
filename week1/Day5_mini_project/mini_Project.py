# Step 1: Representing the Game Board
def create_board():
    return [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

# Step 2: Displaying the Game Board
def display_board(board):
    print("\n  1   2   3")
    for i, row in enumerate(board):
        print(f"{i+1} " + " | ".join(row))
        if i < 2:
            print("  " + "-" * 9)
    print()

# Step 3: Getting Player Input
def player_input(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter column (1-3): ")) - 1

            if row not in range(3) or col not in range(3):
                print("Invalid position! Please enter numbers between 1 and 3.")
            elif board[row][col] != ' ':
                print("That cell is already taken! Choose another.")
            else:
                return row, col
        except ValueError:
            print("Invalid input! Please enter numbers only.")

# Step 4: Checking for a Winner
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Step 5: Checking for a Tie
def check_tie(board):
    return all(board[row][col] != ' ' for row in range(3) for col in range(3))

# Step 6: The Main Game Loop
def play():
    board = create_board()
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print("Rows and columns are numbered 1-3 from top-left.")

    while True:
        display_board(board)

        # Get player move and update board
        row, col = player_input(board, current_player)
        board[row][col] = current_player

        # Check for winner
        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        # Check for tie
        if check_tie(board):
            display_board(board)
            print("It's a tie! Well played both!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

play()
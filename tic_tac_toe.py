import math

# Create an empty board
board = [" " for _ in range(9)]

HUMAN = "X"
AI = "O"


# Display board
def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


# Show board positions
def print_positions():
    print("Board Positions")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")
    print()


# Check winner
def check_winner(player):
    winning_combinations = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True

    return False


# Check draw
def is_draw():
    return " " not in board


# Minimax Algorithm
def minimax(is_maximizing):

    if check_winner(AI):
        return 1

    if check_winner(HUMAN):
        return -1

    if is_draw():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = AI

                score = minimax(False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = HUMAN

                score = minimax(True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score


# AI Move
def ai_move():

    best_score = -math.inf
    best_move = 0

    for i in range(9):

        if board[i] == " ":

            board[i] = AI

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = AI


# Human Move
def human_move():

    while True:

        try:

            move = int(input("Enter your move (1-9): "))

            if move < 1 or move > 9:
                print("Enter a number between 1 and 9.")
                continue

            if board[move - 1] != " ":
                print("Cell already occupied.")
                continue

            board[move - 1] = HUMAN
            break

        except ValueError:
            print("Please enter a valid number.")


# Main Game
def game():

    print("=" * 35)
    print("      TIC TAC TOE AI")
    print("=" * 35)

    print_positions()

    while True:

        print_board()

        human_move()

        if check_winner(HUMAN):
            print_board()
            print("🎉 Congratulations! You Win!")
            break

        if is_draw():
            print_board()
            print("🤝 Match Draw!")
            break

        print("AI is thinking...")

        ai_move()

        if check_winner(AI):
            print_board()
            print("🤖 AI Wins!")
            break

        if is_draw():
            print_board()
            print("🤝 Match Draw!")
            break


# Start Game
game()
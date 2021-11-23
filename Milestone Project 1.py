# Intro
print("Use the computer's keypad to play!")
print("The number you press is where your X or O will be placed!")

# Mapping keys to board
board_map = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
# Possible spaces
possible_spaces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# List of spaces used
board_full = []


# Print the board
def print_board(board):

    line1 = [" ", board[1], " | ", board[2], " | ", board[3], " "]
    line2 = [" ", board[4], " | ", board[5], " | ", board[6], " "]
    line3 = [" ", board[7], " | ", board[8], " | ", board[9], " "]
    midline = "-----------"

    print("".join(line3))
    print(midline)
    print("".join(line2))
    print(midline)
    print("".join(line1))


# Choices
def pos_choice():
    global position
    while position not in possible_spaces:
        print("Please input a number from 1-9")
        position = input("Choose a position: ")


def xo_choice():
    global x_or_o
    while x_or_o not in ["X", "O"]:
        print("Please input X or O")
        x_or_o = input("X or O: ")


def winning():
    global win
    # Winning X
    if board_map[1] == board_map[2] == board_map[3] == "X":
        print("X wins!")
        win = True
    elif board_map[4] == board_map[5] == board_map[6] == "X":
        print("X wins!")
        win = True
    elif board_map[7] == board_map[8] == board_map[9] == "X":
        print("X wins!")
        win = True
    elif board_map[7] == board_map[4] == board_map[1] == "X":
        print("X wins!")
        win = True
    elif board_map[8] == board_map[5] == board_map[2] == "X":
        print("X wins!")
        win = True
    elif board_map[9] == board_map[6] == board_map[3] == "X":
        print("X wins!")
        win = True
    elif board_map[7] == board_map[5] == board_map[3] == "X":
        print("X wins!")
        win = True
    elif board_map[9] == board_map[5] == board_map[1] == "X":
        print("X wins!")
        win = True

    # Winning O
    if board_map[1] == board_map[2] == board_map[3] == "O":
        print("O wins!")
        win = True
    elif board_map[4] == board_map[5] == board_map[6] == "O":
        print("O wins!")
        win = True
    elif board_map[7] == board_map[8] == board_map[9] == "O":
        print("O wins!")
        win = True
    elif board_map[7] == board_map[4] == board_map[1] == "O":
        print("O wins!")
        win = True
    elif board_map[8] == board_map[5] == board_map[2] == "O":
        print("O wins!")
        win = True
    elif board_map[9] == board_map[6] == board_map[3] == "O":
        print("O wins!")
        win = True
    elif board_map[7] == board_map[5] == board_map[3] == "O":
        print("O wins!")
        win = True
    elif board_map[9] == board_map[5] == board_map[1] == "O":
        print("O wins!")
        win = True


# Loop through the game
print_board(board_map)
play = "Y"
win = False
while play == "Y":
    position = 0
    x_or_o = 0
    pos_choice()
    xo_choice()
    board_map[int(position)] = x_or_o

    print_board(board_map)
    board_full.append(x_or_o)
    winning()

    # Play again after win
    if win:
        play = input("Would you like to play again? ")
        # Resetting board
        if play == "Y":
            board_map = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
            print_board(board_map)
            win = False
        # Must be Y or N
        while play not in ["Y", "N"]:
            print("Please input Y or N")
            play = input("Would you like to continue?")

    # Play again after tie
    if not win and len(board_full) == 9:
        print("It's a tie!")
        play = input("Would you like to play again? ")
        # Resetting board
        if play == "Y":
            board_map = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
            print_board(board_map)
            win = False
        # Must be Y or N
        while play not in ["Y", "N"]:
            print("Please input Y or N")
            play = input("Would you like to continue?")

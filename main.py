print("""
# @Author 来ビス―クラム　(raibisu.kuramu@gamil.com)
# @github https://github.com/yuukuramu
# @instagram https://www.instagram.com/raibisu.kuramu
# @site https://yuukuramu.xyz
""")

# CONST
BOARD_ROWS = 3
BOARD_COLS = 3

EMPTY_SQUARE_SYMBOL = "-"

# FUNCTIONS
def clear_terminal():
    """Check OS.system and clear terminal"""

    if os.name == "nt":  # posx, java, nt
        os.system("cls")
    else:
        os.system("clear")


def print_board(board):
    """
    Print board
    """
    for row in board:
        for col in row:
            print(f"{col} ", end="")
        print()


def mark_square(row, col, player):
    """
    Mark square in board
    row, col: 0 - 2
    player: "0", "X"
    """
    board[row][col] = player


def available_square(row, col):
    """Check if square is empty"""
    return board[row][col] == EMPTY_SQUARE_SYMBOL

def is_board_full():
    """Check is board full"""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == EMPTY_SQUARE_SYMBOL:
                return False
    return True

def check_win(player):
    "Check is somebody win."
    # vertical WIN
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Horizontal WIN
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    # asc diognal WIN
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    # desc diognal WIN
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

# modules
import os
import time

import pyfiglet

# time.sleep(1.5)
clear_terminal()

# banner
print(pyfiglet.figlet_format("TIC TAC TOE" ))

# application

# Create board: EMPTY_SQUARE_SYMBOL * BOARD_ROWS
board = [[EMPTY_SQUARE_SYMBOL] * BOARD_ROWS for i in range(BOARD_COLS)]

# player figure whoes allowed to select
allowed_players = ["0", "X"]
try:
    while True:
            # Split to 2 loops cuz we econom memory! Now we select first player figure and forget that to all time.
            # if these 2 loops combining in one loop then we need create a check, if user have an figure. 1 loop 1 unnecessary choice
            player = input("Select player one figure: 0 or X: ").upper()
            # check if figure is in allwed figure list
            if player not in allowed_players:
                print("You can use only [0 or X]")
                continue
            break

    while True:
        clear_terminal()
        
        print()
        print_board(board)
        print()

        try:
            row, col = input("Select square position. example - 0 0: ").split()
        except ValueError:
            print(f"\nLetters not availabled\nTry again!")
            time.sleep(1)
            continue
        
        # input() returns string 
        # Convert data to int, cuz we can't at this situation do it like | int(input("..."))
        row = int(row)
        col = int(col)
        
        try:
            # check if square is free
            if available_square(row, col):
                if player == "0":
                    # if player = 0 mark square and switch players
                    mark_square(row, col, player)
                    player = "X"
                elif player == "X":
                    # if player = X mark square and switch players
                    mark_square(row, col, player)
                    player = "0"
            else:
                print("This square already taken.")
                time.sleep(1)
                continue
        except IndexError:
            # If player selected position who not exist.
            print(f"\nPosition {row, col} not exist\nTry again!")
            time.sleep(1)
            continue
except KeyboardInterrupt:
    print("\nGame has been closed.")
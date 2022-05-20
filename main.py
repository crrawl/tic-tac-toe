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
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == EMPTY_SQUARE_SYMBOL:
                return False
    return True

# libraries
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

print_board(board)

# author: Daniel Villano-Herrera
# date: 8/3/2021

import random
import tkinter
from functools import partial
from tkinter import *
from tkinter import messagebox

# This file will serve as the logistics and the gui of the tic tac toe game.
# I will now use the tic tac toe via lists instead of dictionaries
game_board = [[' ' for rows in range(3)] for columns in range(3)]

# I will now use the sign with numbers to track the players turn.
sign = 0


# Determining how the game is over via winning
def game_Winner(board, player):
            # Win via row 1
    return ((board[0][0] == player and board[0][1] and player and board[0][2] == player) or
            # Win via row 2
            (board[1][0] == player and board[1][1] == player and board[1][2] == player) or
            # Win via row 3
            (board[2][0] == player and board[2][1] == player and board[2][2] == player) or
            # Win via column 1
            (board[0][0] == player and board[1][0] == player and board[2][0] == player) or
            # Win via column 2
            (board[0][1] == player and board[1][1] == player and board[2][1] == player) or
            # Win via column 3
            (board[0][2] == player and board[1][2] == player and board[2][2] == player) or
            # Win via diagonal
            (board[1][0] == player and board[1][1] == player and board[1][2] == player) or
            # Win via diagonal
            (board[2][0] == player and board[1][1] == player and board[0][2] == player))


# Determines whether the game is full by counting the spaces. If the count of spaces is less than 0, the game is full.
def isGameFull():
    not_full = True
    for i in game_board:
        if i.count(' ') > 0:
            not_full = False
    return not_full


# Determines if the space is empty
def empty_space(row, column):
    return game_board[row][column] == ' '


# Text gui for the game
def get_text(row, column, board, l1, l2):
    if board[row][column] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[row][column] = 'X'
        else:
            l1.config(state=ACTIVE)
            l2.config(state=DISABLED)
            board[row][column] = 'O'
        sign+1

# Create the game_board gui
def board_gui(board, l1, l2):
    button = []
    for row in range(3):
        m = 3 + row
        button.append(row)
        button[row] = []
        for column in range(3):
            n = column
            button[row].append(column)
        grab_text = partial(get_text, row, column, board, l1, l2)
        button[row][column] = Button(
            board, bd=5, command=grab_text, height=4, width=8)
        button[row][column].grid(rows=m, cols=n)
        board.mainloop()


# A window for multiplayer
def multi(board):
    board.destroy()
    board = Tk()
    board.title('Multiplayer')


# Creating the gui for the front game
def play():
    menu = Tk()
    menu.geometry('250x250')
    menu.title('Tic-Tac-Toe ')
    frame = Frame(menu)
    frame.pack()

    multi_game = partial(multi, menu)
    title = Label(frame, text="Tic Tac Toe")
    title.pack()

    multi_player_button = Button(menu, text='Multiplayer', command=multi_game, bg='blue', width=500)
    quit_button = Button(menu, text='Quit', bg='red', command=menu.quit, width=500)

    multi_player_button.pack()
    quit_button.pack()

    menu.mainloop()


if __name__ == '__main__':
    play()

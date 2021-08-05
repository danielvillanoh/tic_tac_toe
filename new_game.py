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


# A window for single player
def single(board):
    board.destroy()
    board = Tk()
    board.title('Single Player')


# A window for multiplayer
def multi(board):
    board.destroy()
    board = Tk()
    board.title('Multiplayer')


# Creating the gui for the game
def play():
    menu = Tk()
    menu.geometry('250x250')
    menu.title('Tic-Tac-Toe ')
    frame = Frame(menu)
    frame.pack()

    single_game = partial(single, menu)
    multi_game = partial(multi, menu)
    title = Label(frame, text="Tic Tac Toe")
    title.pack()

    s_player_button = Button(menu, text='Single Player', command=single_game, bg='blue', width=500)
    mult_player_button = Button(menu, text='Multiplayer', command=multi_game, bg='blue', width=500)
    quit_button = Button(menu, text='Quit', bg='red', command=menu.quit, width=500)

    s_player_button.pack()
    mult_player_button.pack()
    quit_button.pack()

    menu.mainloop()


if __name__ == '__main__':
    play()

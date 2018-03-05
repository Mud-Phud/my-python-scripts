#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 18:04:34 2018

@author: robert

Playing tic-tac-toe

"""


import numpy as np
import matplotlib.pyplot as plt
import random

# make a 3x3 board and fill with 0's...
def create_board():
    return np.zeros((3,3), dtype=int)

# player 1 = 1, player 2 = 2, 0 = blank space. This makes a move for player...
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    return board

# lists the open pair of coordinates...
def possibilities(board):
    (good_rows,good_columns)=np.where( board == 0 )
    good_list = [(good_rows[i],good_columns[i]) for i in range(len(good_rows))]
    return good_list

# moves to random spot...
def random_place(board, player):
    pos = random.choice(possibilities(board))
    return place(board, player, pos)

# test whether the player has three in a row on a row...
def row_win(board,player):
    return np.any([ np.all(board[i,:]==player) for i in range(3)])

# test whether the player has three in a row on a column...
def col_win(board,player):
    return np.any([ np.all(board[:,i]==player) for i in range(3)])

# test whether the player has three in a row on a diagonal...
def diag_win(board,player):
    UL_LR_bool = [board[i,i] == player for i in range(3)]
    UR_LL_bool = [board[i,2-i] == player for i in range(3)]
    return np.all(UL_LR_bool) or np.all(UR_LL_bool )


def evaluate(board):
    for player in [1, 2]:
        if (row_win(board,player) or 
        col_win(board,player) or
        diag_win(board,player)):
            return player
    if np.all(board != 0):
        return -1
    else: return 0

    
import time

def next_turn(player): 
    if player == 1: return 2
    else: return 1

def play_game():
    winner = 0
    player = 1
    
    board = create_board()
    #print("player ",player)
    #print("winner ",winner)
    #print(board)
    
    while  winner == 0:
        if winner == -1: 
            return winner
        board = random_place(board, player)
        winner = evaluate(board)
        player = next_turn(player)
        #print("player ",player)
        #print("winner ",winner) 
        #print(board)
    return winner

#%%

start = time.time()
outcomes = []
for i in range(1000):
    outcomes.append(play_game())
stop = time.time()
print(stop-start)

plt.hist(outcomes,bins=3)


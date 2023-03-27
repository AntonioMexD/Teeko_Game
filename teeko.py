import copy
import numpy as np

Board_Size = 4

#Players

Player_1 = 1
Player_2 = 2

#Turn

Move_Empty = 0
Move_Player1 = 1
Move_Player2 = 2

# Victory
WIN_VALUE = 1000000

# Depth limit
DEPTH_LIMIT = 3

# Definir la función heurística
def heuristic(board, player):
    # Contar el número de fichas del jugador en el tablero
    player_count = np.count_nonzero(board == player)
    # Calcular el número de líneas de tres fichas que el jugador tiene en el tablero
    lines = 0
    for i in range(Board_Size):
        for j in range(Board_Size):
            if board[i][j] == player:
                # Comprobar las líneas horizontales
                if j < Board_Size - 2 and board[i][j+1] == player and board[i][j+2] == player:
                    lines += 1
                # Comprobar las líneas verticales
                if i < Board_Size - 2 and board[i+1][j] == player and board[i+2][j] == player:
                    lines += 1
                # Comprobar las líneas diagonales ascendentes
                if i > 1 and j < Board_Size - 2 and board[i-1][j+1] == player and board[i-2][j+2] == player:
                    lines += 1
                # Comprobar las líneas diagonales descendentes
                if i < Board_Size - 2 and j < Board_Size - 2 and board[i+1][j+1] == player and board[i+2][j+2] == player:
                    lines += 1
    return player_count + lines * 10

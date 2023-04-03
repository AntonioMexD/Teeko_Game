# Teeko_Game
This is a simple implementation of the board game Teeko, along with an AI player that uses the minimax algorithm with alpha-beta pruning to play the game.

# Instructions 
To run the game, simply execute the file teeko.py. By default, the game will be played between a human player and the AI player, with the human player going first. To change the players, modify the play_game() function in teeko.py.

# Heuristic
In this heuristic, first it is checked whether player 1 has won the game (i.e., has managed to align four pieces in a row, column or diagonal), and if so, -1 is returned.

Then it is checked if player 2 has won the game, and if so, 1 is returned.

If neither player has won yet, 0 is returned, which means that the game is ongoing and there is no clear winner or loser in this position.

# Installation Guide
* Open your Python editor Ex. Visual Code
* Open the console
* Type the next command:
* python Game.py

To perform a movement, it must be done in the following way: 'row,col'
Where row is the row and col is the column.
For example, if I want to make my move in row 1 and column 2 I must do it in the following way:
1,2
import copy
import numpy as np
import math
import random

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

class Teeko:
    def __init__(self):
        self.board = np.zeros((4, 4), dtype=np.int8)
        self.current_player = 1

    def actions(self):
        actions = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    actions.append((i, j))
        return actions

    def result(self, action):
        i, j = action
        self.board[i][j] = self.current_player
        self.current_player = 2 if self.current_player == 1 else 1

    def is_terminal(self):
        if self.has_won(1) or self.has_won(2) or len(self.actions()) == 0:
            return True
        else:
            return False

    def has_won(self, player):
        for i in range(4):
            if (self.board[i][0] == player and self.board[i][1] == player
                    and self.board[i][2] == player and self.board[i][3] == player):
                return True
            if (self.board[0][i] == player and self.board[1][i] == player
                    and self.board[2][i] == player and self.board[3][i] == player):
                return True
        if (self.board[0][0] == player and self.board[1][1] == player
                and self.board[2][2] == player and self.board[3][3] == player):
            return True
        if (self.board[0][3] == player and self.board[1][2] == player
                and self.board[2][1] == player and self.board[3][0] == player):
            return True
        return False

    def heuristica(self):
        if self.has_won(1):
            return -1
        elif self.has_won(2):
            return 1
        else:
            return 0

    def minimax_alphabeta(self, depth, alpha, beta):
        if depth == 0:
            return self.heuristica()

        if self.current_player == 1:
            max_val = -np.inf
            for i in range(4):
                for j in range(4):
                    if self.board[i][j] == 0:
                        self.board[i][j] = self.current_player
                        self.current_player = 2
                        val = self.minimax_alphabeta(depth-1, alpha, beta)
                        self.board[i][j] = 0
                        self.current_player = 1
                        max_val = max(max_val, val)
                        alpha = max(alpha, max_val)
                        if beta <= alpha:
                            break
            return max_val
        else:
            min_val = np.inf
            for i in range(4):
                for j in range(4):
                    if self.board[i][j] == 0:
                        self.board[i][j] = self.current_player
                        self.current_player = 1
                        val = self.minimax_alphabeta(depth-1, alpha, beta)
                        self.board[i][j] = 0
                        self.current_player = 2
                        min_val = min(min_val, val)
                        beta = min(beta, min_val)
                        if beta <= alpha:
                            break
            return min_val
        
    def evaluate(self):
        return self.minimax_alphabeta(3, -np.inf, np.inf)
    
    def choose_move(self, depth):
        best_move = None
        if self.current_player == 1:
            best_val = -np.inf
            for action in self.actions():
                self.result(action)
                value = self.minimax_alphabeta(depth, -np.inf, np.inf)
                self.board[action] = 0
                self.current_player = 1
                if value > best_val:
                    best_val = value
                    best_move = action
        else:
            best_val = np.inf
            for action in self.actions():
                self.result(action)
                value = self.minimax_alphabeta(depth, -np.inf, np.inf)
                self.board[action] = 0
                self.current_player = 2
                if value < best_val:
                    best_val = value
                    best_move = action
        return best_move
        
    def play_game(self, player1, player2, print_board=True):
        """
        Play a game of Teeko between two players.
        """
        while not self.is_terminal():
            if self.current_player == 1:
                action = player1.get_action(self)
            else:
                action = player2.get_action(self)
            self.result(action)
            if print_board:
                print(self.board)
                print()
        if self.has_won(1):
            print("Player 1 wins!")
        elif self.has_won(2):
            print("Player 2 wins!")
        else:
            print("It's a tie!")


class HumanPlayer:
    """
    A human player for Teeko. Asks for user input to get the next action.
    """
    def get_action(self, game):
        print("Current board:")
        print(game.board)
        while True:
            move = input("Enter your move as 'row,col': ")
            move = move.split(",")
            try:
                move = tuple([int(x) for x in move])
                if move not in game.actions():
                    print("Invalid move.")
                else:
                    return move
            except ValueError:
                print("Invalid move.")

                
class RandomPlayer:
    """
    A player that chooses a random valid action.
    """
    def get_action(self, game):
        return random.choice(game.actions())


class MiniMaxPlayer:
    """
    A player that uses minimax with alpha-beta pruning to choose actions.
    """
    def __init__(self, depth):
        self.depth = depth

    def get_action(self, game):
        best_move = None
        if game.current_player == 1:
            best_score = -np.inf
            for move in game.actions():
                game_copy = copy.deepcopy(game)
                game_copy.result(move)
                score = game_copy.minimax_alphabeta(self.depth, -np.inf, np.inf)
                if score > best_score:
                    best_score = score
                    best_move = move
        else:
            best_score = np.inf
            for move in game.actions():
                game_copy = copy.deepcopy(game)
                game_copy.result(move)
                score = game_copy.minimax_alphabeta(self.depth, -np.inf, np.inf)
                if score < best_score:
                    best_score = score
                    best_move = move
        return best_move

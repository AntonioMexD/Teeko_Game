from teeko import Teeko
from teeko import HumanPlayer
from teeko import RandomPlayer
game = Teeko()
player1 = HumanPlayer()
player2 = RandomPlayer()
player3 = HumanPlayer()
player4 = RandomPlayer()
game.play_game(player1, player2)
# Game Files
from game import GenerateBoard, Player

game = GenerateBoard.Board(14)
board = game.generate()

player = Player.Player([0, 0], [[]])

from game import GenerateBoard
import pyglet

window = pyglet.window.Window()
window.clear()
pyglet.app.run()

board = GenerateBoard.Board(14)
state = board.generate()
# board.display()
# print(state)

from inspect import isfunction
from gameparts import Board

game = Board()

print(type(game))
print(dir(game))
print(isfunction(game.display))

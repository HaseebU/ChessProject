
import colorsys
from turtle import pen


class piece(object):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def printPiece(self):
        print(self.name + " ", end='')

class empty(piece):
    def __init__(self):
        self.name = '*'

class pawn(piece):
    def __init__(self, color, x, y):
        self.name = 'P'
        super().__init__(color, x, y)

    def islegal(self, x, y):
        
        return True

class rook(piece):
    def __init__(self, color, x, y):
        self.name = 'R'
        super().__init__(color, x, y)

class knight(piece):
    def __init__(self, color, x, y):
        self.name = 'N'
        super().__init__(color, x, y)

class bishop(piece):
    def __init__(self, color, x, y):
        self.name = 'B'
        super().__init__(color, x, y)

class queen(piece):
    def __init__(self, color, x, y):
        self.name = 'Q'
        super().__init__(color, x, y)

class king(piece):
    def __init__(self, color, x, y):
        self.name = 'K'
        super().__init__(color, x, y)




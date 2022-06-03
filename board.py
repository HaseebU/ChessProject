import numpy as np

from piece import pawn
from piece import rook
from piece import knight
from piece import bishop
from piece import queen
from piece import king
from piece import empty

class board():
    def __init__(self):
        self.board = np.empty([8, 8], dtype=object)
        self.reset()

    def reset(self):
        for i in range(2,6):
            for j in range(8):
                self.board[i][j] = empty()
        for j in range(8):
            self.board[1][j] = pawn("white", 1, j)
            self.board[6][j] = pawn("black", 6, j)
        #white
        self.board[0][0] = rook("white", 0, 0)
        self.board[0][1] = knight("white", 0, 1)
        self.board[0][2] = bishop("white", 0, 2)
        self.board[0][3] = king("white", 0, 3)
        self.board[0][4] = queen("white", 0, 4)
        self.board[0][5] = bishop("white", 0, 5)
        self.board[0][6] = knight("white", 0, 6)
        self.board[0][7] = rook("white", 0, 7)
        #black
        self.board[7][0] = rook("black", 7, 0)
        self.board[7][1] = knight("black", 7, 1)
        self.board[7][2] = bishop("black", 7, 2)
        self.board[7][3] = king("black", 7, 3)
        self.board[7][4] = queen("black", 7, 4)
        self.board[7][5] = bishop("black", 7, 5)
        self.board[7][6] = knight("black", 7, 6)
        self.board[7][7] = rook("black", 7, 7)

    def move(self, prev, now):
        
        pass

    def printBoard(self):
        for i in range(8):
            for j in range(8):
                self.board[i][j].printPiece()
            print()

if __name__ == '__main__':
    run = board()
    run.printBoard()


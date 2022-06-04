import unittest
from board import board
from piece import pawn
from piece import rook
from piece import knight
from piece import bishop
from piece import queen
from piece import king
from piece import empty

class TestStringMethods(unittest.TestCase):

    def test_Board(self):
        run = board()
        run.printBoard()
        #pond white
        self.assertTrue(run.getPiece(0,1).getName() == 'P')
        self.assertTrue(run.getPiece(4,1).getName() == 'P')
        self.assertTrue(run.getPiece(7,1).getName() == 'P')

        #pond black
        self.assertTrue(run.getPiece(0,6).getName() == 'P')
        self.assertTrue(run.getPiece(4,6).getName() == 'P')
        self.assertTrue(run.getPiece(7,6).getName() == 'P')

        #piece white
        self.assertTrue(run.getPiece(0,0).getName() == 'R')
        self.assertTrue(run.getPiece(1,0).getName() == 'N')
        self.assertTrue(run.getPiece(2,0).getName() == 'B')
        self.assertTrue(run.getPiece(3,0).getName() == 'K')
        self.assertTrue(run.getPiece(4,0).getName() == 'Q')
        self.assertTrue(run.getPiece(5,0).getName() == 'B')
        self.assertTrue(run.getPiece(6,0).getName() == 'N')
        self.assertTrue(run.getPiece(7,0).getName() == 'R')

        #piece white
        self.assertTrue(run.getPiece(0,7).getName() == 'R')
        self.assertTrue(run.getPiece(1,7).getName() == 'N')
        self.assertTrue(run.getPiece(2,7).getName() == 'B')
        self.assertTrue(run.getPiece(3,7).getName() == 'K')
        self.assertTrue(run.getPiece(4,7).getName() == 'Q')
        self.assertTrue(run.getPiece(5,7).getName() == 'B')
        self.assertTrue(run.getPiece(6,7).getName() == 'N')
        self.assertTrue(run.getPiece(7,7).getName() == 'R')

        #test color
        self.assertTrue(run.getPiece(0,0).getColor() == "white")
        self.assertTrue(run.getPiece(4,1).getColor() == "white")
        self.assertTrue(run.getPiece(3,7).getColor() == "black")
        self.assertTrue(run.getPiece(7,6).getColor() == "black")
        
    def test_pawn(self):
        run = board()

        #good test
        self.assertTrue(run.move([0,1],[0,2]))
        self.assertTrue(run.getPiece(0,2).getName() == 'P')
        self.assertTrue(run.move([1,1],[1,3]))
        self.assertTrue(run.getPiece(1,3).getName() == 'P')
        #fail case
        self.assertFalse(run.move([2,1],[2,4]))
        self.assertTrue(run.getPiece(2,1).getName() == 'P')
        #summon black pawn
        run.board[4,2] = rook("black", 4, 2)

        #capture piece
        self.assertTrue(run.move([1,3],[2,4]))
        self.assertTrue(run.getPiece(2,4).getName() == 'P')
        run.printBoard()

    def test_bishop(self):
        run = board()
	    #good test
        self.assertTrue(run.move([1,0],[0,2]))
        self.assertTrue(run.move([0,2],[2,4]))


if __name__ == '__main__':
    unittest.main()
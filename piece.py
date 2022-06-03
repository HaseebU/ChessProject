
import colorsys
from pickle import TRUE
from re import X
from tkinter import Y
from turtle import pen


class piece(object):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def printPiece(self):
        print(self.name + " ", end='')
    
    def setCord(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getColor(self):
        return self.color

    def isEmpty(self):
        return self.empty

class empty(piece):
    def __init__(self):
        self.name = '*'
        self.empty = True

class pawn(piece):
    def __init__(self, color, x, y):
        self.name = 'P'
        self.empty = False
        super().__init__(color, x, y)

    def islegal(self, prev, now):
        if(prev.getX() != now.getX()):
            return False
        
        if(prev.getColor() == "white"):
            if(now.getY()-prev.getY() == 1):
                return True
            elif(now.getY()-prev.getY() == 2):
                if(now.getY() == 1):
                    return True

        elif(prev.getColor() == "black"):
            if(now.getY()-prev.getY() == -1):
                return True
            elif(now.getY()-prev.getY() == -2):
                if(now.getY() == 6):
                    return True

        return False

    def promotion(self, prev, now):
        if(prev.getColor() == "white" and now.getY() == 7):
            return True


class rook(piece):
    def __init__(self, color, x, y):
        self.name = 'R'
        self.empty = False
        super().__init__(color, x, y)

    def islegal(self, prev, now):
        if(prev.getX() != prev.getX() and prev.getY() == prev.getY()):
            return True
        if(prev.getY() != prev.getY() and prev.getX() == prev.getX()):
            return True
        return False


class knight(piece):
    def __init__(self, color, x, y):
        self.name = 'N'
        self.empty = False
        super().__init__(color, x, y)                
    def islegal(self, prev, now):
	    if(((prev.getX() + 2 == now.getX() or prev.getX() - 2 == now.getX()) and (prev.getY() + 1 == now.getY() or prev.getY() - 1 == now.getY())) or ((prev.getX() + 1 == now.getX() or prev.getX() - 1 == now.getX()) and (prev.getY() + 2 == now.getY() or prev.getY() - 2 == now.getY()))):
		    return True
        else:
	        return False

    
	    #if(prev.getX() + 3 == now.getX() or prev.getX() - 3 == now.getX() or prev.getX() + 1 == now.getX() or prev.ge    tX() - 1 == now.getX()):
		    #return True
        #if (prev.getY() + 3 == now.getY() or prev.getY() - 3 == now.getY() or prev.getY() + 1 == now.getY() or prev.getY() - 1 == now.getY()):
	        #return True
        #return False
	        #return True
        #return False


class bishop(piece):
    def __init__(self, color, x, y):
        self.name = 'B'
        self.empty = False
        super().__init__(color, x, y)

    def islegal(self, prev, now):
        if(abs(prev.getX()-now.getX()) == abs(prev.getY()-now.getY())):
            return True
        return False
         
class queen(piece):
    def __init__(self, color, x, y):
        self.name = 'Q'
        self.empty = False
        super().__init__(color, x, y)

    def islegal(self, prev, now):
        if(abs(prev.getX()-now.getX()) == abs(prev.getY()-now.getY())):
            return True
        if(prev.getX() != prev.getX() and prev.getY() == prev.getY()):
            return True
        if(prev.getY() != prev.getY() and prev.getX() == prev.getX()):
            return True
        return False

class king(piece):
    def __init__(self, color, x, y):
        self.name = 'K'
        self.empty = False
        super().__init__(color, x, y)

    def islegal(self, prev, now):
        if(abs(now.getY()-prev.getY()) > 1):
            return False
        if(abs(now.getX()-prev.getX()) > 1):
            return False
        return True




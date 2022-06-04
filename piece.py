class piece(object):
    def __init__(self, color, y, x):
        self.color = color
        self.x = x
        self.y = y

    def printPiece(self):
        print(self.name + " ", end='')
    
    def getName(self):
        return self.name

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
    def __init__(self, y, x):
        self.name = '*'
        self.empty = True
        self.color = "*"
        self.x = x
        self.y = y
    
    def isLegal(self, board, prev, now):
        return False

class pawn(piece):
    def __init__(self, color, y, x):
        self.name = 'P'
        self.empty = False
        super().__init__(color, y, x)

    def isLegal(self, board, prev, now):
        if(prev.getX() != now.getX()):
            if(abs(prev.getX()-now.getX()) == 1):
                if(prev.getColor() == "white"):
                    if(prev.getY()-now.getY() == -1):
                        if(not now.isEmpty() and now.getColor() != prev.getColor()):
                            return True
                else:
                    if(prev.getY()-now.getY() == 1):
                        if(not now.isEmpty() and now.getColor() != prev.getColor()):
                            return True
            return False
        
        if(abs(now.getY()-prev.getY()) == 1):
            if(board[now.getY()][now.getX()].isEmpty()):
                return True

        if(prev.getColor() == "white"):
            if(now.getY()-prev.getY() == 2):
                if(prev.getY() == 1):
                    if(board[now.getY()][now.getX()].isEmpty() and board[now.getY()-1][now.getX()].isEmpty()):
                        return True

        elif(prev.getColor() == "black"):
            if(now.getY()-prev.getY() == -2):
                if(prev.getY() == 6):
                    if(board[now.getY()][now.getX()].isEmpty() and board[now.getY()+1][now.getX()].isEmpty()):
                        return True

        return False

    def promotion(self, prev, now):
        if(prev.getColor() == "white" and now.getY() == 7):
            return True
        if(prev.getColor() == "black" and now.getY() == 0):
            return True
        return False

    #def promotionChoice(self):
        #if(promotion(self, prev, now)):

class rook(piece):
    def __init__(self, color, y, x):
        self.name = 'R'
        self.empty = False
        super().__init__(color, y, x)

    def isLegal(self, board, prev, now):
        if(prev.getY() < now.getY()):
            for i in range(prev.getY()+1, now.getY()):
                if(not board[i][prev.getX()].isEmpty() or prev.getColor() == now.getColor()):
                    return False
        elif(prev.getY() > now.getY()):
            for i in range(now.getY()+1, prev.getY()):
                if(not board[i][prev.getX()].isEmpty() or prev.getColor() == now.getColor()):
                    return False
        if(prev.getX() < now.getX()):
            for i in range(prev.getX()+1, now.getX()):
                if(not board[prev.getY()][i].isEmpty() or prev.getColor() == now.getColor()):
                    return False
        elif(prev.getX() > now.getX()):
            for i in range(now.getX()+1, prev.getX()):
                if(not board[prev.getY()][i].isEmpty() or prev.getColor() == now.getColor()):
                    return False
        if(prev.getColor() == now.getColor()):
            return False

        return True


class knight(piece):
    def __init__(self, color, y, x):
        self.name = 'N'
        self.empty = False
        super().__init__(color, y, x)

    def isLegal(self, board, prev, now):
        if(abs(prev.getX()-now.getX()) == 2 and abs(prev.getY()-now.getY()) == 1):
            if(now.getColor() != prev.getColor()):
               return True
        if(abs(prev.getX()-now.getX()) == 1 and abs(prev.getY()-now.getY()) == 2):
            if(now.getColor() != prev.getColor()):
               return True
        return False

class bishop(piece):
    def __init__(self, color, y, x):
        self.name = 'B'
        self.empty = False
        super().__init__(color, y, x)

    def isLegal(self, board, prev, now):
        if(abs(prev.getX()-now.getX()) == abs(prev.getY()-now.getY())):
            if(prev.getX() < now.getX()):
                for i in range(prev.getX()+1, now.getX()):
                    if(prev.getY() < now.getY()):
                        for j in range(prev.getY()+1, now.getY()): 
                            if(not board[j][i].isEmpty() or prev.getColor() == now.getColor()):
                                return False
                    elif(prev.getY() > now.getY()):
                        for j in range(now.getY()+1, prev.getY()): 
                            if(not board[j][i].isEmpty() or prev.getColor() == now.getColor()):
                                return False
            elif(prev.getX() > now.getX()):
                for i in range(now.getX()+1, prev.getX()):
                    if(prev.getY() < now.getY()):
                        for j in range(prev.getY()+1, now.getY()): 
                            if(not board[j][i].isEmpty() or prev.getColor() == now.getColor()):
                                return False
                    elif(prev.getY() > now.getY()):
                        for j in range(now.getY()+1, prev.getY()): 
                            if(not board[j][i].isEmpty() or prev.getColor() == now.getColor()):
                                return False
            if(prev.getColor() == now.getColor()):
                return False
            return True
        return False

class queen(piece):
    def __init__(self, color, y, x):
        self.name = 'Q'
        self.empty = False
        super().__init__(color, y, x)

    def isLegal(self, board, prev, now):
        if(abs(prev.getX()-now.getX()) == abs(prev.getY()-now.getY())):
            if(prev.getX() < now.getX()):
                for i in range(prev.getX()+1, now.getX()):
                    if(prev.getY() < now.getY()):
                        for j in range(prev.getY()+1, now.getY()): 
                            if(not board[j][i].isEmpty() or prev.getColor() == now.getColor()):
                                return False
                    elif(prev.getY() > now.getY()):
                        for j in range(now.getY()+1, prev.getY()): 
                            if(not board[j][i].isEmpty() or prev.getColor() == now.getColor()):
                                return False
            elif(prev.getX() > now.getX()):
                for i in range(now.getX()+1, prev.getX()):
                    if(prev.getY() < now.getY()):
                        for j in range(prev.getY()+1, now.getY()): 
                            if(not board[j][i].isEmpty() or prev.getColor() == now.getColor()):
                                return False
                    elif(prev.getY() > now.getY()):
                        for j in range(now.getY()+1, prev.getY()): 
                            if(not board[j][i].isEmpty() or prev.getColor() == now.getColor()):
                                return False
            if(prev.getColor() == now.getColor()):
                return False
            return True

        if(prev.getY() < now.getY()):
            for i in range(prev.getY()+1, now.getY()):
                if(not board[i][prev.getX()].isEmpty() or prev.getColor() == now.getColor()):
                    return False
        elif(prev.getY() > now.getY()):
            for i in range(now.getY()+1, prev.getY()):
                if(not board[i][prev.getX()].isEmpty() or prev.getColor() == now.getColor()):
                    return False
        if(prev.getX() < now.getX()):
            for i in range(prev.getX()+1, now.getX()):
                if(not board[prev.getY()][i].isEmpty() or prev.getColor() == now.getColor()):
                    return False
        elif(prev.getX() > now.getX()):
            for i in range(now.getX()+1, prev.getX()):
                if(not board[prev.getY()][i].isEmpty() or prev.getColor() == now.getColor()):
                    return False
        if(prev.getColor() == now.getColor()):
            return False

        return True

class king(piece):
    def __init__(self, color, y, x):
        self.name = 'K'
        self.empty = False
        super().__init__(color, y, x)

    def isLegal(self, board, prev, now):
        if(abs(now.getY()-prev.getY()) > 1):
            return False
        if(abs(now.getX()-prev.getX()) > 1):
            return False
        if(now.getColor() == prev.getColor()):
            return False
        return True




from board import board
from player import white
from player import black


if __name__ == '__main__':
    run = board()
    run.printBoard()

    gameOver = False
    turn = True
    moveP = ""

    while(not gameOver):
        if(turn):
            moveP = input("enter move white, [1-8]+[1-8]+[1-8]+[1-8] eg. 1112 : ")
        else:
            moveP = input("enter move black, [1-8]+[1-8]+[1-8]+[1-8] eg. 1112 : ")
        if(len(moveP) == 4):
            if(turn == True):
                try:
                    if(run.board[int(moveP[1])-1,int(moveP[0])-1].getColor() == "white"):
                        run.move([int(moveP[0])-1,int(moveP[1])-1],[int(moveP[2])-1,int(moveP[3])-1])
                        turn = False
                except:
                    pass
            if(turn == False):
                try:
                    if(run.board[int(moveP[1])-1,int(moveP[0])-1].getColor() == "black"):
                        run.move([int(moveP[0])-1,int(moveP[1])-1],[int(moveP[2])-1,int(moveP[3])-1])
                        turn = True
                except:
                    pass

        print()
        run.printBoard()





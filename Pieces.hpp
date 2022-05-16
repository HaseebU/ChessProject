#ifndef __PIECES_H__
#define __PIECES_H__

#include "tile.hpp"
#include "board.hpp"

#include <cstring>
#include <string>
#include <iostream>

using namespace std;

class Pieces {
protected:
    char name;
    char color;
    int xPos, yPos;

public:
    Pieces() : color('*'), xPos(0), yPos(0) { }
    Pieces(char c, int x, int y) : color(c), xPos(x), yPos(y) { }
    virtual ~Pieces() = default;
    char getName() { return name; }
    int getXPos() { return xPos; }
    int getYPos() { return yPos; }
    void setXPos(int xPos) { this->xPos = xPos; }
    void setXPos(int yPos) { this->yPos = yPos; }
    bool move(int xMove, int yMove) { xPos = xMove; yPos = yMove; }
    bool isLegal();
};

class Pawn : public Pieces {
private:
    char name = 'C';
public:
    Pawn() : Pieces() { }
    Pawn(char c, int x, int y) : Pieces(c, x, y) { }
    virtual bool isLegal(int xMove, int yMove);
};

class King : public Pieces {
private:
    char name = 'K';
    int movesMade = 0;
public:
    King() : Pieces() { }
    King(char c, int x, int y) : Pieces(c, x, y) { }
    virtual bool isLegal(int xMove, int yMove);

    int getMovesMade() { return movesMade; }
    void addMovesMade() { movesMade++; }
};

class Queen : public Pieces {
private:
    char name = 'Q';
public:
    Queen() : Pieces() { }
    Queen(char c, int x, int y) : Pieces(c, x, y) { }
    virtual bool isLegal(int xMove, int yMove);
};

class Rook : public Pieces {
private:
    char name = 'R';
    int movesMade = 0;
public:
    Rook() : Pieces() { }
    Rook(char c, int x, int y) : Pieces(c, x, y) { }
    virtual bool isLegal(int xMove, int yMove);

    int getMovesMade() { return movesMade; }
    void addMovesMade() { movesMade++; }
};

class Knight : public Pieces {
private:
    char name = 'N';
public:
    Knight() : Pieces() { }
    Knight(char c, int x, int y) : Pieces(c, x, y) { }
    virtual bool isLegal(int xMove, int yMove);
};

class Bishop : public Pieces {
private:
    char name = 'B';
public:
    Bishop() : Pieces() { }
    Bishop(char c, int x, int y) : Pieces(c, x, y) { }
    virtual bool isLegal(int xMove, int yMove);
};

#endif // __PIECES_H__

#ifndef __BOARD_H__
#define __BOARD_H__

#include "tile.hpp"

#include <cstring>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Board {
private:
    Tile board[8][8];
public:
    Board();
    void initializeBoard();
    Tile getTile(int i, int j);
    void undoMove();

};

#endif

#ifndef __TILE_H__
#define __TILE_H__

#include "Tile.hpp"
#include "Pieces.hpp"

#include <cstring>
#include <string>
#include <iostream>

using namespace std;

class Tile {
private:
	bool isOccupied;
	Pieces* piece = nullptr;
public:
	Tile() : isOccupied(false) { }
	bool checkOccupied() { return isOccupied; }
	void changeStatus(bool status) { isOccupied = status; }
	void placePiece(char piece, char color, int x, int y);

	void removePiece(char piece);
};

#endif

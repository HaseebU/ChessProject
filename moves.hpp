#ifndef MOVES_HPP
#define MOVES_HPP

#include <cstring>
#include <string>
#include <iostream>

using namespace std;

class Moves {
	protected:
	char name;
	char color;
	int x;
	int y;

	public:
	Moves();
	Moves(char col, int xpos, int ypos);
	virtual ~Moves();
	char name();
	int xPos();
	int yPos();
	void castle();
	void promote();
	void enPassant();
};

#endif MOVES_HPP

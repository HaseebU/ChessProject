#include "moves.hpp"

using namespace std;

Moves::Moves() {
	color = '*';
	x = 0;
	y = 0;
}

Moves::Moves(char col, int xpos, int ypos) {
	color = col;
	x = xpos;
	y = ypos;
}

char Moves::name() {
	return name;
}

int Moves::xPos() {
	return x;
}

int Moves::yPos() {
	return y;
}

void Moves::castle() {
	
}

void Moves::promote() {
	
}

void Moves::enPassant() {
	
}

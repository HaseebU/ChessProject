#include "Board.hpp"

Board::Board() {
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			board[i][j] = Tile();
		}
	}
}

void Board::initializeBoard() {
	string layout = "RNBQKBNR";
	char color = 'w';
	for (int i = 0; i < 7; i += 7) {
		if (i > 1) { color = 'b'; }
		for (int j = 0; j < layout.length(); j++) {
			board[i][j].placePiece((char)layout.at(j), color, i, j);
		}
	}
	for (int i = 1; i < 7; i += 4) {
		if (i > 1) { color = 'b'; }
		for (int j = 0; j < 7; j++) {
			board[i][j].placePiece('P', color, i, j);
		}
	}
}

Tile Board::getTile(int i, int j) { 
	return board[i][j]; 
}


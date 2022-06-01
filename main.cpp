#include <SFML/Graphics.hpp>
#include <time.h>
using namespace sf;

#include <iostream>



const int size = 76;           //Used for grid size in pieces.png

Sprite pieceSprites[32];       //Array of all Sprites for chess pieces

//Stub Init, Eventually should get board data from Board class//
//6->Pawn           //3->Bishop
//5->Rook           //2->Queen
//4->Knight         //1->King
//Positive->White   //Negative->Black
int boardNums[8][8] =  {-5, -4, -3, -1, -2, -3, -4, -5,
                        -6, -6, -6, -6, -6, -6, -6, -6,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        6, 6, 6, 6, 6, 6, 6, 6,
                        5, 4, 3, 1, 2, 3, 4, 5};

//Sets the size and position of the piece sprites
void populateSprites() {
    int k = 0;

    for (int i=0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            int pieceNum = boardNums[i][j];     //The int stored at location i, j in the boardNums array

            if (pieceNum != 0) {                //Skip 0's
                int x = abs(pieceNum) - 1;      //Select the type of Piece this will be
                int y;
                if (pieceNum < 0 ) {y = 1;}     //For negative numbers choose from the black sprites from the bottom row of pieces.png
                if (pieceNum > 0 ) {y = 0;}     //For postitive numbers choose from the white sprites from top row of pieces.png

                pieceSprites[k].setTextureRect(IntRect(x*size, y*size, size, size));    //Determines the section of pieces.png that will be assigned to this sprite
                pieceSprites[k].setPosition(size*j, size*i);                            //Determines this sprites position on the board

                k++;
            }
        }
    }
}

int main() {
    RenderWindow window(VideoMode(612, 612), "CHESS");

    Texture t1, t2;
    t1.loadFromFile("images/pieces.png");
    t2.loadFromFile("images/board.png");

    for (int i=0; i<32; i++) {pieceSprites[i].setTexture(t1);}  //Assign all pieces sprites to the pieces.png texture
    populateSprites();

    Sprite sBoard(t2);          //Assign Sprite to board.png texture
    int movePiece = 0;          //Tracks which piece in the piece sprites array is to be moved

    bool moving = false;        //Tracks if a piece is being moved
    int px = 0, py = 0;

    while (window.isOpen()) {
        Vector2i mouseVec = Mouse::getPosition(window);

        Event e;
        while (window.pollEvent(e)) {

            //Check if window is still opened
            if (e.type == Event::Closed) {
                window.close();
            }
            
            //Pick up object
            if (e.type == Event::MouseButtonPressed) {
                if (e.key.code == Mouse::Left) {
                    for (int i=0; i<32; i++) {
                        if (pieceSprites[i].getGlobalBounds().contains(mouseVec.x,mouseVec.y)) {
                            movePiece = i;      //indicate the piece in pieceSprites to be moved
                            moving = true;
                            
                            px = mouseVec.x - pieceSprites[i].getPosition().x;
                            py = mouseVec.y - pieceSprites[i].getPosition().y;
                        }
                    }
                }
            }

            //Drop object
            if (e.type == Event::MouseButtonReleased) {
                if (e.key.code == Mouse::Left) {
                    moving = false;
                    pieceSprites[movePiece].setScale(1, 1);
                }
            }

            //Update position of the piece that is being moved
            if (moving) {
                pieceSprites[movePiece].setScale(1.1f, 1.1f);
                pieceSprites[movePiece].setPosition(mouseVec.x-px, mouseVec.y-py);      //Center the piece on the mouse while moving
            }
        }

        //display
        window.clear();
        window.draw(sBoard);
        for (int i=0; i<32; i++) {window.draw(pieceSprites[i]);}
        window.display();
    } //End WindowIsOpen
    return 0;
} //End main
# Chess UI
 
Authors: \<[Aaron Song](https://github.com/AaronSxng)\> \<[Jingfang Guan](https://github.com/alexgjf)\> \<[Haseeb Umerani](https://github.com/HaseebU)\> \<[Jordan Peck](https://github.com/Mimin7447)\>

## Project Description
  * Why is it important or interesting to you?
    * Programming a chess game is interesting because there are a lot of specific rules to the game. The game requires you to know how each pieces moves as well as how it captures and wins. Because of this, programming the game can be a challenge since we don't want the user making ilegal moves.
  * What languages/tools/technologies do you plan to use? (This list may change over the course of the project)
    * [C++](https://www.cplusplus.com/) - Language for classes and objects
    * [Python](https://www.python.org/) - Language for gui and ai
    * [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python GUI
  * What will be the input/output of your project? What are the features that the project provides?
    * The output of the program will be the chess board along with the pieces. The input is the players movement. Some of the features may include a timer, an undo button, and a simple ai. The chess program will have a menu page and a fully functional board and pieces. These pieces and boards will have individual roles that work together. The features added to the game is mainly for ease of use.
 
## Class Diagram
![uml](https://user-images.githubusercontent.com/74108022/168510055-6965784f-cbfc-4f2d-8895-fa856f4bf2b9.PNG)


Description: 
* **Game** class is the driver for our program and has an instance of a board, all 32 pieces, and both players. It initializes the board and displays the game to the GUI.
* **Chess Piece** keeps track of its own position and has a unique move method defnied in its subclass (Pawns also handle their own promotion). Has a color, type, and a counter for how many moves it has made.
* **Chess Board** Records the moves that have been played and tracks the state of the game. Determines if a player is in check, Who's turn it is, and can undo turns.
* **Player** has a color which it declares. Determines when it is it's time to play.
 
 > ## Phase III
 > In our project we used both **strategy** design patterns. For the implementation of our chess pieces, we used a **strategy** pattern in that each piece has a different **'move' strategy**. Since the chess pieces are very similar, we were able to simplify our code by using an abstract class **Pieces**. Because of this, we only had to define the **'move' strategy** that is unique to each piece. We also used the **composition** design pattern to implement our **board** class. The board is composed of 64 tiles. This allows us to compartmentalize our code so that board is not too cluttered. It also allows us to make many instances of the 'tile' class which all have the same behavior. Overall the use of these design patterns helped us to cooperate more smoothly and to create more readable code.
 
 > ## Final deliverable
 > All group members will give a demo to the TA/reader during lab time. The TA/reader will check the demo and the project GitHub repository and ask a few questions to all the team members. 
 > Before the demo, you should do the following:
 > * Complete the sections below (i.e. Screenshots, Installation/Usage, Testing)
 > * Plan one more sprint (that you will not necessarily complete before the end of the quarter). Your In-progress and In-testing columns should be empty (you are not doing more work currently) but your TODO column should have a full sprint plan in it as you have done before. This should include any known bugs (there should be some) or new features you would like to add. These should appear as issues/cards on your Project board.
 > * Make sure your README file and Project board are up-to-date reflecting the current status of your project (e.g. any changes that you have made during the project such as changes to your class diagram). Previous versions should still be visible through your commit history. 
 
 ## Screenshots
 > Screenshots of the input/output after running your application
 > ![image](https://user-images.githubusercontent.com/46555484/171975710-5c3156b0-fcc3-41f5-8e55-0158d436ef85.png)
 > ![image (1)](https://user-images.githubusercontent.com/46555484/171975779-0208e66f-fb9b-4efb-be5a-df7f7f6a529d.png)

 ## Installation/Usage
 > Instructions on installing and running your application
 > * Download Python 3.10.
 > * Download the following Graphics library for the GUI: https://www.sfml-dev.org/download/sfml/2.5.1/
 > * In board.py, we input numpy library and it is used for working with the board arrays or matrice.
 ## Testing
 > How was your project tested/validated? If you used CI, you should have a "build passing" badge in this README.
 > * The first test case is testing when the chess board is initialized, are all chess pieces at the correct position, class, and color.
 > * We unit tested each function for the individual pieces, such as getX, getY, move (different movement mechanisms for each piece), color, collision, capturing, etc.
 > * More specifically, each piece of chess(pawn, rook, biship, king, knight, queen) are tested for all movements following its rule, including capturing opponents' pieces and not capturing teammates. It also passed the test for chess pieces that move more than 1 space are not jumping over any non empty tile. 
 > * There are also test cases for pieces to detect illegal movement of each kind of chess that should return false when it happens.
 

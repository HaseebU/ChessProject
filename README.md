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
![uml](https://user-images.githubusercontent.com/74108022/168495870-377bf873-e795-4b7f-9990-4ab27a3156ea.PNG)

Description: 
* **Game** class is the driver for our program and has an instance of a board, all 32 pieces, and both players. It initializes the board and displays the game to the GUI.
* **Chess Piece** keeps track of its own position and has a unique move method defnied in its subclass (Pawns also handle their own promotion). Has a color, type, and a counter for how many moves it has made.
* **Chess Board** Records the moves that have been played and tracks the state of the game. Determines if a player is in check, Who's turn it is, and can undo turns.
* **Square** composite class of **Chess Board** (has 64 squares). Has a color, reports if it is occupied and by what piece.
* **Player** has a color which it declares. Determines when it is it's time to play.
 
 > ## Phase III
 > You will need to schedule a check-in for the second scrum meeting with the same reader you had your first scrum meeting with (using Calendly). Your entire team must be present. This meeting will occur on week 8 during lab time.
 > * Before the meeting you should perform a sprint plan like you did in Phase II.
 > * You should also update this README file by adding the following:
 >   * What design pattern(s) did you use? For each pattern you must explain in 4-5 sentences:
 >     * Why did you pick this pattern? And what feature did you implement with it?
 >     * How did the design pattern help you write better code?
 >   * An updated class diagram that reflects the design pattern(s) you used. You may combine multiple design patterns into one diagram if you'd like, but it needs to be clear which portion of the diagram represents which design pattern (either in the diagram or in the description).
 >   * Make sure your README file (and Project board) are up-to-date reflecting the current status of your project. Previous versions of the README file should still be visible through your commit history.
> 
> During the meeting with your reader you will discuss: 
 > * How effective your last sprint was (each member should talk about what they did)
 > * Any tasks that did not get completed last sprint, and how you took them into consideration for this sprint
 > * Any bugs you've identified and created issues for during the sprint. Do you plan on fixing them in the next sprint or are they lower priority?
 > * What tasks you are planning for this next sprint.

 
 > ## Final deliverable
 > All group members will give a demo to the TA/reader during lab time. The TA/reader will check the demo and the project GitHub repository and ask a few questions to all the team members. 
 > Before the demo, you should do the following:
 > * Complete the sections below (i.e. Screenshots, Installation/Usage, Testing)
 > * Plan one more sprint (that you will not necessarily complete before the end of the quarter). Your In-progress and In-testing columns should be empty (you are not doing more work currently) but your TODO column should have a full sprint plan in it as you have done before. This should include any known bugs (there should be some) or new features you would like to add. These should appear as issues/cards on your Project board.
 > * Make sure your README file and Project board are up-to-date reflecting the current status of your project (e.g. any changes that you have made during the project such as changes to your class diagram). Previous versions should still be visible through your commit history. 
 
 ## Screenshots
 > Screenshots of the input/output after running your application
 ## Installation/Usage
 > Instructions on installing and running your application
 ## Testing
 > How was your project tested/validated? If you used CI, you should have a "build passing" badge in this README.
 

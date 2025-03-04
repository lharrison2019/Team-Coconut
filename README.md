
An explanation of the purpose of each file in your repository

go_fish.py: our overall code to play the game go fish in visual studio code without GUI. 

go_fish_with_GUI.py: modified version of go_fish.py that will run the GUI using GUI.py 

GUI.py: script to build the GUI and control/add all of its widgets. 


Clear instructions on how to run your program from the command line:

In Terminal: There is one expected argument that the human player needs to imput which is their player name. There is also one optional argument which is the computer name. Example the user would type in the terminal on their mac is: python3 go_fish.py Lindsay.To give the computer a name, the format to run the game would be: python3 go_fish.py human_name -c computer_name. From there the user is asked if they want to play the game, which they can either answer "yes" or "no". If the human player/user answers "yes" then the game begins. Throughout the game the user will be prompted to type in a rank [2,3,4,5,6,7,8,9,10,jack,queen,king,ace] when it is their turn. The game will end when there are no more cards left in the deck or a player has ran out of cards.



With GUI: There is one expected argument that the human player needs to imput which is their player name. There is also one optional argument which is the computer name. Example the user would type in the terminal on their mac is: python3 go_fish_with_GUI.py Lindsay. To give the computer a name, the format to run the game would be: python3 go_fish_with_GUI.py human_name -c computer_name


Clear instructions on how to use your program and/or interpret the output of the program, as applicable:
Once the game is properly run through the command line by typing "python3 go_fish.py username" the human player is ased if they want to begin the game. They can either answer by typing "yes" to play the game or "no" to not play the game. If the user answers "yes" then the game begins. The human player will be dealt seven typical playing cards randomly called their "hand". A score is also depicted, however since the game has just started the scores are both zero. Next the human player is asked to request a rank. A rank can be [2,3,4,5,6,7,8,9,10,jack,queen,king,ace]. There are then two possible outcomes that will happen. The first possibility is that the computer player has the requested rank and must give it to you. Or the second possibility is that the computer player does not have the requested rank so you must "go fish", which means a random card will be given to you from the deck. Next, will be the computer player's turn. The computer will follow the same instructions as the human player just did. The goal of the game is to request ranks to create what is called a book. A book is a collection of four cards with the same rank. When either the human or computer player collects a book those cards go away from the players hand and generate one point. The game will end when there are no cards left in the deck to draw from or a player no longer has anymore cards. The winner is declared by the player who has the most points(books) at the end of the game.



An annotated bibliography of all sources you used to develop your project. For each source, explain how you used the source.

JackJack  4, et al. “How to Pass Arguments to a Button Command in Tkinter?” Stack Overflow, 1 Sept. 1959, https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter. 

 I used this stack overflow forum to help me figure out how to input multiple arguments into the command arguement for the buttons with the use of the partial() method found in the functools module. 


Paned Windows - Python Tkinter Gui Tutorial #48 - YouTube. https://www.youtube.com/watch?v=9Hyltpk2tSM. 

This tutorital was used for creating and setting up the different panels and adding them to the window in the desired fashion. 


“Tkinter - Python Interface to TCL/TK¶.” Tkinter - Python Interface to Tcl/Tk - Python 3.10.1 Documentation, https://docs.python.org/3/library/tkinter.html. 

This is the offical documentation for the module, tkinter. Nour used this documentation as a general reference for creating the different widgets used in the 
GUI.py script. 

“Go Fish Rules and Gameplay.” Ducksters, https://www.ducksters.com/games/go_fish_rules.php. 

We used this as a reference for the rules of go fish.


Attributions: Author of each method/function
make_deck(): Lindsay 
deal(num_of_cards): Nour
end_game(player_one, player_two): Subaita
__init__(self, name): Nour
print_board(self, other): Enrique
check_hand(self, other, req_rank): Lindsay & Nour
has_book(self): Enrique
draw(self): Subaita
HumanPlayer request_card(self, other): Subaita
ComputerPlayer request_card(self, other): Nour
main(human_name, computer_name): Enrique & Subaita
GUI.py: Nour
go_fish_with_GUI.py modified by Nour

All though we wrote down these specific contributions it is important to note that this was a collaborative effort and most of the time each member had some sort of contribution to everything even if it was small. The GUI section was completely Nour and she decided to figure this out on her own to make our game look much more presentable to a player, which was a wonderful addition to the project. 















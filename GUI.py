import go_fish_with_GUI
from tkinter import *
from functools import partial

def game_end(game_state_panel, human, computer): 
    """Create the ending game panel. 
    
    This function will create and shows the ending game panel, which will 
    contain a label stating that the game has ended and who the winner 
    was based on which player had the higher score, if it was a tie.
    
    Args: 
        game_state_panel: Paned window that contains information about 
            the game. 
        human: HumanPlayer object representing human player 
        computer: ComputerPlayer object representing the computer player. 
    
    """
    
    game_state_panel.destroy()

    end_panel = PanedWindow(bg= "#F8FFA6")
    end_panel.pack(fill= BOTH, expand=1)
    
    winner = Label(end_panel ,font= ('Comic Sans MS' , 70), bg="#F8FFA6", justify='center')
    
    if human.score > computer.score: 
        winner.configure(text= f'Game End.\n{human.name} Wins!')
    elif human.score < computer.score: 
        winner.configure(text= f'Game End.\n{computer.name} Wins!')
    else: 
        winner.configure(text= 'Game End.\nIts a Tie!')
        
    winner.pack()
    
def update(game_state_panel, computer, human, game_state, 
           window, deck, human_info, computer_info, card_panel): 
    """Updates player information.
    
    This function will update player information lables, specfically
    the human_info and computer_info labels; these labels contain 
    player name, score, and for the computer player, the number of 
    cards in the hand. This function will aslo delete and re add 
    the buttons representing the human player hand due to new cards 
    being added/deleted from the hand during the game. 
    
    Args: 
        game_state_panel: Paned window that contains information about 
            the game. 
        computer: ComputerPlayer object representing the computer player. 
        human: HumanPlayer object representing human player 
        game_state: Text documenting the moves in the game. 
        window: root window
        deck: list of cards represented as tuples (rank, suit)
        human_info: Label that states human player name and score 
        computer_info : Label that states computer player name, score, and 
            number of cards in the hand. 
        card_panel: Paned window containing buttons representing human hand. 
        
    Sources : 
        
        JackJack4, et al. “How to Pass Arguments to a Button Command in Tkinter?” Stack Overflow,
        1 Sept. 1959, https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter. 

            I used this stack overflow forum to help me figure out how to input multiple arguments into the command
            arguement for the buttons with the use of the partial() method. 
    """
    
    human_info.configure(text= ('Player ' + human.name + '\nScore: ' + str(human.score)))
    computer_info.configure(text= ('Player ' + computer.name + '\nScore: ' 
                                   + str(computer.score) + '\nNum. of Cards: ' + str(len(computer.hand))))

    for widgets in card_panel.winfo_children():
        widgets.destroy()
    
    for card in human.hand:
        card_button = Button( card_panel, text =(card[0], card[1]), font =('Comic Sans MS' , 15),
            command= partial(play,card[0], human, computer, game_state, window, deck, 
                             game_state_panel,human_info, computer_info, card_panel))
        card_button.pack(side=LEFT)
    
    window.mainloop()
        
def play(human_req_rank, human, computer, game_state, window,
         deck, game_state_panel,human_info, computer_info, card_panel): 
    """Plays game. 
    
    This function runs the game in the order it should be played in,
    while inserting game moves into the game_state object. 
    
    Args: 
        human_req_rank: string containing requested rank from 
            human player that is obtained when a button is clicked on.
        human: HumanPlayer object representing human player 
        computer: ComputerPlayer object representing the computer player. 
        game_state: Text documenting the moves in the game. 
        window: root window
        deck: list of cards represented as tuples (rank, suit)
        game_state_panel: Paned window that contains information about 
            the game. 
        human_info: Label that states human player name and score 
        computer_info : Label that states computer player name, score, and 
            number of cards in the hand. 
        card_panel: Paned window containing buttons representing human hand. 
        
    """
    
    while go_fish_with_GUI.end_game(human, computer, deck) == False:
         
        game_state.insert(END, (
            f'\n{human.name} requests {human_req_rank} from {computer.name}.\n\n🐟-------------🐟\n'))
        
        if computer.check_hand(human, human_req_rank, deck):
            
            game_state.insert(END , (f'\n{computer.name} has {human_req_rank}!\n'))
        else: 
    
            game_state.insert(END , (f"\nSorry! {computer.name} had no {human_req_rank}s! Go Fish!\n"))
        
        game_state.insert(END , ("\n🐟-------------🐟\n"))
           
        if human.has_book(): 
            game_state.insert(END , (
                f'\n{human.name} has a book!One point is added to their score.\n\n🐟-------------🐟\n'))
  
        computer_req_rank = computer.request_card()   
        
        game_state.insert(END , (
            f'\n{computer.name} requests {computer_req_rank} from {human.name}.\n\n🐟-------------🐟\n'))
        
        if human.check_hand(computer, computer_req_rank, deck):
            game_state.insert(END , (f'\n{human.name} has {computer_req_rank}!\n'))
        else: 
            game_state.insert(END , (f"\nSorry! {human.name} had no {computer_req_rank}s! Go Fish!\n"))
        
        game_state.insert(END , ("\n🐟-------------🐟\n"))

        if computer.has_book(): 
            game_state.insert(END , (
                f'\n{computer.name} has a book!One point is added to their score.\n\n🐟-------------🐟\n'))

        game_state.insert(END, f'\n{human.name}, what rank would you like to request?\n\n🐟-------------🐟\n')

    
        update(game_state_panel, computer, human, game_state, window, deck, human_info, computer_info, card_panel)
        
        window.mainloop()

    game_end(game_state_panel, human, computer)
        
def create_game_panel(window, start_panel, human, computer, deck): 
    """Creates game panel.
    
    This function creates and shows the game panel and everything 
    it contains, including the human_panel(panel containing all 
    information about the human player, including buttons representing player 
    hand),the computer_panel(panel containing all information about the
    computer player), and game_state_panel(contains information about the 
    moves played during the game). 
    
    Args: 
        window: root window
        start_panel: Paned window that contains welcome labels and begin button
        human: HumanPlayer object representing human player 
        computer: ComputerPlayer object representing the computer player. 
        deck: list of cards represented as tuples (rank, suit)
    
    Sources: 
        Paned Windows - Python Tkinter Gui Tutorial #48 - YouTube. https://www.youtube.com/watch?v=9Hyltpk2tSM. : 
            
            I ended up using his technique for adding the panels onto the actual window. The set up of the code
            is simiflar but modified to fit how I wanted to set up the game. 
        
        JackJack4, et al. “How to Pass Arguments to a Button Command in Tkinter?” Stack Overflow,
        1 Sept. 1959, https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter. 

            I used this stack overflow forum to help me figure out how to input multiple arguments into the command
            arguement for the buttons with the use of the partial() method. 
    
    """

    start_panel.pack_forget()
   
    game_state_panel = PanedWindow()
    game_state_panel.pack(fill= BOTH, expand=1)
    
    game_state = Text(game_state_panel,font =('Comic Sans MS' , 15))
    game_state_panel.add(game_state)
    
    game_state.insert(END, "Game Start!\n")
    game_state.insert(END, f'\n{human.name}, what rank would you like to request?\n')
     
    computer_panel = PanedWindow( game_state_panel, bg= "#F8FFA6", orient= 'vertical')
    game_state_panel.add(computer_panel)

    computer_info = Label(game_state_panel, justify= "left", 
                        text= ('Player ' + computer.name + '\nScore: ' + str(computer.score)+ 
                               '\nNum. of Cards: ' + str(len(computer.hand))), 
                        font= ('Comic Sans MS' , 30 ))
    computer_panel.add(computer_info)
  
    human_panel = PanedWindow( computer_panel,   bg= "white" , orient= 'vertical')
    computer_panel.add(human_panel)
    
    human_info = Label(computer_panel , bg= "#F8FFA6", 
                        text= ('Player ' + human.name + '\nScore: ' + str(human.score)),
                        font = ('Comic Sans MS' , 30 ))
    human_panel.add(human_info)
    
    card_panel = PanedWindow(human_info, bg= "#F8FFA6", orient='vertical')
    card_panel.pack(side= BOTTOM)
    
    for card in human.hand:
        card_button = Button( card_panel, text =(card[0], card[1]), font =('Comic Sans MS' , 15),
            command= partial(play,card[0], human, computer, game_state, window, deck, game_state_panel,human_info, computer_info, card_panel))
        card_button.pack(side=LEFT)
    
    window.mainloop()

def main(human , computer, deck):
    """Main function. 
    
    This function creates the root window, along with the 
    start_panel. The start_panel includes 2 labels and a button; 
    one label contains the name of the game (Go Fish) and another 
    welcomes the player. The button will be used to indicate 
    that the player wishes to start the game, which will create 
    the those repsective panels. 
    
    Args: 
        human: HumanPlayer object representing human player 
        computer: ComputerPlayer object representing the computer player. 
        deck: list of cards represented as tuples (rank, suit)  
      
    """

    window = Tk()
    window.title("Go Fish")
    window.geometry("800x600")
     

    start_panel= PanedWindow(bg= "#F8FFA6")
    start_panel.pack(fill = BOTH, expand =1)

    welcome = Label(start_panel , text = '🐟Go Fish🐟' , font= ('Comic Sans MS' , 70), bg="#F8FFA6", justify='center')

    begin_lbl = Label(start_panel ,
                    text = 'Would you like to begin the game? ',  
                    font= ('Comic Sans MS' , 40), bg="#F8FFA6", justify= 'center') 
    
    start = Button(start_panel, justify= 'center', text= "Start" , bd= 0 ,
                   font = ('Comic Sans MS' , 30 ),
                   command = partial(create_game_panel,window, start_panel, human, computer, deck))

    welcome.pack()
    begin_lbl.pack()
    start.pack()

    window.mainloop()
    
    
    
    
        



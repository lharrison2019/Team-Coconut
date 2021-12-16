"""A module for playing Go Fish.

Attributes: 
    ranks: list containing string values representing different card ranks 
    suits: list containing string values representing different card suits
"""

from random import *
from argparse import ArgumentParser
import sys
from time import sleep 

ranks = ['2', '3', '4' , '5' ,'6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['♣️', '♥', '♦', '♠']

def make_deck():  
    """Creates deck.
    
    This function will create a list of cards, or a deck, that will contain 52 tuples
    representing these cards. The cards are formated as (rank, suit)
    
    Returns: 
        deck: list of tuples representing cards, formated as (rank, suit)
    """
    deck = []
    for rank in ranks: 
        for suit in suits: 
              deck.append((rank, suit))
    shuffle(deck)
    return deck

def deal(num_of_cards, deck): 
    """Deals player hands from Deck. 
    
    This function will take a specified number of cards from the deck 
    and returns those cards to a player.  

    Args: 
        num_of_cards: int representing the amount of cards that 
            will be taken from the deck and returns to the player. 
        deck: list containing cards representing a deck
        
    Returns: 
        hand: list of cards that will be returned to the player. 

    """
    hand = []
    for i in range(num_of_cards):
        card = randint(0, len(deck)-1)
        hand.append(deck.pop(card))
    
    return hand            

def end_game(player_one, player_two, deck): 
    """Determines if game will end.
    
    This function will determine if the game will end. There are two instances
    where a go fish came comes to an end: one of the players has no cards 
    in their hand or there are no cards in the deck. This function will check 
    for both and will return True is the game has come to an end. 
    
    Args: 
        player_one: Player object represeting the first player 
        player_two: Player object represeting the second player
        deck: list containing cards representing a deck
        
    Returns: 
        boolean: true if either play has no cards in their hand or 
            deck doesnt contain any cards, false if not. 
    
    """
    if len(deck) == 0: 
        return True
    elif len(player_one.hand) == 0:
        return True
    elif len(player_two.hand) == 0 :
        return True
    return False
    
class Player: 
    """Parent Class representing a player. 
    
    Attributes: 
        name: string representing name of player 
        hand: list of cards representing current hand of the player 
        score: int representing the players score.

    """
    def __init__(self, name, deck): 
        self.name = name
        self.hand = deal(7,deck) 
        self.hand.sort()
        self.score = 0 
          
    def print_board(self,other):
        """Prints cards. 
        
        Prints the cards in player's hand.
        
        Args: 
            other: Player object representing other player 
        
        Side effects: 
            prints out players hand.
        """
        
        print('Your Hand: ')
        for card in self.hand: 
           
            print(f'| {card[0]}{card[1]} |' ,end= "") 
        
        print(f'\n\nScore: {self.name} = {self.score} ||| {other.name} = {other.score}')
        print('\n🐟-------------🐟')
        
    def check_hand(self, other, req_rank, deck): 
        """Checks hand for requested rank
        
        This method will check this player's(self) hand for a requested rank from 
        the other player(other). If the rank exists in this players hand, the method 
        will remove all cards containing the same rank requested and add them to the 
        other player's hand and this method will return true. If no cards are found 
        with the same rank, this method will return false.
        
        Args: 
            other: object representing other player 
            req_rank: string containing rank that is being requested by other player
            deck: list of tuples representing cards, formated as (rank, suit)
        
        Side effects: 
            If applicable, this method will add cards to other.hand and will remove 
            cards from self.hand. 
        """
        
        is_rank  = [card[0] == req_rank for card in self.hand ]
        cards_given  = []
    
        for i in range(len(is_rank)-1): 
            if is_rank[i]: 
                card = self.hand.pop(i)
                cards_given.append(card)
        sleep(1)
        if len(cards_given) == 0 : 
            print(f"\nSorry! {self.name} had no {req_rank}s! Go Fish!\n","🐟-------------🐟")
            self.draw(deck)
        else: 
            print(f'\n {self.name} has {req_rank}!\n🐟-------------🐟')
            other.hand.extend(cards_given)
            other.hand.sort()
              
    def has_book(self): 
        """Checks for books. 
    
        In Go Fish, a book is a set of 4 cards containing the same rank.
        When a player has a book in their hand, this function will remove
        those cards from the player's(self) hand and add a single point 
        to the player's score. This can only happen once per turn. 
        
        Returns:
            boolean: true if the player's hand contains a book, false otherwise 
            
        Side effects: 
            Will remove cards from self.hand and add to self.score if applicable 
        """
        
        for rank in ranks: 
            counter = 0
            
            for card in self.hand: 
                if card[0] == rank:
                    counter+=1 

            if counter == 4: 
                new_hand = [card for card in self.hand if card[0]!= rank]
                self.hand = new_hand
                self.score += 1
                print(f'\n{self.name} has a book! One point is added to their score.\n',
                      '\n🐟-------------🐟\n')            
            
    def draw(self, deck):
        """Draws one card. 
        
        This method will draw one randomly selected card from the deck 
        using the deal() function and add it to the player's hand. 
        
        Args: 
            deck: list of tuples representing cards, formated as (rank, suit)
        
        Side effects : 
            adds one card to the player's hand(self.hand)
        """
        self.hand.extend(deal(1, deck))
                  
class HumanPlayer(Player): 
    """Child Class of Player Class representing the human player. 
    
    Attributes: 
        name: string representing name of player 
        hand: list of cards representing current hand of the player 
        score: int representing the players score.

    """
    super
    
    def request_card(self, other, deck): 
        """Requests a card. 
        
        This method will ask the player for what rank they request and 
        will use the check_hand method to see if the other player contains 
        card(s) in their hand.
        
        Args: 
            other: other player in the game
            deck: list of tuples representing cards, formated as (rank, suit)
        Side effects: 
            prints on the board asking for the requested rank from the user. 
        """
        
        self.print_board(other)
        while True: 
            req_rank = input(f"\nWhat rank do you request from {other.name}?\n")
            print('🐟-------------🐟')
            
            if str(req_rank) not in ranks: 
                print("\nInvalid rank. Try Again!\n")
            else: 
                break
        
        sleep(1)
        other.check_hand(self, req_rank, deck)
            
class ComputerPlayer(Player): 
    """Child Class of Player Class representing the computer player. 
    
    Attributes: ß
        name: string representing name of player, with a default of
            "Computer"
        hand: list of cards representing current hand of the player 
        score: int representing the players score.

    """
    super
    
    def request_card(self, other, deck):
        """Requests a card. 
        
        This method will request a card in one of two ways. First, the method
        will check for multiple cards with the same rank in the hand. This method 
        will do this my creating another list that contains tuples representing 
        the number of times a rank appears within the hand and the rank itself, or 
        (count(rank), rank). The list will only include ranks that have a count 
        higher than 1. If there are at least three sets of ranks that have a count 
        higher than 1, a rank will be randomly selected from that list. Otherwise, 
        a rank will be randomly selected from the whole hand (self.hand). 
        
        Returns: 
            
            other: other player in the game
            deck: list of cards representing the deck.
            
        Side effects: 
            prints on the board asking for the requested rank from the user. 
        """
        
        ranks_in_hand = [card[0]for card in self.hand]
        
        count_rank = list(set([(ranks_in_hand.count(rank), rank)for rank in 
                               ranks_in_hand if ranks_in_hand.count(rank)>1]))
        
        if len(count_rank) < 3: 
            req_card = self.hand[randint(0,len(self.hand)-1)]
            req_rank= req_card[0]
    
        else :
            req_card = count_rank.pop(randint(0,len(count_rank)-1))
            req_rank= req_card[1]
        
        print(f'\n{self.name} asks {other.name} if they have any {req_rank}s.\n')
        print('🐟-------------🐟')
        sleep(1)
        
        other.check_hand(self, req_rank, deck)
               
def main(human_name, computer_name): 
    """Runs the game.
    
    The main function will create the deck and the 
    two instances of the HumanPlayer and the ComputerPlayer.
    It will then proceed to run the game by calling on the 
    request_card() and has_book() for each player. 
    
    Args: 
        human_name: string containing the chosen name of the 
            HumanPlayer.
        computer_name:string contianing the chosen name of the 
            ComputerPlayer. 
    
    Side effects: 
        Creates instances of the HumanPlayer and ComputerPlayer 
        class. 
    
    """
    while True:
        play= input("Would you like to play a game of 🐟Go Fish🐟?")
        
        if play.lower() != 'yes': 
            break
        
        deck = make_deck()
        
        human_player =  HumanPlayer(human_name, deck)
        computer_player =  ComputerPlayer(computer_name,deck)

        print('\n\nWelcome to Go Fish!\n\n🐟-------------🐟\n')
        
        while end_game(human_player,computer_player, deck) == False:
            human_player.request_card(computer_player, deck)
            human_player.has_book()
            computer_player.request_card(human_player, deck)
            computer_player.has_book()
        
        if human_player.score > computer_player.score: 
            print(f'\nGame End! {human_player.name} Wins!\n')
        elif human_player.score < computer_player.score: 
            print(f'\nGame End! {computer_player.name} Wins!\n')
        else: 
            print('\nGame End!Its a tie!\n')
        
    
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument:
        - player_name: string representing name of human player

    
    Also allow one optional arguments:
        -c, --computer_name: string representing name of computer player
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("player_name", help="name of the human player")
    parser.add_argument("-c", "--computer_name", type=str, default="Computer",
                        help="Optional: give a name to the computer player")
    
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.player_name, args.computer_name)

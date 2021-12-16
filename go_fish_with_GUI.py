"""A module for playing Go Fish using a GUI.

Attributes: 
    ranks: list containing string values representing different card ranks 
    suits: list containing string values representing different card suits
"""

from random import *
from argparse import ArgumentParser
import sys
import GUI

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
        deck: list of tuples representing cards, formated as (rank, suit)
        
    Returns: 
        cards: list of cards that will be returned to the player. 

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
        deck: list of tuples representing cards, formated as (rank, suit)
        
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
        self.hand = deal(7, deck) 
        self.hand.sort()
        self.score = 0 
                        
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
        
        Returns: 
            boolean: true if the rank is found in player(self) hand, false if not.
        
        Side effects: 
            If applicable, this method will add cards to other.hand and will remove 
            cards from self.hand. 
        
        """
        is_rank  = [card[0] == req_rank for card in self.hand ]
        cards_returned  = []
        
        for i in range(len(is_rank)-1): 
            if is_rank[i]: 
                card = self.hand.pop(i)
                cards_returned.append(card)
        
        if len(cards_returned) == 0 : 
            self.hand.extend(deal(1, deck))
            self.hand.sort()
            return False
        
        other.hand.extend(cards_returned)
        other.hand.sort()
        return True
            
    def has_book(self): 
        """Checks for books. 
        
        In Go Fish, a book is a set of 4 cards containing the same rank.
        When a player has a book in their hand, this function will remove
        those cards from the player's(self) hand and add a single point 
        to the player's score. This can only happen once per turn. 
        
        Returns
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
                return True
        return False
                                 
class HumanPlayer(Player): 
    """Child Class of Player Class representing the human player. 
    
    Attributes: 
        name: string representing name of player 
        hand: list of cards representing current hand of the player 
        score: int representing the players score.

    """
    super
              
class ComputerPlayer(Player): 
    """Child Class of Player Class representing the computer player. 
    
    Attributes: ß
        name: string representing name of player, with a default of
            "Computer"
        hand: list of cards representing current hand of the player 
        score: int representing the players score.

    """
    super

    def request_card(self):
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
            req_rank: a string containing the rank the computer player requests. 

        """
        ranks_in_hand = [card[0]for card in self.hand]
        
        count_rank = list(set([(ranks_in_hand.count(rank), rank)for rank in 
                               ranks_in_hand if ranks_in_hand.count(rank)>1]))
        
        if len(count_rank) < 3: 
            req_card = self.hand[randint(0,len(self.hand)-1)]
            return req_card[0]
        else :
            req_card = count_rank.pop(randint(0,len(count_rank)-1))
            return req_card[1]
               
def main(human_name, computer_name): 
    """Runs the game.
    
    The main function will create the deck and the 
    two instances of the HumanPlayer and the ComputerPlayer. 
    The deck and objects will be passed to the main function 
    in GUI.py, which will run the game. 
    
    Args: 
        human_name: string containing the chosen name of the 
            HumanPlayer.
        computer_name:string contianing the chosen name of the 
            ComputerPlayer. 
    
    Side effects: 
        Creates instances of the HumanPlayer and ComputerPlayer 
        class. 
    
    """
    deck = make_deck()
    
    human_player =  HumanPlayer(human_name, deck)
    computer_player =  ComputerPlayer(computer_name, deck)
    
    GUI.main(human_player, computer_player , deck)

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

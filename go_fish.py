import random


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
suits = ['hearts', 'clubs', 'aces', 'spades']
deck = []

def make_deck():
    for num in numbers: 
        for suit in suits: 
              deck.append([num, suit])
              
    random.shuffle(deck)
    return deck

def deal(num_of_cards): 
    """Deals player hands from Deck. 
    
    This function will take a specified number of cards from the deck 
    and returns those cards to a player.  

    Args: 
        num_of_cards: int representing the amount of cards that 
        will be taken from the deck and returns to the player. 
        
    Returns: 
        hand: list of cards that will be returned to the player. 

    """
    hand = []
    for i in range(num_of_cards):
        card = random.randint(0, len(deck))
        hand.append(deck.pop(card))
    
    return hand

def pair_count(hand):
    score = 0 
    for deck in hand:
        if hand.count(hand) > 1:

            deck.remove(hand)
            deck.remove(hand)
            score += 1 

class Player: 
    """Parent Class representing a player. 
    
    Attributes: 
        name: string representing name of player 
        hand: list of cards representing current hand of the player 
        score: int representing the players score.

    """
    
    def __init__(self, name, hand, score): 
        self.name = name
        self.hand = deal(7) 
        self.score = 0 
        
    def get_score(self): 
        """Returns score. 
        
        Returns: 
            self.score: int representing the players score.
            
        """
        return self.score
    
    def get_hand(self): 
        """Returns hand. 
        
        Returns: 
            self.hand: list of cards representing current hand of the player 
        
        """
        return self.hand 
    
    

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
    
    Attributes: 
        name: string representing name of player, with a default of
            "Computer"
        hand: list of cards representing current hand of the player 
        score: int representing the players score.

    """
   
    super
    
    def __init__(self, hand, score , name = "Computer"): 
        self.name = name
        self.hand = deal(7) 
        self.score = 0 
    
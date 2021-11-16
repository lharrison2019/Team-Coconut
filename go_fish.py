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


def deal_hand(): 
    hand = []
    
    for i in range(7):
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
    
    def __init__(self, name, hand, score): 
        self.name = name
        self.hand = deal_hand() 
        self.score = 0 
        
    def get_score(self): 
        return self.score
    
    def get_hand(self): 
        return self.hand 
    
    

class HumanPlayer(Player): 
    
    super
    
    
class ComputerPlayer(Player): 
   
    super
    
    def __init__(self, hand, score , name = "Computer"): 
        self.name = name
        self.hand = deal_hand() 
        self.score = 0 
    
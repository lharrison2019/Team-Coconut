from _typeshed import ReadOnlyBuffer


import random

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
suit = ['hearts', 'clubs', 'aces', 'spades']
player1 = list()
player1_hand = 0 

player2 = list()
player2_hand = 0

def player_cards():
    cards = []
    cards.append([numbers, suit])
    random.shuffle(cards)
    return cards
    

    for i in range(5):
        deck  = cards.pop()
        player1.append(deck)

    for i in range(5):
        deck = cards.pop()
        player2.append(deck)

def pair_count(hand):
    score = 0 
    for deck in hand:
        if hand.count(hand) > 1:

            deck.remove(hand)
            deck.remove(hand)
            score += 1 

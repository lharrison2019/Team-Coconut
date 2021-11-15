from _typeshed import ReadOnlyBuffer


import random

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
suit = ['hearts', 'clubs', 'aces', 'spades']

def player_cards():
    cards = []
    cards.append([numbers, suit])
    random.shuffle(cards)
    return cards
    
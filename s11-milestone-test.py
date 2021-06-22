'''
Blackjack Game Mileston Project
Coded by Thoughtless Labs

'''

# Player - Track and use money and cards

# Computer Dealer - Deal cards and play hand


# Create players
# Create a deck
# Deal Cards
# Check for win
# Check for 21 then
# Tell player cards
# Decide on hit, stay
# Dealer plays until bust or rules (must hit on soft 17, etc.)
# End loop and restart

# Basic logic
# Game loop
# Player loop
# Dealer loop

import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks= ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven': 7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():
    
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player():
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def add_cards(self, new_cards):
        self.all_cards.append(new_cards)

    def stand():
        pass

#create a new deck
game_deck = Deck()

#shuffle the deck
game_deck.shuffle()

#create player and dealer
player = Player(input('What is your name? '))
dealer = Player('Dealer')

game_on = True
while game_on:
    
    if len(game_deck.all_cards) < 5:
        #create a new deck
        game_deck = Deck()

        #shuffle the deck
        game_deck.shuffle()

    

    #Player's Turn
    player_turn = True
    while player_turn:
        print(f"{player.name}'s turn")
        break

    game_on = False

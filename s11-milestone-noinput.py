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
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven': 7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

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

    def __string__(self):
        pass

#create player and dealer
player = Player(input('What is your name? '))
dealer = Player('Dealer')

#create a new deck
game_deck = Deck()

#shuffle the deck
game_deck.shuffle()

game_on = True
while game_on:
    player_score = 0
    dealer_score = 0

    for i in range(2):
        player.add_cards(game_deck.deal_one())
        dealer.add_cards(game_deck.deal_one())

    for i in range(0,len(player.all_cards)):
        player_score += player.all_cards[i].value

    for i in range(0,len(dealer.all_cards)):
        dealer_score += dealer.all_cards[i].value 

    if player_score == 21:
        print(f"{player.name} has Blackjack!")
        break
    elif player_score > 21:
        print(f"{player.name} has BUSTED!")
        player_score = 0
        break
    elif player_score >=17:
        print(f"{player.name} stays with {player_score}")
        break
    else:
        player.add_cards(game_deck.deal_one())
        continue
    
    print(f"Dealer has {dealer_score}")
    if dealer_score == 21:
        print(f"Dealer has Blackjack! {player.name} loses.")
        break
    elif dealer_score > 21:
        print(f"Dealer has BUSTED!")
        dealer_score = 0
        break
    elif dealer_score >=17:
        print(f"Dealer stays with {dealer_score}")
        break
    else:
        player.add_cards(game_deck.deal_one())
        continue

if player_score > dealer_score:
    print(f"{player.name} wins")
else:
    print(f"Dealer wins")

game_on = False

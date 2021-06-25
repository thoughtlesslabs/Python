'''
Blackjack Game Mileston Project
Coded by Thoughtless Labs

'''
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

def count_score(player_hand):
    score = 0
    for i in range(0,len(player_hand.all_cards)):
        if player_hand.all_cards[i].rank == 'Ace':
            if (score + player_hand.all_cards[i].value) > 21:
                player_hand.all_cards[i].value = 1
        score = score + player_hand.all_cards[i].value
    return score,player_hand


#create player and dealer
player = Player('John')#input('What is your name? '))
dealer = Player('Dealer')

#create a new deck
game_deck = Deck()

#shuffle the deck
game_deck.shuffle()

game_on = True
while game_on:

    for i in range(2):
        player.add_cards(game_deck.deal_one())
        dealer.add_cards(game_deck.deal_one())

    player_score = count_score(player)
    dealer_score = count_score(dealer)

    if player_score[0] == 21:
        print(f"{player_score[1].name} has Blackjack!")
        break
    elif dealer_score[0] == 21:
        print(f"{dealer_score[1].name} has Blackjack!")
        break

    player_turn = True

    while player_turn:
        player_score = count_score(player)
        print(f"{player.name} has a score of {player_score[0]}")
        if player_score[0] > 21:
            print(f"{player.name} has BUSTED!")
            dealer_turn = False
            break
        elif player_score[0] >=17:
            print(f"{player.name} stays with a score of {player_score[0]}")
            dealer_turn = True
            break
        elif player_score[0] < 17:
            player.add_cards(game_deck.deal_one())
            print(f"{player.name} gets a {player.all_cards[-1]}")
            continue
        else:
            dealer_turn = True
            break
            

    while dealer_turn:
        dealer_score = count_score(dealer)
        print(f"{dealer.name} has a score of {dealer_score[0]}")
        if dealer_score[0] > 21:
            print(f"Dealer has BUSTED!")
            break
        elif dealer_score[0] >=17:
            print(f"Dealer stays with a score of {dealer_score[0]}")
            break
        elif dealer_score[0] < 17:
            dealer.add_cards(game_deck.deal_one())
            print(f"{dealer.name} gets a {dealer.all_cards[-1]}")
            continue
        else:
            break
    
    game_on=False

if player_score[0] > 21:
    print("Dealer Wins")
elif dealer_score[0] > 21:
    print(f"{player.name} wins!")
elif player_score[0] == dealer_score[0]:
    print("It's a tie!")
elif player_score[0] > dealer_score[0]:
    print(f"{player.name} wins")
else:
    print(f"Dealer wins")
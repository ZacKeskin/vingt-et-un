##################################################
#   Import packages
from itertools import product, chain
from random import randint

##################################################
#   Define simulation parameters

N = 6                               # Number of 52-card packs in deck
N_PLAYERS = 1                       # Number of players (other than dealer)
ROUNDS_BEFORE_RESHUFFLE = 5         # Number of hands played before deck reset to full
SOFT_17_STAND = True                # Boolean if dealer must stand on 'soft' 17 (contains ace)

##################################################
#   Define Classes

class Card():
    def __init__(self,suit,number,packid,value,c_id):
        self.suit = suit
        self.number = number
        self.pack = packid
        self.value = value
        self.c_id = c_id


class Deck():
    def __init__(self):
        self.count = N * 52
        self.suits = ['Clubs','Diamonds','Hearts','Spades']
        self.cards = [Card(suit,name,packid,value,(i+j+k)) for i, suit in enumerate(self.suits)                                                 
                                                 for j, (name,value) in enumerate({'2':2,'3':3,'4':4,'5':5,'6':6,
                                                                    '7':7,'8':8,'9':9,'10':10,
                                                                    'Jack':10,'Queen':10,'King':10,'Ace':11}.items())
                                                 for k,packid in enumerate(range(N))]     
                                                                                               
    def draw_cards(self,n_cards):
        # Select cards at random and move from deck to hands
        cid = randint(0, self.count)
        # Update number of cards in deck
        self.count -= n_cards
        # Deal n cards at random from deck
        return [self.cards.pop(randint(0, self.count - i)) for i, card in enumerate(range(n_cards))]  
        

class Player():
    def __init__(self):
        self.hand =[]
        
class Dealer():
    def __init__(self):
        self.hand = []




class Game():
    def __init__(self):
        self.deck = Deck()
        self.players = [Player() for player in range(N_PLAYERS)]
        self.dealer = Dealer()
    
    def deal_hands(self):
        for player in self.players:
            player.hand.extend(self.deck.draw_cards(2))
        self.dealer.hand.extend(self.deck.draw_cards(2))



if __name__ == "__main__":

    newGame = Game()

    newGame.deal_hands()

    
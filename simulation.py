##################################################
#   Import packages
from random import randint


##################################################
#   Define simulation parameters

N = 6                                # Number of 52-card packs in deck
N_PLAYERS = 5                        # Number of players (other than dealer)
ROUNDS_BEFORE_RESHUFFLE = 10         # Number of hands played before deck reset to full
SOFT_17_HIT = True                   # Boolean if dealer must hit on 'soft' 17 (contains ace)
N_SIMULATIONS = 1                    # Number of games to simulate

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
        self.cards = [Card(suit,name,packid,value,(str(i)+'_'+str(j)+'_'+str(k))) for i, suit in enumerate(self.suits)                                                 
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
    def hit(self,game): 
        self.hand.extend(game.deck.draw_cards(1))
        self.total = sum(card.value for card in self.hand)

class Dealer():
    def __init__(self):
        self.hand = []
    def hit(self,game):
        self.hand.extend(game.deck.draw_cards(1))
        self.total = sum(card.value for card in self.hand)
    def play(self,game):
        while True:            
            if self.total > 21:
                if any(card.number == "Ace" for card in self.hand):
                    self.hand[0].value -= 10   # Shouldn't strictly matter which card we drop by 10             
                    self.hit(game)                    
                else:                    
                    break # Dealer Bust    
            elif self.total == 17 and any(card.number == "Ace" for card in self.hand):
                if SOFT_17_HIT == True:
                    self.hit(game)                                              
            elif self.total < 17:                            
                self.hit(game)
            else:            
                break # Dealer Stands



class Game():
    def __init__(self):
        self.deck = Deck()
        self.players = [Player() for player in range(N_PLAYERS)]
        self.dealer = Dealer()
    
    def deal_hands(self):
        for player in self.players:
            player.hand.extend(self.deck.draw_cards(2))
            player.total =  sum(card.value for card in player.hand)
        self.dealer.hand.extend(self.deck.draw_cards(2))
        self.dealer.total = sum(card.value for card in self.dealer.hand)

    def play_round(self):
        # Each player chooses to hit or stick at random
        for player in self.players:
            
            while player.total < 21:
                if randint(0,1) == 1:
                    player.hit(self)
                else:
                    break   # Player sticks

        # Dealer plays according to mandated rules
        self.dealer.play(self)

        print('Dealer Score:',self.dealer.total,'Player Scores:',[player.total for player in self.players])
        #print([('cid:',card.c_id, card.number, card.suit) for card in player.hand for player in self.players])
        
        # Reset Player and Dealer hands
        self.players = [Player() for player in range(N_PLAYERS)]
        self.dealer = Dealer()
        # Re-deal
        self.deal_hands()
        #self.scores = dict(


def run_simulation(n_rounds=1):
    newGame = Game()
    newGame.deal_hands()
    for round in range(n_rounds):
        print('Round:',round+1)
        newGame.play_round()
    print('Cards Remaining:',newGame.deck.count)

if __name__ == "__main__":
    
    for i in range(N_SIMULATIONS):
        run_simulation(n_rounds=ROUNDS_BEFORE_RESHUFFLE)
 
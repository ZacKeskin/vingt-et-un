from simulation import Deck
from nose.tools import assert_is, assert_in, assert_almost_equal, assert_raises


###########################################################################
###              Test Deck Initialisation
###########################################################################



# Use test generator to test the number of cards in an N-pack deck is as expected
def deck_count(N):
    deck = Deck(N)
    assert_is(deck.count,N*52)

def test_generator_count():
    for N in range(0,5):
        yield deck_count, N
    
# Test that the sum of a dealt pack of cards is as expected
def test_value():
    deck = Deck(1)
    assert sum(card.value for card in deck.cards) == 380




###########################################################################
###              Test Draw Cards Method
###########################################################################

# Test the sum of the cards is reduced by expected number on draw method
def draw_cards(N):
    deck = Deck(2)
    original_count = deck.count
    withdrawn = deck.draw_cards(N)
    assert deck.count == original_count - N

def test_generator_draw():
    for N in range(0,40,5):
        yield draw_cards, N



## Possible Tests:
    # Test Exception is handled when deck drops below minimum cards
    # Test odds of
    # Test multiple players get right number of cards
    # Test hit and stick return correct numbers of cards
    # Test Deck reset at end of hand
    # Test 

from enum import Enum

class Colors(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3

class Cards(Enum):
    SKIP = 10
    REVERSE = 11
    DRAW2 = 12

class Wilds(Enum):
    WILD = 0
    DRAW4 = 1

def build_card_counts():
    # Define the composition of an Uno deck.
    CARD_COUNTS = {"color":{}
                   "wild": {}
                  }
    # Color cards
    for c in Colors:
        # 2 of each 
        CARD_COUNTS["color"][c.value] = {i:2 for i in range(13)}
        # (except zeros; only 1 of each zero)
        CARD_COUNTS["color"][c.value][0] = 1
        
    # Wild cards (wild, plus4). 4 of each
    for w in Wilds:
        CARD_COUNTS["wild"][w.value] = 4
    return CARD_COUNTS    

DECK_CARD_COUNTS = build_card_counts()

def build_deck(n_decks=1):
    cc = uu.DECK_CARD_COUNTS
    deck = []
    for color, counts in cc["color"].items():
        for value, count in counts.items():
            for _ in range(count):
                deck.append((False,color,value)) 
    return deck*n_decks

    


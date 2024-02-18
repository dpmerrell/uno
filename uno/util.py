
from enum import Enum

class Colors(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3

class Cards(Enum):
    SKIP = 10
    REVERSE = 11
    PLUS2 = 12

class Wilds(Enum):
    WILD = 0
    PLUS4 = 1

def build_card_counts():
    # Define the composition of an Uno deck.
    CARD_COUNTS = {}
    # Color cards
    for c in Colors:
        # 2 of each 
        CARD_COUNTS[c.value] = {i:2 for i in range(13)}
        # (except zeros; only 1 of each zero)
        
    # Wild cards (wild, plus4). 4 of each
    for w in Wilds:
        CARD_COUNTS[w.value] = 4
    return CARD_COUNTS    

CARD_COUNTS = build_card_counts



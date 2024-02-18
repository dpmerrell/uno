"""

"""

import numpy as np

class UnoHand:
    
    def __init__(self):
        self.color_grid = np.zeros(13, 4, dtype=np.int8)
        self.wild_grid = np.zeros(2, dtype=np.int8)
        self.n_cards = 0

    """
    Card: 
        * color cards: (NUMBER, COLOR)
        * wild cards:  (IS_PLUSFOUR,)
    """
    def add_card(self, card):
        if len(card) == 2:
            self.color_grid[*card] += 1
        else:
            self.wild_grid[card[0]] += 1
        return


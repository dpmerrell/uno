"""

"""

import numpy as np

class UnoHand:
    
    def __init__(self):
        self.color_grid = np.zeros(4, 13 dtype=np.int8)
        self.wild_grid = np.zeros(2, dtype=np.int8)
        self.n_cards = 0


    """
    Card: (ISWILD, COLOR, VALUE)
        ISWILD: Bool
        COLOR: -1 (no assigned color); 0-3 (assigned color)
        VALUE: 
            when ISWILD: 0-1 (wild, draw4)
            otherwise: 0-12 (numbers, actions)
    """
    def add_card(self, card):
        if card[0]: # IS WILD
            self.wild_grid[card[2]] += 1
        else: # IS A COLOR CARD
            self.color_grid[card[1],card[2]] += 1
        self.n_cards += 1
        return


    def remove_card(self, card):
        if card[0]: # IS WILD 
            n_cards = self.wild_grid[card[2]]
            if n_cards > 0:
                self.wild_grid[card[1]] = n_cards - 1
                self.n_cards -= 1
            else:
                raise ValueError(f"Hand does not contain card {card}")
        else: # IS A COLOR CARD
            n_cards = self.color_grid[card[1],card[2]]
            if n_cards > 0:
                self.color_grid[card[1],card[2]] = n_cards - 1
                self.n_cards -= 1
            else:
                raise ValueError(f"Hand does not contain card {card}")

    #TODO
    def get_legal_moves(self, card):
        legal_moves = []

        if card[0]: # IS WILD
            # If it's a draw4, then ONLY a draw4 is legal
            if card[2] == 1:
                legal_moves += [(True,i,1) for i in range(3)]*self.wild_grid[1]
            else: # If it's a wild:
                # If it has NO assigned color, then
                # ANY card is legal
                if card[1] == -1:

                else:
                # If it has an assigned color,
                # then only cards of that color OR wilds are legal.
          
        else: # IS A COLOR CARD

        return legal_moves




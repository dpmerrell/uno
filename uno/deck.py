
from random import shuffle
import uno.util as uu


class UnoDeck:

    def __init__(self, n_decks=1):
        self.draw_pile = build_deck(n_decks=n_decks)
        shuffle(self.draw_pile)
        self.discard_pile = [self.draw_pile.pop()]

    def draw(self):
        # If the draw pile ran out of cards:
        if len(self.draw_pile) == 0:
            # Handle a corner case -- empty deck!
            if len(self.discard_pile) == 0:
                return None
            # If the deck isn't empty, just move the discard
            # pile into the draw pile and shuffle it
            # (except the top card)
            else:
                self.draw_pile = self.discard_pile[:-1]
                self.discard_pile = [self.discard_pile[-1]]
                shuffle(self.draw_pile)
        # Most of the time, we just pop from the draw pile
        return self.draw_pile.pop()

    def top_card(self):
        return self.discard_pile[-1]


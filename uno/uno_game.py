

class UnoGame:

    def __init__(self, players, deck, history=[]):
        self.players = players
        self.deck = deck
        self.cur_player = self.players[0]
        self.clockwise = True
        self.history = history


    def play_game(self, max_turns=10000):

        # Play until there's only one player left
        while len(self.players) > 1:

            # Player observes the game state
            # and submits an action to the game
            card = self.cur_player.choose_action(self)

            # Game validates player's action
            # (and throws an error if not valid);
            self.validate_action(card)

            # The game updates its state 
            self.update_state(card)

        return


    def validate_action(self, card):
        # verify that the player has the card

        # verify that the card is a legal move, 
        # given the deck's top card
        return


    def update_state(self, card):

        # Update deck
        # Update direction
        # Update players
        # Update cur_player
        # Update history



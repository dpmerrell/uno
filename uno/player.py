

class UnoPlayer:

    def __init__(self):
        self.hand = UnoHand()

    def choose_action(self, game):
        raise NotImplementedError("Need to implement `choose_action`")


class RandomPlayer(UnoPlayer):

    def __init__(self):
        pass

    def choose_action(self, game):
        pass


class SimplePolicyPlayer(UnoPlayer):
 
    def __init__(self):
        pass

    def choose_action(self, game):
        pass



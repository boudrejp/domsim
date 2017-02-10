__author__ = 'breppert'


from CardImpls.Helper import *

class Haggler(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Haggler"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        player.turn_info.add_money(2)

    def is_terminal(self):
        return True

    def card_goodness(self):
        return 6

    def economy(self):
        return 2

    def get_categories(self):
        return [Card.ECONOMY, Card.GAINER]


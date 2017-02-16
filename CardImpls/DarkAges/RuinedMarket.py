__author__ = 'breppert'


from Card import Card

from CardImpls.Helper import *

class RuinedMarket(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Ruined Market"

    def get_cost(self, reduction = 0):
        return max([0, 0 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.RUIN]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        player.turn_info.buys += 1

    def card_goodness(self):
        return -10

    def is_terminal(self):
        return True

    def get_categories(self):
        return [Card.JUNK]


__author__ = 'breppert'


from Card import Card

from CardImpls.Helper import *

class RuinedVillage(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Ruined Village"

    def get_cost(self, reduction = 0):
        return max([0, 0 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.RUIN]

    def play_card(self, game, player, opposing_player, play_type = None):
        pass

    def card_goodness(self):
        return -30

    def get_categories(self):
        return [Card.JUNK]


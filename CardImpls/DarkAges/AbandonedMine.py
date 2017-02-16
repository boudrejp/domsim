__author__ = 'breppert'


from Card import Card

from CardImpls.Helper import *

class AbandonedMine(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Abandoned Mine"

    def get_cost(self, reduction = 0):
        return max([0, 0 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.RUIN]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        player.turn_info.add_money(1)


    def is_terminal(self):
        return True

    def card_goodness(self):
        return -30

    def economy(self):
        return 1

    def get_categories(self):
        return [Card.JUNK, Card.ECONOMY]


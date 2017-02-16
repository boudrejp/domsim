__author__ = 'breppert'


from Card import Card

from CardImpls.Helper import *

class RuinedLibrary(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Ruined Library"

    def get_cost(self, reduction = 0):
        return max([0, 0 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.RUIN]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        for i in range(1):
            player.draw_card()

    def draws(self, hand = None):
        return 1

    def is_terminal(self):
        return True

    def card_goodness(self):
        return -10

    def get_categories(self):
        return [Card.JUNK]


__author__ = 'breppert'


from Card import Card

from CardImpls.Helper import *

class Monument(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Monument"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.ATTACK]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        player.turn_info.add_money(2)
        player.victory_chips += 1

    def is_terminal(self):
        return True

    def card_goodness(self):
        return 6

    def economy(self):
        return 2

    def get_categories(self):
        return [Card.TERMINAL_PAYLOAD_STACKING]


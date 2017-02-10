__author__ = 'breppert'


from CardImpls.Helper.util import *


class Oasis(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Oasis"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.draw_card()
        player.turn_info.add_money(1)
        discard_card_from_hand(player)


    def is_terminal(self):
        return False

    def card_goodness(self):
        return 4

    def is_cantrip(self):
        return True

    def get_categories(self):
        return [Card.ECONOMY]
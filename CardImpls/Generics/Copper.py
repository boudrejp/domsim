__author__ = 'breppert'

from Card import Card

class Copper(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Copper"

    def get_cost(self, reduction = 0):
        return max([0, 0 - reduction])

    def get_types(self):
        return [Card.TREASURE]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.add_money(1)

    def economy(self):
        return 1

    def card_goodness(self):
        return -12
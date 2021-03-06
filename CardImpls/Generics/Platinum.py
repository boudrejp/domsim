__author__ = 'breppert'

from Card import Card

class Platinum(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Platinum"

    def get_cost(self, reduction = 0):
        return max([0, 9 - reduction])

    def get_types(self):
        return [Card.TREASURE]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.add_money(5)

    def economy(self):
        return 5

    def card_goodness(self):
        return 8

    def get_categories(self):
        return [Card.ECONOMY]
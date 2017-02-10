__author__ = 'breppert'

from Card import Card

class Colony(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Colony"

    def get_cost(self, reduction = 0):
        return max([0, 11 - reduction])

    def get_types(self):
        return [Card.VICTORY]

    def get_victory_points(self, player, opposing_player):
        return 10

    def get_categories(self):
        return [Card.POINTS]
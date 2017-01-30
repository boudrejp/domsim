__author__ = 'breppert'

from Card import Card

class Estate(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Estate"

    def get_types(self):
        return [Card.VICTORY]

    def get_cost(self, reduction = 0):
        return max([0, 2 - reduction])

    def get_victory_points(self, player, opposing_player):
        return 1

    def get_categories(self):
        return [Card.POINTS]
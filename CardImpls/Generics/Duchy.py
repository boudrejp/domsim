__author__ = 'breppert'
from Card import Card

class Duchy(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Duchy"

    def get_types(self):
        return [Card.VICTORY]

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_victory_points(self, player, opposing_player):
        return 3

    def get_categories(self):
        return [Card.POINTS]
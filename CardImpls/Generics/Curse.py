__author__ = 'breppert'

from Card import Card

class Curse(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Curse"

    def get_types(self):
        return [Card.CURSE]

    def get_cost(self, reduction = 0):
        return max([0, 0 - reduction])

    def get_victory_points(self, player, opposing_player):
        return -1

    def get_categories(self):
        return [Card.JUNK]
__author__ = 'breppert'

from Card import Card

class Gardens(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Gardens"

    def get_types(self):
        return [Card.VICTORY]

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_victory_points(self, player, opposing_player):
        return int(len(player.get_all_cards()) / 10)



    def get_categories(self):
        return [Card.POINTS]
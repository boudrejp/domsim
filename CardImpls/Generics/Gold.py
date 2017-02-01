__author__ = 'breppert'

from Card import Card

class Gold(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Gold"

    def get_cost(self, reduction = 0):
        return max([0, 6 - reduction])

    def get_types(self):
        return [Card.TREASURE]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.add_money(3)

    def economy(self):
        return 3

    def card_goodness(self):
        return 5

    def get_categories(self):
        return [Card.ECONOMY]
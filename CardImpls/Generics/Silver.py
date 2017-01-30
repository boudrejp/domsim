__author__ = 'breppert'

from Card import Card

class Silver(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Silver"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.TREASURE]

    def play_card(self, game, player, opposing_player):
        player.turn_info.add_money(2)

    def economy(self):
        return 2

    def card_goodness(self):
        return 3

    def get_categories(self):
        return [Card.ECONOMY]
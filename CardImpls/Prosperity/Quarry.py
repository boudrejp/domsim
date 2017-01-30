__author__ = 'breppert'

from Card import Card

class Quarry(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Quarry"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.TREASURE]

    def play_card(self, game, player, opposing_player):
        player.turn_info.add_money(1)
        player.turn_info.action_only_cost_reductions += 2

    def economy(self):
        return 1.2

    def card_goodness(self):
        return 4

    def get_categories(self):
        return [Card.ECONOMY]
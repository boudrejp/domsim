__author__ = 'breppert'

from Card import Card


class Bridge(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Bridge"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        player.turn_info.cost_reductions += 1
        player.turn_info.add_money(1)
        player.turn_info.buys += 1

    def is_terminal(self):
        return True

    def card_goodness(self):
        return 6

    def plus_buys(self):
        return 1

    def economy(self):
        return 2

    def get_categories(self):
        return [Card.ECONOMY, Card.BUYS]
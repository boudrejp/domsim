__author__ = 'breppert'

from Card import Card


class Festival(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Festival"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions += 1
        player.turn_info.add_money(2)
        player.turn_info.buys += 1

    def card_goodness(self):
        return 5

    def plus_buys(self):
        return 1

    def economy(self):
        return 2

    def is_village(self):
        return True

    def get_categories(self):
        return [Card.ECONOMY, Card.BUYS, Card.VILLAGE]
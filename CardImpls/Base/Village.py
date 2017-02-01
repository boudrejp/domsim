__author__ = 'breppert'

from Card import Card


class Village(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Village"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions += 1
        for i in range(1):
            player.draw_card()

    def draws(self, hand = None):
        return 1

    def is_village(self):
        return 1

    def card_goodness(self):
        return 4

    def get_categories(self):
        return [Card.VILLAGE]
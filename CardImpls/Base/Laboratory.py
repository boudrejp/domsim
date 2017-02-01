__author__ = 'breppert'

from Card import Card


class Laboratory(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Laboratory"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        for i in range(2):
            player.draw_card()

    def draws(self, hand = None):
        return 2

    def is_cantrip(self):
        return True

    def card_goodness(self):
        return 7

    def get_categories(self):
        return [Card.NONTERMINAL_DRAW]
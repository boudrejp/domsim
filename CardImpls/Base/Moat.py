__author__ = 'breppert'

from Card import Card


class Moat(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Moat"

    def get_cost(self, reduction = 0):
        return max([0, 2 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.REACTION]

    def play_card(self, game, player, opposing_player):
        player.turn_info.actions -= 1
        for i in range(2):
            player.draw_card()

    def draws(self, hand = None):
        return 2


    def card_goodness(self):
        return 2

    def get_categories(self):
        return [Card.TERMINAL_DRAW]
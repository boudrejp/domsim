__author__ = 'breppert'

from Card import Card

class Smithy(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Smithy"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        for i in range(3):
            player.draw_card()

    def is_terminal(self):
        return True

    def draws(self, hand = None):
        return 3

    def card_goodness(self):
        return 4

    def get_categories(self):
        return [Card.TERMINAL_DRAW]
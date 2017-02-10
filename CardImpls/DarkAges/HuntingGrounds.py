__author__ = 'breppert'

from Card import Card
from Util.SupplyAnalyzer import *

class HuntingGrounds(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Hunting Grounds"

    def get_cost(self, reduction = 0):
        return max([0, 6 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        for i in range(4):
            player.draw_card()

    def on_trash(self, game, player, opposing_player):
        if get_pile_size("Duchy", game.supply) > 0:
            player.gain_card("Duchy", "discard")
        else:
            for i in range(3):
                player.gain_card("Estate", "discard")
        return True

    def is_terminal(self):
        return True

    def draws(self, hand = None):
        return 4

    def card_goodness(self):
        return 7

    def get_categories(self):
        return [Card.TERMINAL_DRAW]
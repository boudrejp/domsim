__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *
from CardImpls.Helper import *



class Witch(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Witch"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type=None):
        player.turn_info.actions -= 1
        for i in range(2):
            player.draw_card()

        if not opposing_player.blocks_attacks():
            opposing_player.gain_card("Curse")

    def draws(self, hand = None):
        return 2

    def is_terminal(self):
        return True

    def card_goodness(self):
        return 8

    def get_categories(self):
        return [Card.JUNKER, Card.TERMINAL_DRAW]
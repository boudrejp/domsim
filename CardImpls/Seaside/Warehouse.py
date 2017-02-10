__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *
from CardImpls.Helper import *


class Warehouse(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Warehouse"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        for i in range(3):
            player.draw_card()
        for i in range(3):
            discard_card_from_hand(player)

    def is_sifter(self):
        return True

    def is_terminal(self):
        return False

    def card_goodness(self):
        return 4

    def get_categories(self):
        return [Card.SIFTER]


    def can_play_for_benefit(self, game, player, opposing_player):
        if (len(player.deck) + len(player.discard)) <= 2:
            return False
        return True
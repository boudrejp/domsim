__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *
from CardImpls.Helper import *



class Familiar(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Familiar"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_potion_cost(self, reduction = 0):
        return 1

    def get_types(self):
        return [Card.ACTION, Card.ATTACK]

    def play_card(self, game, player, opposing_player, play_type=None):
        player.draw_card()

        if not opposing_player.blocks_attacks():
            opposing_player.gain_card("Curse")




    def is_terminal(self):
        return False

    def card_goodness(self):
        return 8

    def get_categories(self):
        return [Card.JUNKER]

    def is_cantrip(self):
        return True
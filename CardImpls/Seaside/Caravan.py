__author__ = 'breppert'

from Card import Card
from CardImpls.Helper import discard_card_from_hand
from Util.HandHelper import *
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *

class Caravan(Card):
    def __init__(self):
        self.duration_finished = False

    def get_name(self):
        return "Caravan"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.DURATION]


    def play_card(self, game, player, opposing_player, play_type = None):
        self.duration_finished = False
        player.draw_card()

    def duration_card(self, game, player, opposing_player, play_type = None):
        player.draw_card()
        self.duration_finished = True


    def should_duration(self):
        return not self.duration_finished

    def is_terminal(self):
        return False

    def is_cantrip(self):
        return True

    def draws(self, hand = None):
        return 0.5

    ### Subjective information ###
    def card_goodness(self):
        return 5

    def get_categories(self):
        return [Card.NONTERMINAL_DRAW]
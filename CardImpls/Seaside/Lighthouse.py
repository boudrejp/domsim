__author__ = 'breppert'

from Card import Card
from CardImpls.Helper import discard_card_from_hand
from Util.HandHelper import *
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *

class Lighthouse(Card):
    def __init__(self):
        self.duration_finished = False

    def get_name(self):
        return "Lighthouse"

    def get_cost(self, reduction = 0):
        return max([0, 2 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.DURATION]


    def play_card(self, game, player, opposing_player, play_type = None):
        self.duration_finished = False
        player.turn_info.actions += 1
        player.turn_info.add_money(1)

    def duration_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.add_money(1)
        self.duration_finished = True

    def should_duration(self):
        return not self.duration_finished

    def is_terminal(self):
        return False

    def is_village(self):
        return True

    def economy(self):
        return 1.5

    ### Subjective information ###
    def card_goodness(self):
        return 3

    def get_categories(self):
        return [Card.ECONOMY]
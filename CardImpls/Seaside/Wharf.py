__author__ = 'breppert'

from Card import Card
from CardImpls.Helper import discard_card_from_hand
from Util.HandHelper import *
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *

class Wharf(Card):
    def __init__(self):
        self.duration_finished = False

    def get_name(self):
        return "Wharf"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.DURATION]


    def play_card(self, game, player, opposing_player, play_type = None):
        self.duration_finished = False
        player.turn_info.actions -= 1
        for i in range(2):
            player.draw_card()
        player.turn_info.buys += 1

    def duration_card(self, game, player, opposing_player, play_type = None):
        for i in range(2):
            player.draw_card()
        player.turn_info.buys += 1
        self.duration_finished = True


    def should_duration(self):
        return not self.duration_finished

    def is_terminal(self):
        return True


    ### Subjective information ###
    def card_goodness(self):
        return 9

    def draws(self, hand = None):
        return 2.5

    def get_categories(self):
        return [Card.BUYS, Card.TERMINAL_DRAW]
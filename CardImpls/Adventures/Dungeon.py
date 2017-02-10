__author__ = 'breppert'

from Card import Card
from CardImpls.Helper import discard_card_from_hand
from Util.HandHelper import *
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *

class Dungeon(Card):
    def __init__(self):
        self.duration_finished = False

    def get_name(self):
        return "Dungeon"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.DURATION]


    def play_card(self, game, player, opposing_player, play_type = None):
        self.duration_finished = False
        for i in range(2):
           player.draw_card()
        for i in range(2):
            discard_card_from_hand(player)

    def duration_card(self, game, player, opposing_player):
        self.play_card(game, player, opposing_player)
        self.duration_finished = True


    def should_duration(self):
        return not self.duration_finished

    def is_sifter(self):
        return True

    ### Subjective information ###
    def card_goodness(self):
        return 7

    def get_categories(self):
        return [Card.SIFTER]

    def can_play_for_benefit(self, game, player, opposing_player):
        if (len(player.deck) + len(player.discard)) <= 1:
            return False
        return True
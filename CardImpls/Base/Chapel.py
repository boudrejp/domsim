__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *
from CardImpls.Helper.util import *


class Chapel(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Chapel"

    def get_cost(self, reduction = 0):
        return max([0, 2 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        for i in range(4):
            trash_card_from_hand(self, player, False)

    def is_terminal(self):
        return True

    def card_goodness(self):
        return 8

    def trashes_from_hand(self, player):
        trash_candidates = 0
        for card in player.hand:
            if card.get_name() == "Copper" or card.get_name() == "Estate" or card.get_name() == "Curse":
                trash_candidates += 1
        return trash_candidates

    def can_play_for_benefit(self, game, player, opposing_player):
        if get_total_cards_wanted_to_trash_from_hand(self, player) >= 1:
            return True
        else:
            return False


    def trashes(self):
        return 4

    def get_categories(self):
        return [Card.TRASHER]

    def trashes_estates(self):
        return True

    def trashes_coppers(self):
        return True
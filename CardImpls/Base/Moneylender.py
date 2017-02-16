__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *
from CardImpls.Helper.util import *


class Moneylender(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Moneylender"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        for i in range(1):
            trashed_a_card = trash_card_from_hand(self, player, False)
            if trashed_a_card:
                player.turn_info.add_money(3)

    def is_terminal(self):
        return True

    def card_goodness(self):
        return 4

    def can_play_for_benefit(self, game, player, opposing_player):
        if get_total_cards_wanted_to_trash_from_hand(self, player) >= 1:
            return True
        else:
            return False


    def trashes(self):
        return 4

    def economy(self):
        return 0.5

    def get_categories(self):
        return [Card.TRASHER]

    def trashes_estates(self):
        return False

    def trashes_coppers(self):
        return True
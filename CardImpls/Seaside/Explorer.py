__author__ = 'breppert'

from Card import Card
from Util.SupplyAnalyzer import *
from CardImpls.Helper.util import *
from Config import *

class Explorer(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Explorer"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1

        if player.get_cards_in_hand_by_name().count("Province") >= 1:
            if LOGGING:
                print "Revealing Province..."
            player.gain_card("Gold", "hand")
        else:
            player.gain_card("Silver", "hand")


    def can_play_for_benefit(self, game, player, opposing_player):
        if get_total_cards_wanted_to_trash_from_hand(self, player) >= 2:
            return True
        else:
            return False


    def is_terminal(self):
        return True


    def card_goodness(self):
        return 5

    def get_categories(self):
        return [Card.TRASHER]
__author__ = 'breppert'

from Card import Card
from Util.SupplyAnalyzer import *
from CardImpls.Helper.util import *

class TradingPost(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Trading Post"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1

        trashing_going_normally = True
        for i in range(2):
            trashing_going_normally = trash_card_from_hand(self, player, True)

        if trashing_going_normally and get_pile_size("Silver", game.supply) >= 1:
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
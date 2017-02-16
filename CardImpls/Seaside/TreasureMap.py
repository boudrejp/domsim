__author__ = 'breppert'

from Card import Card
from Interactions import StandardInteractions
from Config import LOGGING

from CardImpls.Helper import *

class TreasureMap(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Treasure Map"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1

        player.trash_card(self, "play_area")


        if 'Treasure Map' in player.get_cards_in_hand_by_name():
            card_to_trash = player.hand[player.get_cards_in_hand_by_name().index("Treasure Map")]
            card_was_trashed = player.trash_card(card_to_trash, "hand")


            if card_was_trashed:
                for i in range(4):
                    player.gain_card("Gold", "topdeck")




    def is_terminal(self):
        return True

    def economy(self):
        return 2

    def card_goodness(self):
        return 5

    def can_play_for_benefit(self, game, player, opposing_player):
        if cards_in_deck("Gold", player) >= 4:
            breaker = 7
        if player.get_cards_in_hand_by_name().count(self.get_name()) >= 2 or cards_in_deck("Gold", player) >= 4:
            return True
        else:
            return False

    def get_categories(self):
        return [Card.GAINER]
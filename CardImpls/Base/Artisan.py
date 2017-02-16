__author__ = 'breppert'

from Card import Card
from Util.SupplyAnalyzer import *
from CardImpls.Helper.util import *

class Artisan(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Artisan"

    def get_cost(self, reduction = 0):
        return max([0, 6 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        card_to_gain = player.get_card_to_buy(5, 1, True, "Artisan")
        player.gain_card(card_to_gain, "hand")

        card_to_topdeck = None
        cards_to_topdeck = topdeck_cards(player, player.hand, return_only=True)
        if len(cards_to_topdeck) >= 1:
            card_to_topdeck = cards_to_topdeck[0]

        if card_to_topdeck is not None:
            player.hand.remove(card_to_topdeck)
            player.topdeck_card(card_to_topdeck)


    def is_terminal(self):
        return True


    def card_goodness(self):
        return 7

    def get_categories(self):
        return [Card.GAINER]
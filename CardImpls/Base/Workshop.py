__author__ = 'breppert'

from Card import Card
from Config import *


class Workshop(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Workshop"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1

        card_to_gain = player.get_card_to_buy(4, 1, True, "Workshop")
        if LOGGING:
            print "%s Gaining %s" % (player.player_name, card_to_gain)
        player.gain_card(card_to_gain, "discard")

    def card_goodness(self):
        return 2

    def get_categories(self):
        return [Card.GAINER]
__author__ = 'breppert'

from Card import Card
from Interactions import StandardInteractions

from CardImpls.Helper import *

class Mountebank(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Mountebank"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.ATTACK]

    def play_card(self, game, player, opposing_player):
        player.turn_info.actions -= 1
        player.turn_info.add_money(2)

        if not opposing_player.blocks_attacks():
            if not StandardInteractions.discard_to_block_mountebank(opposing_player):
                opposing_player.gain_card("Curse", "discard")
                opposing_player.gain_card("Copper", "discard")

    def is_terminal(self):
        return True

    def economy(self):
        return 2

    def card_goodness(self):
        return 9

    def get_categories(self):
        return [Card.TERMINAL_PAYLOAD_STACKING]
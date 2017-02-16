__author__ = 'breppert'

from Card import Card
from Interactions import StandardInteractions
from Config import LOGGING

from CardImpls.Helper import *

class SeaHag(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Sea Hag"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.ATTACK]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1

        if not opposing_player.blocks_attacks():
            top_opposing_player_cards = opposing_player.reveal_cards(1)
            if len(top_opposing_player_cards) == 1:
                if LOGGING:
                    print "%s Discarding %s" % (opposing_player.player_name, top_opposing_player_cards[0].get_name())
                opposing_player.discard.append(top_opposing_player_cards[0])

            opposing_player.gain_card("Curse", "topdeck")

    def is_terminal(self):
        return True

    def economy(self):
        return 2

    def card_goodness(self):
        return 5

    def get_categories(self):
        return [Card.JUNKER]
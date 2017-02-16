__author__ = 'breppert'

from Card import Card
from CardImpls.Helper.util import *

class GhostShip(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Ghost Ship"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.ATTACK]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        for i in range(2):
            player.draw_card()

        if not opposing_player.blocks_attacks():
            while len(opposing_player.hand) >= 4:
                card_to_topdeck = None
                cards_to_topdeck = topdeck_cards(opposing_player, opposing_player.hand, return_only=True)
                if len(cards_to_topdeck) >= 1:
                    card_to_topdeck = cards_to_topdeck[0]

                if card_to_topdeck is not None:
                    opposing_player.hand.remove(card_to_topdeck)
                    opposing_player.topdeck_card(card_to_topdeck)

    def is_terminal(self):
        return True

    def draws(self, hand = None):
        return 2

    def card_goodness(self):
        return 7

    def get_categories(self):
        return [Card.TERMINAL_DRAW, Card.TERMINAL_PAYLOAD_NONSTACKING]
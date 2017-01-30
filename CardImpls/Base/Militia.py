__author__ = 'breppert'


from Card import Card

from CardImpls.Helper import *

class Militia(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Militia"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.ATTACK]

    def play_card(self, game, player, opposing_player):
        player.turn_info.actions -= 1
        player.turn_info.add_money(2)

        if not opposing_player.blocks_attacks():
            while len(opposing_player.hand) >= 4:
                discard_card_from_hand(opposing_player)

    def is_terminal(self):
        return True

    def draws(self, hand = None):
        return 3

    def card_goodness(self):
        return 4

    def economy(self):
        return 2

    def get_categories(self):
        return [Card.TERMINAL_PAYLOAD_NONSTACKING]


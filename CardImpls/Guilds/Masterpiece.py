__author__ = 'breppert'

from Card import Card

class Masterpiece(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Masterpiece"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.TREASURE]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.add_money(1)

    def economy(self):
        return 1

    def card_goodness(self):
        return -12

    def can_overpay(self):
        return True

    def do_overpay(self, player, opposing_player, overpay_amount):
        for i in range(overpay_amount):
            player.gain_card("Silver", "discard")
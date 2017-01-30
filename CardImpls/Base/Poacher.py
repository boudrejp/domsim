__author__ = 'breppert'

from Card import Card
from CardImpls.Helper import discard_card_from_hand


class Poacher(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Poacher"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player):
        for i in range(1):
            player.draw_card()
        player.turn_info.add_money(1)
        for i in range(game.supply.get_num_empty_piles()):
            discard_card_from_hand(player)

    def draws(self, hand = None):
        return 1

    def is_cantrip(self):
        return True

    def card_goodness(self):
        return 4

    def economy(self):
        return 1

    def get_categories(self):
        return [Card.ECONOMY]
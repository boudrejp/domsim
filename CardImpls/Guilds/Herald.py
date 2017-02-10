__author__ = 'breppert'

from Card import Card
from Util.PlayHelper import *


class Herald(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Herald"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        for i in range(1):
            player.draw_card()
        revealed_cards = player.reveal_cards(1)
        if len(revealed_cards) == 1:
            revealed_card = revealed_cards[0]
            if Card.ACTION in revealed_card.get_types():
                player.play_card(revealed_card, None, "deck")
            else:
                player.topdeck_card(revealed_card)

    def can_overpay(self):
        return True

    def do_overpay(self, player, opposing_player, overpay_amount):
        for i in range(overpay_amount):
            best_card = get_max_goodness(player.discard)
            player.discard.remove(best_card)
            player.topdeck_card(best_card)

    def is_cantrip(self):
        return True

    def draws(self, hand = None):
        return 1

    def is_village(self):
        return 1

    def card_goodness(self):
        return 6

    def get_categories(self):
        return [Card.VILLAGE, Card.NONTERMINAL_DRAW]
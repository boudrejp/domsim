__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *
from CardImpls.Helper import util


class HuntingParty(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Hunting Party"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type=None):
        player.draw_card()

        cards_in_hand = player.get_cards_in_hand_by_name()
        revealed_cards = player.reveal_cards(1)
        cards_to_discard = []
        while len(revealed_cards) != 0:
            revealed_card = revealed_cards[0]
            if revealed_card.get_name() not in cards_in_hand:
                player.hand.append(revealed_card)
                break
            else:
                cards_to_discard.append(revealed_card)
                revealed_cards = player.reveal_cards(1)

        for card in cards_to_discard:
            player.discard_card(card, "deck")

    def is_terminal(self):
        return False

    def card_goodness(self):
        return 8

    def draws(self, hand = None):
        return 2

    def get_categories(self):
        return [Card.NONTERMINAL_DRAW]
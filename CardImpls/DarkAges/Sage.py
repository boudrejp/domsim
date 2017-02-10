__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *
from CardImpls.Helper import util


class Sage(Card):

    def __init__(self):
        pass

    def get_name(self):
        return "Sage"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type=None):
        revealed_cards = player.reveal_cards(1)
        cards_to_discard = []
        while len(revealed_cards) != 0:
            revealed_card = revealed_cards[0]
            if revealed_card.get_cost(player.turn_info.get_reduction(revealed_card.get_types())) >= 3:
                player.hand.append(revealed_card)
                break
            else:
                cards_to_discard.append(revealed_card)
                revealed_cards = player.reveal_cards(1)

        for card in cards_to_discard:
            player.discard_card(card, "deck")


    def sifts_from_deck(self):
        return True

    def is_terminal(self):
        return False

    def card_goodness(self):
        return 3

    def get_categories(self):
        return [Card.SIFTER]

    def is_cantrip(self):
        return True

    def is_sifter(self):
        return True
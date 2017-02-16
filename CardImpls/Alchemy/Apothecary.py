__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *
from CardImpls.Helper import *



class Apothecary(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Apothecary"

    def get_cost(self, reduction = 0):
        return max([0, 2 - reduction])

    def get_potion_cost(self, reduction = 0):
        return 1

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type=None):
        player.draw_card()

        revealed_cards = player.reveal_cards(4)
        cards_to_put_back = []
        cards_to_put_in_hand = []
        for i, card in enumerate(revealed_cards):
            if card.get_name() == "Copper":
                cards_to_put_in_hand.append(card)
            else:
                cards_to_put_back.append(card)

        for card in cards_to_put_in_hand:
            player.hand.append(card)

        topdeck_cards(player, cards_to_put_back)

    def sifts_from_deck(self):
        return True

    def draws(self, hand = None):
        return 1

    def is_terminal(self):
        return False

    def card_goodness(self):
        return 7

    def get_categories(self):
        return [Card.SIFTER, Card.NONTERMINAL_DRAW]

    def is_cantrip(self):
        return True

    def is_sifter(self):
        return True
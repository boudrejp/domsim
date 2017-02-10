__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *
from CardImpls.Helper import *



class Cartographer(Card):
    TOSS_TERMINALS = False


    def __init__(self):
        pass

    def get_name(self):
        return "Cartographer"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type="Money"):
        player.draw_card(1)

        revealed_cards = player.reveal_cards(4)
        cards_to_put_back = []
        cards_to_discard = []
        for i, card in enumerate(revealed_cards):
            if Card.VICTORY in card.get_types() or Card.JUNK in card.get_types() or card.get_name() == "Copper":
                cards_to_discard.append(card)
            else:
                cards_to_put_back.append(card)

        for card in cards_to_discard:
            player.discard_card(card, "deck")

        for card in cards_to_put_back:
            player.topdeck_card(card)
        #topdeck_cards(player, cards_to_put_back)

    def sifts_from_deck(self):
        return True

    def is_terminal(self):
        return False

    def card_goodness(self):
        return 6

    def get_categories(self):
        return [Card.SIFTER]

    def is_cantrip(self):
        return True

    def is_sifter(self):
        return True
__author__ = 'breppert'


from Card import Card

from CardImpls.Helper import *

class Survivors(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Survivors"

    def get_cost(self, reduction = 0):
        return max([0, 0 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.RUIN]

    def play_card(self, game, player, opposing_player, play_type = None):
        #Rudimentary logic where it puts back if both cards are "good" and discards if either is bad.

        revealed_cards = player.reveal_cards(2)

        should_put_back = True

        for i, card in enumerate(revealed_cards):
            if card.get_name() == "Copper" or (Card.VICTORY in card.get_types() and Card.ACTION not in card.get_types()) or \
            card.JUNK in card.get_categories():
                should_put_back = False

        if should_put_back:
            for i in range(len(revealed_cards)):
                player.topdeck_card(revealed_cards[i])
        else:
            for i in range(len(revealed_cards)):
                player.discard_card(revealed_cards[i], "deck")

    def card_goodness(self):
        return -30

    def is_terminal(self):
        return True

    def get_categories(self):
        return [Card.JUNK]


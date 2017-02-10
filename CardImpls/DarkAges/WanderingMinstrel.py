__author__ = 'breppert'

from Card import Card
from CardImpls.Helper import util


class WanderingMinstrel(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Wandering Minstrel"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions += 1
        for i in range(1):
            player.draw_card()

        revealed_cards = player.reveal_cards(3)
        cards_to_discard = []
        cards_to_topdeck = []
        for card in revealed_cards:
            if Card.ACTION in card.get_types():
                cards_to_topdeck.append(card)
            else:
                cards_to_discard.append(card)

        for card in cards_to_discard:
            player.discard_card(card, "deck")

        util.topdeck_cards(player, cards_to_topdeck)




    def draws(self, hand = None):
        return 1

    def is_village(self):
        return 1

    def card_goodness(self):
        return 7

    def get_categories(self):
        return [Card.VILLAGE]
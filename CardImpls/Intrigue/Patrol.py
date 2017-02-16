__author__ = 'breppert'

from Card import Card
from CardImpls.Helper import util

class Patrol(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Patrol"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        for i in range(3):
            player.draw_card()

        revealed_cards = player.reveal_cards(4)
        cards_to_hand = []
        cards_to_topdeck = []
        for card in revealed_cards:
            if Card.VICTORY in card.get_types() or Card.CURSE in card.get_types():
                cards_to_hand.append(card)
            else:
                cards_to_topdeck.append(card)

        for card in cards_to_hand:
            player.hand.append(card)

        util.topdeck_cards(player, cards_to_topdeck)



    def is_terminal(self):
        return True

    def draws(self, hand = None):
        return 3.2

    def card_goodness(self):
        return 8

    def get_categories(self):
        return [Card.TERMINAL_DRAW]
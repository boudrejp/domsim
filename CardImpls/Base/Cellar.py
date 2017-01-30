__author__ = 'breppert'

from Card import Card
from CardImpls.Helper import discard_card_from_hand

class Cellar(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Cellar"

    def get_cost(self, reduction = 0):
        return max([0, 2 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player):
        cards_by_name = map(lambda x: x.get_name(), player.hand)
        cards_to_discard = cards_by_name.count("Estate") + cards_by_name.count("Copper") + cards_by_name.count("Curse")
        for i in range(cards_to_discard):
            discard_card_from_hand(player)
        for i in range(cards_to_discard):
            player.draw_card()

    def is_sifter(self):
        return True

    def is_terminal(self):
        return False

    def card_goodness(self):
        return 2

    def get_categories(self):
        return [Card.SIFTER]
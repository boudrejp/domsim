__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *


class Chapel(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Chapel"

    def get_cost(self, reduction = 0):
        return max([0, 2 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player):
        player.turn_info.actions -= 1
        for i in range(4):
            for card in player.hand:
                if card.get_name() == "Estate":
                    player.trash_card(card, "hand")
                    break
                elif card.get_name() == "Curse":
                    player.trash_card(card, "hand")
                    break
                elif card.get_name() == "Copper" and get_total_economy(player) > 4:
                    player.trash_card(card, "hand")
                    break

    def is_terminal(self):
        return True

    def card_goodness(self):
        return 8

    def trashes_from_hand(self, player):
        trash_candidates = 0
        for card in player.hand:
            if card.get_name() == "Copper" or card.get_name() == "Estate" or card.get_name("Curse"):
                trash_candidates += 1
        return trash_candidates


    def trashes(self):
        return 4

    def get_categories(self):
        return [Card.TRASHER]

    def trashes_estates(self):
        return True

    def trashes_coppers(self):
        return True
__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *
from CardImpls.Helper.util import *


class Forager(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Forager"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        trash_card_from_hand(self, player, True)
        player.turn_info.add_money(self.get_unique_treasures_in_trash(game))


    def get_unique_treasures_in_trash(self, game):
        trash = game.trash
        unique_treasues_in_trash = []
        for card in trash:
            if Card.TREASURE in card.get_types():
                card_name = card.get_name()
                if card_name not in unique_treasues_in_trash:
                    unique_treasues_in_trash.append(card_name)

        return len(unique_treasues_in_trash)



    def is_terminal(self):
        return False

    def card_goodness(self):
        return 4

    def trashes_from_hand(self, player):
        trash_candidates = 0
        for card in player.hand:
            if card.get_name() == "Copper" or card.get_name() == "Estate" or card.get_name() == "Curse":
                trash_candidates += 1
        return trash_candidates

    def can_play_for_benefit(self, game, player, opposing_player):
        if get_total_cards_wanted_to_trash_from_hand(self, player) >= 1:
            return True
        else:
            return False

    def trashes(self):
        return 1

    def is_compulsive_trasher(self):
        return True

    def get_categories(self):
        return [Card.TRASHER]

    def trashes_estates(self):
        return True

    def trashes_coppers(self):
        return True
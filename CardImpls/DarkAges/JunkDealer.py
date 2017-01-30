__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *


class JunkDealer(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Junk Dealer"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player):
        player.draw_card()

        player.turn_info.add_money(1)

        cards_by_name = map(lambda x: x.get_name(), player.hand)

        for i in range(1):
            trash_target = None
            if "Curse" in cards_by_name:
                trash_target = "Curse"
            elif "Estate" in cards_by_name:
                trash_target = "Estate"
            elif "Copper" in cards_by_name:
                trash_target = "Copper"
            elif "Silver" in cards_by_name:
                trash_target = "Silver"
            else:
                trash_target = cards_by_name[0]

            for card in player.hand:
                if card.get_name() == trash_target:
                    player.trash_card(card, "hand")
                    break


    def is_terminal(self):
        return False

    def card_goodness(self):
        return 8

    def trashes_from_hand(self, player):
        trash_candidates = 0
        for card in player.hand:
            if card.get_name() == "Copper" or card.get_name() == "Estate" or card.get_name("Curse"):
                trash_candidates += 1
        return trash_candidates


    def trashes(self):
        return 1

    def is_cantrip(self):
        return True

    def get_categories(self):
        return [Card.TRASHER]

    def trashes_estates(self):
        return True

    def trashes_coppers(self):
        return True
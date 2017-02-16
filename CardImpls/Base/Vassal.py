__author__ = 'breppert'

from Card import Card
from Util.PlayHelper import *


class Vassal(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Vassal"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        player.turn_info.add_money(2)
        revealed_cards = player.reveal_cards(1)
        if len(revealed_cards) == 1:
            revealed_card = revealed_cards[0]
            if Card.ACTION in revealed_card.get_types():
                if revealed_card.can_play_for_benefit(game, player, opposing_player):
                    player.turn_info.actions += 1 #Hackery for sure, who cares
                    player.play_card(revealed_card, None, "deck")
            else:
                player.discard_card(revealed_card, "deck")

    def is_terminal(self):
        return True

    def economy(self):
        return 2

    def draws(self, hand = None):
        return 0.5

    def card_goodness(self):
        return 4

    def get_categories(self):
        return [Card.ECONOMY]
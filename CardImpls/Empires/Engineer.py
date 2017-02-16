__author__ = 'breppert'

from Card import Card
from Config import *


class Engineer(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Engineer"

    def get_cost(self, reduction = 0):
        return max([0, 0 - reduction])

    def get_debt(self):
        return 4

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = "trashing"):
        player.turn_info.actions -= 1

        card_to_gain = player.get_card_to_buy(4, 1, True, "Engineer")
        player.gain_card(card_to_gain, "discard")

        if play_type == "trashing" or play_type == None:
            player.trash_card(self, "play_area")
            card_to_gain = player.get_card_to_buy(4, 1, True, "Engineer")
            player.gain_card(card_to_gain, "discard")



    def card_goodness(self):
        return 5

    def get_categories(self):
        return [Card.GAINER]
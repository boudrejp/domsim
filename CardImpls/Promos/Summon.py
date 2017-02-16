__author__ = 'breppert'

from Card import Card
from Config import *


class Summon(Card):
    def __init__(self):
        pass
        self.set_aside_card = None

    def get_name(self):
        return "Summon"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        card_to_gain = player.get_card_to_buy(4, 1, True, "Summon")
        player.gain_card(card_to_gain, "discard")

    def card_goodness(self):
        return 5

    def get_categories(self):
        return [Card.GAINER]

    def do_on_buy(self, game, player, opposing_player):
        card_to_gain = player.get_card_to_buy(4, 1, True, "Summon")
        if card_to_gain != "Death Cart" and card_to_gain != "Border Village":
            gained_card = player.gain_card(card_to_gain, "set aside")
            self.set_aside_card = gained_card
        else: #  Lose track
            player.gain_card(card_to_gain, "discard")

        player.set_aside_area.append(self)

    def call_from_set_aside(self, game, player, opposing_player):
        player.set_aside_area.remove(self)
        if self.set_aside_card is not None:
            player.turn_info.actions += 1
            player.play_card(self.set_aside_card, None, "set aside")

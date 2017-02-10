__author__ = 'breppert'

from Card import Card

class Potion(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Potion"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.TREASURE]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.potions += 1

    def economy(self):
        return 0

    def card_goodness(self):
        return 5
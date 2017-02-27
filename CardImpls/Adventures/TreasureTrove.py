__author__ = 'breppert'

from Card import Card

class TreasureTrove(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Treasure Trove"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.TREASURE]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.add_money(2)
        player.gain_card("Gold", "discard")
        player.gain_card("Copper", "discard")

    def economy(self):
        return 2

    def card_goodness(self):
        return 6

    def get_categories(self):
        return [Card.ECONOMY]
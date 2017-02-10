__author__ = 'breppert'

from Card import Card

class Tunnel(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Tunnel"

    def get_types(self):
        return [Card.VICTORY]

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_victory_points(self, player, opposing_player):
        return 2

    def on_discard(self, game, player, opposing_player):
        player.gain_card("Gold", "discard")
        return True


    def get_categories(self):
        return [Card.POINTS]
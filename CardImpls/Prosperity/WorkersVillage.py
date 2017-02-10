__author__ = 'breppert'

from Card import Card


class WorkersVillage(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Worker's Village"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions += 1
        for i in range(1):
            player.draw_card()

        player.turn_info.buys += 1

    def draws(self, hand = None):
        return 1

    def is_village(self):
        return 1

    def card_goodness(self):
        return 6

    def get_categories(self):
        return [Card.VILLAGE, Card.BUYS]
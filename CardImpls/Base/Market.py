__author__ = 'breppert'

from Card import Card


class Market(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Market"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player):
        for i in range(1):
            player.draw_card()
        player.turn_info.add_money(1)
        player.turn_info.buys += 1

    def draws(self, hand = None):
        return 1

    def is_cantrip(self):
        return True

    def card_goodness(self):
        return 5

    def plus_buys(self):
        return 1

    def economy(self):
        return 1

    def get_categories(self):
        return [Card.ECONOMY, Card.BUYS]
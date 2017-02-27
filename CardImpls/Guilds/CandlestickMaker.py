__author__ = 'breppert'

from Card import Card


class CandlestickMaker(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Candlestick Maker"

    def get_cost(self, reduction = 0):
        return max([0, 2 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.coin_tokens += 1
        player.turn_info.buys += 1

    def card_goodness(self):
        return 3

    def economy(self):
        return 1

    def get_categories(self):
        return [Card.ECONOMY, Card.BUYS]
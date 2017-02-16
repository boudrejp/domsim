__author__ = 'breppert'

from Card import Card


class CityQuarter(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "City Quarter"

    def get_cost(self, reduction = 0):
        return max([0, 0 - reduction])

    def get_debt(self):
        return 8

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions += 1

        cards_to_draw = 0
        for card in player.hand:
            if Card.ACTION in card.get_types():
                cards_to_draw += 1
        for i in range(cards_to_draw):
            player.draw_card()

    def draws(self, hand = None):
        return 4

    def should_play_first(self):
        return True

    def is_village(self):
        return 1

    def card_goodness(self):
        return 9

    def get_categories(self):
        return [Card.VILLAGE, Card.NONTERMINAL_DRAW]
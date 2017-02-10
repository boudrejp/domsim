__author__ = 'breppert'

from Card import Card


class Ironworks(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Ironworks"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1

        card_to_gain = player.get_card_to_buy(4, 1, True, "Ironworks")
        gained_card_obj = player.gain_card(card_to_gain, "discard")

        if Card.ACTION in gained_card_obj.get_types():
            player.turn_info.actions += 1
        if Card.TREASURE in gained_card_obj.get_types():
            player.turn_info.add_money(1)
        if Card.VICTORY in gained_card_obj.get_types():
            player.draw_card()

    def is_terminal(self):
        return False #TODO: Fix

    def card_goodness(self):
        return 6

    def get_categories(self):
        return [Card.GAINER]
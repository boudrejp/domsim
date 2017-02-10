__author__ = 'breppert'

from Card import Card


class BorderVillage(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Border Village"

    def get_cost(self, reduction = 0):
        return max([0, 6 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions += 1
        for i in range(1):
            player.draw_card()

    def draws(self, hand = None):
        return 1

    def is_village(self):
        return 1

    def card_goodness(self):
        return 9

    def get_categories(self):
        return [Card.VILLAGE]

    def do_on_gain(self, game, player, opposing_player):
        card_to_gain = player.get_card_to_buy(
            self.get_cost(reduction=player.turn_info.cost_reductions + player.turn_info.action_only_cost_reductions) - 1,
            buys=1,
            forced=True,
            gain_type="Border Village")
        player.gain_card(card_to_gain, "discard")
        return True
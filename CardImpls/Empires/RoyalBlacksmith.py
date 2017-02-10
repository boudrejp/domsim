__author__ = 'breppert'

from Card import Card

class RoyalBlacksmith(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Royal Blacksmith"

    def get_cost(self, reduction = 0):
        return max([0, 0 - reduction])

    def get_debt(self):
        return 8

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1
        for i in range(5):
            player.draw_card()

        coppers_to_discard = []
        for card in player.hand:
            if card.get_name() == "Copper":
                coppers_to_discard.append(card)

        for copper in coppers_to_discard:
            player.discard_card(copper, "hand")


    def is_terminal(self):
        return True

    def draws(self, hand = None):
        return 5

    def card_goodness(self):
        return 8

    def get_categories(self):
        return [Card.TERMINAL_DRAW]
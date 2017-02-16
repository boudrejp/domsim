__author__ = 'breppert'


from CardImpls.Helper.util import *


class Mill(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Mill"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.VICTORY]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.draw_card()


        #If we want to discard at least one card that would help us, go ahead and do the discard.
        #TODO: Don't discard if the second card is silver or better.
        #TODO (unlikley): Discard if over-drawing for extra $
        card_wanted_to_discard_most = discard_card_from_hand(player, return_only=True)
        if Card.JUNK in card_wanted_to_discard_most.get_categories() or "Estate" == card_wanted_to_discard_most.get_name():
            for i in range(2):
                discard_card_from_hand(player)
            player.turn_info.add_money(2)


    def get_victory_points(self, player, opposing_player):
        return 1

    def is_terminal(self):
        return False

    def card_goodness(self):
        return 5

    def draws(self, hand = None):
        return 1

    def is_cantrip(self):
        return True

    def get_categories(self):
        return [Card.ECONOMY]
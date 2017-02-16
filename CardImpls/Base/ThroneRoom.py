__author__ = 'breppert'

from Card import Card


class ThroneRoom(Card):
    def __init__(self):
        pass
        self.duration_finished = False
        self.attached_to_duration = False
        self.duration_attachment = None

    def get_name(self):
        return "Throne Room"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        self.duration_finished = True
        self.attached_to_duration = False

        next_card, play_instructions = player.get_action_card_to_play_next()
        if next_card is not None:
            player.turn_info.actions += 1 #Because I did actions kinda funny, ok?
            player.play_card(next_card, play_instructions, "hand")
            player.play_card(next_card, play_instructions, "throned")

            if next_card.should_duration():
                self.attached_to_duration = True
                self.duration_attachment = next_card
                self.duration_finished = False

    def duration_card(self, game, player, opposing_player):
        self.duration_attachment.duration_card(game, player, opposing_player)
        self.duration_finished = True if self.duration_attachment.should_duration() else False


    def should_duration(self):
        return not self.duration_finished

    def draws(self, hand = None):
        return 1

    def is_village(self):
        return 1

    def card_goodness(self):
        return 6

    def get_categories(self):
        return [Card.THRONE_VARIANT, Card.VILLAGE]
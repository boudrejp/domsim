__author__ = 'breppert'

class SingleGameStats(object):
    def __init__(self):
        self.turn_output_moneys = []
        self.turn_output_buys = []
        self.turn_percentage_deck_draw = []
        self.turn_attacks_in_play = []

    def add_money_output(self, output):
        self.turn_output_moneys.append(output)

    def get_money_output(self):
        return self.turn_output_moneys

    def add_num_attacks_in_play(self, attacks_in_play):
        self.turn_attacks_in_play.append(attacks_in_play)

    def get_attacks_in_play(self):
        return self.turn_attacks_in_play
__author__ = 'breppert'

class SingleGameStats(object):
    def __init__(self):
        self.turn_output_moneys = []
        self.turn_output_buys = []
        self.turn_percentage_deck_draw = []
        self.turn_attacks_in_play = []
        self.total_cards_trashed = 0
        self.estate_cards_trashed = 0
        self.copper_cards_trashed = 0

    def add_money_output(self, output):
        self.turn_output_moneys.append(output)

    def get_money_output(self):
        return self.turn_output_moneys

    def add_num_attacks_in_play(self, attacks_in_play):
        self.turn_attacks_in_play.append(attacks_in_play)

    def get_attacks_in_play(self):
        return self.turn_attacks_in_play

    def increment_cards_trashed(self):
        self.total_cards_trashed += 1

    def increment_coppers_trashed(self):
        self.copper_cards_trashed += 1

    def increment_estates_trashed(self):
        self.estate_cards_trashed += 1

    def get_total_cards_trashed(self):
        return self.total_cards_trashed

    def get_total_coppers_trashed(self):
        return self.copper_cards_trashed

    def get_total_estates_trashed(self):
        return self.estate_cards_trashed

    def get_max_open_number_hit(self):
        '''
        returns maximum number hit on turn 3 or 4
        '''
        return max([self.turn_output_moneys[2], self.turn_output_moneys[3]])

    def get_max_open_number_hit_twice(self):
        '''
        returns minimum number hit on both turns 3 and 4
        '''
        return min([self.turn_output_moneys[2], self.turn_output_moneys[3]])
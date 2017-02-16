__author__ = 'breppert'

from SingleGameStats import *

class PlayerStats(object):
    def __init__(self, player_name):
        self.player_name = player_name
        self.game_stats_list = []
        self.game_number = -1


    def start_new_game(self):
        self.game_stats_list.append(SingleGameStats())
        self.game_number += 1

    def add_money_output(self, output):
        self.get_current_game().add_money_output(output)

    def add_attacks_in_play(self, attacks):
        self.get_current_game().add_num_attacks_in_play(attacks)

    def get_current_game(self):
        return self.game_stats_list[self.game_number]

    def increment_trashed_cards(self):
        self.get_current_game().increment_cards_trashed()

    def increment_trashed_coppers(self):
        self.get_current_game().increment_coppers_trashed()

    def increment_trashed_estates(self):
        self.get_current_game().increment_estates_trashed()

    def get_average_money_output(self):
        each_games_average = []
        for game in self.game_stats_list:
            game_outputs = game.get_money_output()
            each_games_average.append(float(sum(game_outputs))/len(game_outputs))
        return sum(each_games_average) / len(each_games_average)

    def get_average_cards_trashed(self):
        each_games_amount = []
        for game in self.game_stats_list:
            cards_trashed = game.get_total_cards_trashed()
            each_games_amount.append(cards_trashed)
        return float(sum(each_games_amount)) / len(each_games_amount)

    def get_average_coppers_trashed(self):
        each_games_amount = []
        for game in self.game_stats_list:
            cards_trashed = game.get_total_coppers_trashed()
            each_games_amount.append(cards_trashed)
        return float(sum(each_games_amount)) / len(each_games_amount)

    def get_average_estates_trashed(self):
        each_games_amount = []
        for game in self.game_stats_list:
            cards_trashed = game.get_total_estates_trashed()
            each_games_amount.append(cards_trashed)
        return float(sum(each_games_amount)) / len(each_games_amount)

    def get_average_attacks_output(self):
        each_games_average = []
        for game in self.game_stats_list:
            game_outputs = game.get_attacks_in_play()
            each_games_average.append(float(sum(game_outputs))/len(game_outputs))
        return sum(each_games_average) / len(each_games_average)


    def get_open_number_hit_percentage(self):
        number_hit_dict = {}
        total_games = len(self.game_stats_list)
        percentages_dict = {}
        for game in self.game_stats_list:
            game_output = game.get_max_open_number_hit()
            outputs_to_update = range(0, game_output+1)

            for output in outputs_to_update:
                if output not in number_hit_dict:
                    number_hit_dict[output] = 1
                else:
                    number_hit_dict[output] = number_hit_dict[output] + 1

        for number in number_hit_dict.keys():
            percentages_dict[number] = "%.2f%%" % (float(number_hit_dict[number]) / total_games * 100)

        return percentages_dict

    def get_open_number_hit_twice_percentage(self):
        number_hit_dict = {}
        total_games = len(self.game_stats_list)
        percentages_dict = {}
        for game in self.game_stats_list:
            game_output = game.get_max_open_number_hit_twice()
            outputs_to_update = range(0, game_output+1)

            for output in outputs_to_update:
                if output not in number_hit_dict:
                    number_hit_dict[output] = 1
                else:
                    number_hit_dict[output] = number_hit_dict[output] + 1

        for number in number_hit_dict.keys():
            percentages_dict[number] = "%.2f%%" % (float(number_hit_dict[number]) / total_games * 100)

        return percentages_dict
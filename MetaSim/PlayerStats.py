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

    def get_average_money_output(self):
        each_games_average = []
        for game in self.game_stats_list:
            game_outputs = game.get_money_output()
            each_games_average.append(float(sum(game_outputs))/len(game_outputs))
        return sum(each_games_average) / len(each_games_average)

    def get_average_attacks_output(self):
        each_games_average = []
        for game in self.game_stats_list:
            game_outputs = game.get_attacks_in_play()
            each_games_average.append(float(sum(game_outputs))/len(game_outputs))
        return sum(each_games_average) / len(each_games_average)


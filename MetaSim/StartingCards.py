__author__ = 'breppert'

from Config import *
from Game import *
from StartingCardsConfigs import *
from PlayerStats import *

winner_list = []

p1stats = PlayerStats("Player One")
p2stats = PlayerStats("Mic Qsenoch")


for i in range(RUNS):
    game = Game("Player One", "Mic Qsenoch", Player, Player, p1stats, p2stats, None, State.State().get_cards())
    winner = game.play_game(1, 2)
    winner_list.append(winner)
    if i % 1000 == 0:
        print i, "runs done...."


print p2stats.get_average_money_output()
print p2stats.get_average_attacks_output()
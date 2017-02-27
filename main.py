__author__ = 'breppert'

import Game
from Players import *
from Player import *
from MetaSim import PlayerStats

winner_list = []

p1stats = PlayerStats.PlayerStats("Archibald")
p2stats = PlayerStats.PlayerStats("Wiley")

for i in range(RUNS):
    game = Game.Game("Archibald", "Wiley", gsrNoSupportPlayer.gsrNoSupportPlayer, Player, p1stats, p2stats)
    winner = game.play_game()
    winner_list.append(winner)
    if i % 100 == 0:
        print i, "runs done...."

print "=" * 20
print "Archibald wins: %s" % winner_list.count("Archibald")
print "Wiley wins: %s" % winner_list.count("Wiley")
print "Ties: %s" % winner_list.count("Tie!")


'''
print p2stats.get_average_cards_trashed()

print p2stats.get_average_money_output()

print p2stats.get_average_coppers_trashed()
print p2stats.get_average_estates_trashed()
'''
#print p2stats.get_open_number_hit_percentage()
#print p2stats.get_open_number_hit_twice_percentage()
__author__ = 'breppert'

import Game
from Players import *
from Player import *
from MetaSim import PlayerStats

winner_list = []

p1stats = PlayerStats.PlayerStats("Archibald")
p2stats = PlayerStats.PlayerStats("Wiley")

for i in range(RUNS):
    game = Game.Game("Archibald", "Wiley", Player, CardTestingPlayer.CardTestingPlayer, p1stats, p2stats)
    winner = game.play_game()
    winner_list.append(winner)
    if i % 100 == 0:
        print i, "runs done...."

print "=" * 20
print "Jacker wins: %s" % winner_list.count("Archibald")
print "Mariner wins: %s" % winner_list.count("Wiley")
print "Ties: %s" % winner_list.count("Tie!")
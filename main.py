__author__ = 'breppert'

import Game
from Players import *

winner_list = []

for i in range(1000):
    game = Game.Game("Jacker", "Amuleteer", JackPlayer.JackPlayer, AmuletPlayer.AmuletPlayer)
    winner = game.play_game()
    winner_list.append(winner)
    if i % 100 == 0:
        print i, "runs done...."

print "=" * 20
print "Jacker wins: %s" % winner_list.count("Jacker")
print "Amuleteer wins: %s" % winner_list.count("Amuleteer")
print "Ties: %s" % winner_list.count("Tie!")
__author__ = 'breppert'

import Game
from Players import *
from Player import *

winner_list = []

for i in range(1):
    game = Game.Game("Jacker", "Mariner", SentryPlayer.SentryPlayer, Player)
    winner = game.play_game()
    winner_list.append(winner)
    if i % 100 == 0:
        print i, "runs done...."

print "=" * 20
print "Jacker wins: %s" % winner_list.count("Jacker")
print "Mariner wins: %s" % winner_list.count("Mariner")
print "Ties: %s" % winner_list.count("Tie!")
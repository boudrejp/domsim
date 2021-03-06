__author__ = 'breppert'

from Player import Player
from CardImpls.Generics import *
from random import choice
from Config import *
from Supply import *
from Players import *


class Game:
    '''
    Contains everything needed for a two player game of Dominion
    '''

    def __init__(self, player_one_name, player_two_name, player_one_class, player_two_class, player_one_stats, player_two_stats, starting_cards_one = None, starting_cards_two = None, force_starting_hand = None):
        self.__setup__(player_one_name, player_two_name, player_one_class, player_two_class, player_one_stats, player_two_stats, starting_cards_one, starting_cards_two, force_starting_hand)
        self.supply = Supply()
        self.turn_number = 1
        self.trash = []


    def play_game(self, first_player = None, stop_on_turn = None):
        if first_player is None:
            players_turn = choice([1,2])
        else:
            players_turn = first_player
        first_player = players_turn
        players_played_this_turn = 0
        while (not self.game_is_over()):
            if players_turn == 1:
                if LOGGING:
                    print "\n%s's turn (%d):" % (self.player_one.player_name, self.turn_number)
                self.player_one.play_turn()
                players_turn = 2
            elif players_turn == 2:
                if LOGGING:
                    print "\n%s's turn (%d):" % (self.player_two.player_name, self.turn_number)
                self.player_two.play_turn()
                players_turn = 1

            players_played_this_turn += 1
            if players_played_this_turn >= 2:
                self.turn_number += 1
                players_played_this_turn = 0

            if stop_on_turn is None:
                pass
            elif self.turn_number >= stop_on_turn:
                return

        winner = self.get_winner(first_player, players_played_this_turn)
        return winner



    def game_is_over(self):
        if len(self.supply.supply_piles["Province"]) == 0 or len(self.supply.supply_piles["Colony"]) == 0:
            return True

        empty_piles = 0
        for pile in self.supply.supply_piles:
            if len(self.supply.supply_piles[pile]) == 0:
                empty_piles += 1

        if empty_piles >= 3:
            return True

        return False

    def get_winner(self, first_player, players_played_this_turn):
        if LOGGING:
            print ""
            print "%s: %d VP" % (self.player_one.player_name, self.player_one.get_total_vp())
            print "%s: %d VP" % (self.player_two.player_name, self.player_two.get_total_vp())

        if self.player_one.get_total_vp() > self.player_two.get_total_vp():
            winner = self.player_one.player_name
        else:
            winner = self.player_two.player_name

        #Ties
        if self.player_one.get_total_vp() == self.player_two.get_total_vp():
            if players_played_this_turn == 0:
                winner = "Tie!"
            else:
                if first_player == 1:
                    winner = self.player_two.player_name
                else:
                    winner = self.player_one.player_name

        if LOGGING:
            print "Winner: %s!" % (winner)

        if LOGGING:
            print "\n%s's deck" % self.player_one.player_name
            self.player_one.print_deck_contents()
            print "\n%s's deck" % self.player_two.player_name
            self.player_two.print_deck_contents()

        return winner


    def get_starting_cards(self):
        starting_cards = []
        for i in range(7):
            starting_cards.append(Copper.Copper())
        for i in range(3):
            starting_cards.append(Estate.Estate())

        return starting_cards

    def __setup__(self, player_one_name, player_two_name, player_one_class, player_two_class, player_one_stats, player_two_stats, starting_cards_one, starting_cards_two, force_starting_hand):
        self.Trash = []
        if starting_cards_one is None:
            self.player_one = player_one_class(self, player_one_name, self.get_starting_cards(), player_one_stats, force_starting_hand)
        else:
            self.player_one = player_one_class(self, player_one_name, starting_cards_one, player_one_stats, force_starting_hand)
        if starting_cards_two is None:
            self.player_two = player_two_class(self, player_two_name, self.get_starting_cards(), player_two_stats, force_starting_hand)
        else:
            self.player_two = player_two_class(self, player_two_name, starting_cards_two, player_two_stats, force_starting_hand)

        self.player_one.add_opposing_player(self.player_two)
        self.player_two.add_opposing_player(self.player_one)
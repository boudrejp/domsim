__author__ = 'breppert'

from Card import *
from Config import *

def do_merchant(player):
    if player.turn_info.first_silver_played == False:
        merchants_in_play = map(lambda x: x.get_name(), player.play_area).count("Merchant")
        player.turn_info.add_money(merchants_in_play)
        player.turn_info.first_silver_played = True


def do_groundskeeper(player, bought_card):
    if Card.VICTORY in bought_card.get_types():
        groundskeepers_in_play = map(lambda x: x.get_name(), player.play_area).count("Groundskeeper")
        player.victory_chips += groundskeepers_in_play
        if LOGGING:
            if groundskeepers_in_play > 0:
                print "%s Takes %d VP Chips from Groundskeeper" % (player.player_name, groundskeepers_in_play)

def do_haggler(player, bought_card):
    hagglers_in_play = map(lambda x: x.get_name(), player.play_area).count("Haggler")
    for i in range(hagglers_in_play):
        gain_up_to = bought_card.get_cost(reduction = player.turn_info.get_reduction(bought_card.get_types())) - 1
        card_to_gain = player.get_card_to_buy(gain_up_to, 1, True, "Haggler")
        player.gain_card(card_to_gain, "discard")

def do_goons(player):
    goons_in_play = map(lambda x: x.get_name(), player.play_area).count("Goons")
    player.victory_chips += goons_in_play
    if LOGGING:
        if goons_in_play > 0:
            print "%s Takes %d VP Chips from Goons" % (player.player_name, goons_in_play)
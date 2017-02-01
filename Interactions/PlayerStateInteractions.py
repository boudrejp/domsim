__author__ = 'breppert'

def do_merchant(player):
    if player.turn_info.first_silver_played == False:
        merchants_in_play = map(lambda x: x.get_name(), player.play_area).count("Merchant")
        player.turn_info.add_money(merchants_in_play)
        player.turn_info.first_silver_played = True
__author__ = 'breppert'

from Card import Card
from Util.SupplyAnalyzer import *

class Mine(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Mine"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        #Potential TODO: Support gaining kingdom treasures
        player.turn_info.actions -= 1
        cards_in_hand_by_name = player.get_cards_in_hand_by_name()
        treasures_in_hand = map(lambda x: True if Card.TREASURE in x.get_types() else False, player.hand)

        if True in treasures_in_hand:
            if "Gold" in cards_in_hand_by_name and "Platinum" in game.supply.supply_piles.keys():
                card_to_trash = player.hand[cards_in_hand_by_name.index("Gold")]
                card_to_gain = "Platinum"
            elif "Copper" in cards_in_hand_by_name:
                card_to_trash = player.hand[cards_in_hand_by_name.index("Copper")]
                card_to_gain = "Silver"
            elif "Silver" in cards_in_hand_by_name:
                card_to_trash = player.hand[cards_in_hand_by_name.index("Silver")]
                card_to_gain = "Gold"
            else:
                #Do nothing
                return
        else:
            return

        #TODO: Safeguard pile sizes and the such
        cards_to_gain_ladder = ["Platinum", "Gold", "Silver", "Copper"]

        player.trash_card(card_to_trash, "hand")
        player.gain_card(card_to_gain, "hand")






    def is_terminal(self):
        return True


    def card_goodness(self):
        return 2

    def get_categories(self):
        return [Card.GAINER]
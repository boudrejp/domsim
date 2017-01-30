__author__ = 'breppert'

from Card import Card
from CardImpls.Helper import discard_card_from_hand
from Util.HandHelper import *
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *

class Amulet(Card):
    def __init__(self):
        self.duration_finished = False

    PROVINCE_ECONOMY = 18

    def get_name(self):
        return "Amulet"


    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.ACTION, Card.DURATION]


    def play_card(self, game, player, opposing_player):
        self.duration_finished = False
        player.turn_info.actions -= 1
        money_this_turn = get_treasures_dollars_in_hand(player.hand) + player.turn_info.money
        cards_in_hand_by_name = player.get_cards_in_hand_by_name()

        #Trashing Estate always, unless we're hitting 7 while greening
        if "Estate" in cards_in_hand_by_name and not (money_this_turn == 7 and get_total_economy(player) >= Amulet.PROVINCE_ECONOMY):
            card_position_to_trash = cards_in_hand_by_name.index("Estate")
            card_to_trash = player.hand[card_position_to_trash]
            player.trash_card(card_to_trash, "hand")
        #Taking Dollars
        elif money_this_turn == 5 and get_pile_size("Province", game.supply) > 5: ##  Add a dollar to hit 6 if we don't want duchy
            player.turn_info.add_money(1)
        elif money_this_turn == 7 and get_total_economy(player) >= Amulet.PROVINCE_ECONOMY: ##  Add a dollar to hit 8 if we're greening
            player.turn_info.add_money(1)
        #Gain silver (don't trash a copper) if we're exactly on a greening price point
        elif (money_this_turn == 5 and get_pile_size("Province", game.supply) <= 5) \
            or (money_this_turn == 8 and get_total_economy(player) >= Amulet.PROVINCE_ECONOMY):
            player.gain_card("Silver", "discard")
        #Trashing Copper
        #elif money_this_turn != 3 and money_this_turn != 6 and "Copper" in cards_in_hand_by_name: ## Killing a copper if it doesn't knock a treasure price point
        #    card_position_to_trash = cards_in_hand_by_name.index("Copper")
        #    card_to_trash = player.hand[card_position_to_trash]
        #    player.trash_card(card_to_trash, "hand")
        #Gaining Silver
        else:
            player.gain_card("Silver", "discard")

    def duration_card(self, game, player, opposing_player):
        money_in_hand = get_treasures_dollars_in_hand(player.hand)
        another_amulet_in_hand = is_card_in_hand("Amulet", player.hand)
        cards_in_hand_by_name = player.get_cards_in_hand_by_name()

        #Trashing Estate always, unless we're hitting 7 while greening
        if "Estate" in cards_in_hand_by_name and not (money_in_hand == 7 and get_total_economy(player) >= Amulet.PROVINCE_ECONOMY):
            card_position_to_trash = cards_in_hand_by_name.index("Estate")
            card_to_trash = player.hand[card_position_to_trash]
            player.trash_card(card_to_trash, "hand")
        #Taking Dollars
        elif money_in_hand == 5 and get_pile_size("Province", game.supply) > 5: ##  Add a dollar to hit 6 if we don't want duchy
            player.turn_info.add_money(1)
        elif money_in_hand == 7 and get_total_economy(player) >= Amulet.PROVINCE_ECONOMY: ##  Add a dollar to hit 8 if we're greening
            player.turn_info.add_money(1)
        #Gain silver (don't trash a copper) if we're exactly on a greening price point
        elif (money_in_hand == 5 and get_pile_size("Province", game.supply) <= 5) \
            or (money_in_hand == 8 and get_total_economy(player) >= Amulet.PROVINCE_ECONOMY):
            player.gain_card("Silver", "discard")
        #Trashing Copper
        #elif money_in_hand != 3 and money_in_hand != 6 and "Copper" in cards_in_hand_by_name: ## Killing a copper if it doesn't knock a treasure price point
        #    card_position_to_trash = cards_in_hand_by_name.index("Copper")
        #    card_to_trash = player.hand[card_position_to_trash]
        #    player.trash_card(card_to_trash, "hand")
        #Gaining Silver
        else:
            player.gain_card("Silver", "discard")

        self.duration_finished = True




    def should_duration(self):
        return not self.duration_finished


    def is_terminal(self):
        return True


    ### Subjective information ###
    def card_goodness(self):
        return 7

    def economy(self):
        return 1

    def get_categories(self):
        return [Card.TRASHER, Card.GAINER, Card.ECONOMY]
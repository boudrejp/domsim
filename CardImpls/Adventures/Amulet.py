__author__ = 'breppert'

from Card import Card
from Util.HandHelper import *
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *
from CardImpls.Helper import *

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


    def play_card(self, game, player, opposing_player, play_type = "Money"):
        self.duration_finished = False
        player.turn_info.actions -= 1
        money_this_turn = get_treasures_dollars_in_hand(player.hand) + player.turn_info.money
        cards_in_hand_by_name = player.get_cards_in_hand_by_name()

        if play_type == "Money" or play_type == "None":
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
        elif play_type == "Engine":
            if get_total_cards_wanted_to_trash_from_hand(self, player) >= 1:
                trash_card_from_hand(self, player, True)
            elif get_total_economy(player) <= 5:
                player.gain_card("Silver", "discard")
            else:
                player.turn_info.add_money(1)

    def duration_card(self, game, player, opposing_player, play_type = "Money"):
        #Potential TODO is to make the duration logic more complicated (i.e. plan to play both Amulets for coin if one in hand)
        money_in_hand = get_treasures_dollars_in_hand(player.hand)
        another_amulet_in_hand = is_card_in_hand("Amulet", player.hand)
        cards_in_hand_by_name = player.get_cards_in_hand_by_name()

        self.play_card(game, player, opposing_player, play_type)
        player.turn_info.actions += 1

        self.duration_finished = True



    def trashes_from_hand(self, player):
        return 1

    def should_duration(self):
        return not self.duration_finished


    def is_terminal(self):
        return True

    def trashes_coppers(self):
        return True

    def trashes_estates(self):
        return True


    ### Subjective information ###
    def card_goodness(self):
        return 7

    def economy(self):
        return 1

    def get_categories(self):
        return [Card.TRASHER, Card.GAINER, Card.ECONOMY]
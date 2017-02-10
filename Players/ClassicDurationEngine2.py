__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class ClassicDurationEngine2(Player):
    def __init__(self, game, player_name, starting_cards, player_stats):
        super(ClassicDurationEngine2, self).__init__(game,  player_name, starting_cards, player_stats)


    def get_card_to_buy(self, money, buys, forced = False, gain_type = "Normal", potions = 0):
        supply = self.game.supply

        need_more_village = True if (get_terminals(self) / 2 - get_villages(self)) > 0 else False
        need_more_draw = True if (get_total_cards(self) - get_total_draw(self)) > 3 else False

        #print "Draw deficit: ", (get_total_cards(self) - get_total_draw(self))

        #print "Needs more village: ", need_more_village
        #print "Needs more draw: ", need_more_draw

        if gain_type == "Normal":
            ignore_debt = False
        else:
            ignore_debt = True


        if self.can_buy("Junk Dealer", money, ignore_debt) and (cards_in_deck("Junk Dealer", self) < 1):
            return "Junk Dealer"
        elif self.can_buy("Province", money, ignore_debt) and (get_terminals(self) > 7 or get_pile_size("Wharf", supply) == 0): #and self.should_green_with_province():
            return "Province"
        elif self.can_buy("Duchy", money, ignore_debt) and get_pile_size("Province", supply) <= 5 and (get_terminals(self) > 5 or get_pile_size("Wharf", supply) == 0):
            return "Duchy"
        elif self.can_buy("Estate", money, ignore_debt) and get_pile_size("Province", supply) <= 1 and (get_terminals(self) > 5 or get_pile_size("Wharf", supply) == 0):
            return "Estate"
        elif self.can_buy("Wharf", money, ignore_debt) and need_more_draw:
            return "Wharf"
        elif self.can_buy("Gold", money, ignore_debt) and need_more_village == False:
            return "Gold"
        elif self.can_buy("Militia", money, ignore_debt) and cards_in_deck("Militia", self) == 0:
            return "Militia"
        elif self.can_buy("Fishing Village", money, ignore_debt) and (need_more_village or cards_in_deck("Fishing Village", self) < 1 or cards_in_deck("Militia", self) >= 1):
            return "Fishing Village"
        elif self.can_buy("Silver", money, ignore_debt):
            return "Silver"
        else:
            if forced and self.can_buy("Copper", money, ignore_debt):
                return "Copper"
            else:
                return None

    def should_green_with_province(self):
        #PPR -- If we can't take the lead by more than 6, don't take the second to last one
        score_difference = self.get_total_vp() - self.opposing_player.get_total_vp()
        total_points_to_score = 0
        provinces_left = get_pile_size("Province", self.game.supply)
        provinces_left_original = provinces_left
        duchies_left = get_pile_size("Duchy", self.game.supply)
        estates_left = get_pile_size("Estate", self.game.supply)

        tmp_turn_money = self.turn_info.money

        buying_provinces = True
        while (buying_provinces):
            if provinces_left > 0 and tmp_turn_money >= 8:
                total_points_to_score += 6
                provinces_left -= 1
                tmp_turn_money -= 8
            else:
                buying_provinces = False

        buying_duchies = True
        while (buying_duchies):
            if duchies_left > 0 and tmp_turn_money >= 5:
                total_points_to_score += 3
                duchies_left -= 1
                tmp_turn_money -= 5
            else:
                buying_duchies = False

        buying_estates = True
        while (buying_estates):
            if estates_left > 0 and tmp_turn_money >= 2:
                total_points_to_score += 1
                estates_left -= 1
                tmp_turn_money -= 2
            else:
                buying_estates = False



        #Logic for when to lower the province pile to 1
        if provinces_left_original == 2 and provinces_left == 1: #This is the number of provinces left after maximum buying
            if score_difference + total_points_to_score <= 6:
                if True:
                    print "Not buying province on purpose!"
                    print "Duchies left", duchies_left
                    print "My score: %d, his score: %d, provinces left: %d, my money this turn: %d, points this turn: %d" % (
                        self.get_total_vp(), self.opposing_player.get_total_vp(), provinces_left_original, self.turn_info.money,
                        total_points_to_score
                    )
                return False

        return True
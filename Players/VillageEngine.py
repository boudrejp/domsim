__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class VillageEngine(Player):
    def __init__(self, game, player_name, starting_cards, player_stats, force_starting_hand):
        super(VillageEngine, self).__init__(game,  player_name, starting_cards, player_stats, force_starting_hand)


    def get_card_to_buy(self, money, buys, forced = False, gain_type = "Normal", potions = 0):
        supply = self.game.supply

        need_more_village = True if (get_terminals(self) - get_villages(self)) > 0 else False
        need_more_draw = True if (get_total_cards(self) - get_total_draw(self)) > 2 else False
        need_more_plus_buy = True if get_total_economy(self) > 8 and get_plus_buy(self) == 0 else False
        if not need_more_plus_buy:
            need_more_plus_buy = True if get_total_economy(self) > 8 and (get_total_economy(self) / get_plus_buy(self) > 5) else False

        #print "Draw deficit: ", (get_total_cards(self) - get_total_draw(self))

        #print "Needs more village: ", need_more_village
        #print "Needs more draw: ", need_more_draw

        if gain_type == "Normal":
            ignore_debt = False
        else:
            ignore_debt = True

        draw_card = "Smithy"
        trashing_card = "Doctor"
        village_card = "Village"
        plus_buy_card = "Market"
        copies_of_trasher = 1


        if self.can_buy(trashing_card, money, ignore_debt) and cards_in_deck(trashing_card, self) < copies_of_trasher and get_junk_cards(self) > 4 and money > 3:
            self.turn_info.set_overpay(10000)
            return trashing_card
        elif self.can_buy("Junk Dealer", money, ignore_debt) and cards_in_deck("Junk Dealer", self) < copies_of_trasher and get_junk_cards(self) > 4 and money > 3:
            return "Junk Dealer"
        elif self.can_buy("Province", money, ignore_debt) and ((get_terminals(self) > 7 or get_pile_size(draw_card, supply) == 0) or (get_total_economy(self) > 16)): #and self.should_green_with_province():
            return "Province"
        elif self.can_buy("Duchy", money, ignore_debt) and get_pile_size("Province", supply) <= 5 and get_total_economy(self) > 16:
            return "Duchy"
        elif self.can_buy("Estate", money, ignore_debt) and get_pile_size("Province", supply) <= 1:
            return "Estate"
        elif self.can_buy(draw_card, money, ignore_debt) and need_more_draw and not need_more_village:
            return draw_card
        elif self.can_buy(plus_buy_card, money, ignore_debt) and (need_more_plus_buy):
            return plus_buy_card
        elif self.can_buy("Gold", money, ignore_debt) and need_more_village == False:
            return "Gold"
        elif self.can_buy(village_card, money, ignore_debt) and (need_more_village) and cards_in_deck("Silver", self) >= 2:
            return village_card
        elif self.can_buy("Silver", money, ignore_debt) and cards_in_deck("Silver", self) < 3:
            return "Silver"
        elif self.can_buy(village_card, money, ignore_debt):
            return village_card
        else:
            if forced and self.can_buy("Copper", money, ignore_debt):
                return "Copper"
            else:
                return None
__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class StandardEngine(Player):
    def __init__(self, game, player_name, starting_cards, player_stats):
        super(StandardEngine, self).__init__(game,  player_name, starting_cards, player_stats)


    def get_card_to_buy(self, money, buys, forced = False, gain_type = "Normal", potions = 0):
        supply = self.game.supply

        need_more_village = True if (get_terminals(self) - get_villages(self)) > -1 else False
        need_more_draw = True if (get_total_cards(self) - get_total_draw(self)) > 2 else False

        #print "Draw deficit: ", (get_total_cards(self) - get_total_draw(self))

        #print "Needs more village: ", need_more_village
        #print "Needs more draw: ", need_more_draw

        if gain_type == "Normal":
            ignore_debt = False
        else:
            ignore_debt = True

        draw_card = "Smithy"
        trashing_card = "Chapel"
        village_card = "Worker's Village"
        single_play_payload_card = "Militia"


        if self.can_buy(trashing_card, money, ignore_debt) and cards_in_deck(trashing_card, self) < 1 and get_junk_cards(self) > 4 and (self.game.turn_number != 1 or self.turn_info.money <= 3):
            return trashing_card
        elif self.can_buy("Province", money, ignore_debt) and ((get_terminals(self) > 7 or get_pile_size(draw_card, supply) == 0) or (get_total_economy(self) > 16)): #and self.should_green_with_province():
            return "Province"
        elif self.can_buy("Duchy", money, ignore_debt) and get_pile_size("Province", supply) <= 5 and (get_terminals(self) > 5 or get_pile_size(draw_card, supply) == 0):
            return "Duchy"
        elif self.can_buy("Estate", money, ignore_debt) and get_pile_size("Province", supply) <= 1 and (get_terminals(self) > 5 or get_pile_size(draw_card, supply) == 0):
            return "Estate"
        elif self.can_buy(draw_card, money, ignore_debt) and need_more_draw and cards_in_deck(single_play_payload_card, self) != 0:
            return draw_card
        elif self.can_buy("Gold", money, ignore_debt) and need_more_village == False:
            return "Gold"
        elif self.can_buy(single_play_payload_card, money, ignore_debt) and cards_in_deck(single_play_payload_card, self) == 0:
            return single_play_payload_card
        elif self.can_buy(village_card, money, ignore_debt) and (need_more_village):
            return village_card
        elif self.can_buy("Silver", money, ignore_debt):
            return "Silver"
        else:
            if forced and self.can_buy("Copper", money, ignore_debt):
                return "Copper"
            else:
                return None
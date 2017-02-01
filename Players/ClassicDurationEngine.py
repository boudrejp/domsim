__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class ClassicDurationEngine(Player):
    def __init__(self, game, player_name, starting_cards):
        super(ClassicDurationEngine, self).__init__(game,  player_name, starting_cards)


    def get_card_to_buy(self, money, buys, forced = False):
        supply = self.game.supply

        need_more_village = True if (get_terminals(self) / 2 - get_villages(self)) > 0 else False
        need_more_draw = True if (get_total_cards(self) - get_total_draw(self)) > 3 else False

        #print "Draw deficit: ", (get_total_cards(self) - get_total_draw(self))

        #print "Needs more village: ", need_more_village
        #print "Needs more draw: ", need_more_draw


        if self.can_buy("Junk Dealer", money) and cards_in_deck("Junk Dealer", self) < 1:
            return "Junk Dealer"
        elif self.can_buy("Province", money) and get_terminals(self) > 7:
            return "Province"
        elif self.can_buy("Duchy", money) and get_pile_size("Province", supply) <= 5 and get_terminals(self) > 5:
            return "Duchy"
        elif self.can_buy("Wharf", money) and need_more_draw:
            return "Wharf"
        elif self.can_buy("Gold", money) and need_more_village == False:
            return "Gold"
        elif self.can_buy("Fishing Village", money) and (need_more_village or cards_in_deck("Fishing Village", self) < 1 or cards_in_deck("Militia", self) >= 1):
            return "Fishing Village"
        elif self.can_buy("Militia", money) and cards_in_deck("Militia", self) == 0:
            return "Militia"
        elif self.can_buy("Silver", money):
            return "Silver"
        else:
            if forced and self.can_buy("Copper", money):
                return "Copper"
            else:
                return None
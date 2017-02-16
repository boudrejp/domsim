__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class SeaEngine(Player):
    def __init__(self, game, player_name, starting_cards, player_stats, force_starting_hand):
        super(SeaEngine, self).__init__(game,  player_name, starting_cards, player_stats, force_starting_hand)


    def get_card_to_buy(self, money, buys, forced = False, gain_type = "Normal", potions = 0):
        supply = self.game.supply

        if gain_type == "Normal":
            ignore_debt = False
        else:
            ignore_debt = True


        if self.can_buy("Province", money, ignore_debt) and get_total_economy(self) > 18 and (get_pile_size("Province", supply) <= 8 or get_pile_size("Ghost Ship", supply) == 0):
            return "Province"
        elif self.can_buy("Duchy", money, ignore_debt) and get_pile_size("Province", supply) <= 5:
            return "Duchy"
        elif self.can_buy("Ghost Ship", money, ignore_debt) and cards_in_deck("Ghost Ship", self) < 7 and cards_in_deck("Fishing Village", self) > cards_in_deck("Ghost Ship", self) - 1:
            return "Ghost Ship"
        elif self.can_buy("Gold", money, ignore_debt) and get_pile_size("Fishing Village", supply) == 0:
            return "Gold"
        elif self.can_buy("Sea Hag", money, ignore_debt) and cards_in_deck("Sea Hag", self) < 1:
            return "Sea Hag"
        elif self.can_buy("Warehouse", money, ignore_debt) and cards_in_deck("Warehouse", self) < 2 and cards_in_deck("Lighthouse", self) > cards_in_deck("Warehouse", self):
            return "Warehouse"
        elif self.can_buy("Lighthouse", money, ignore_debt) and cards_in_deck("Lighthouse", self) < 4 and cards_in_deck("Lighthouse", self) <= cards_in_deck("Fishing Village", self):
            return "Lighthouse"
        elif self.can_buy("Fishing Village", money, ignore_debt):
            return "Fishing Village"
        elif self.can_buy("Silver", money, ignore_debt):
            return "Silver"
        else:
            if forced and self.can_buy("Copper", money, ignore_debt):
                return "Copper"
            else:
                return None
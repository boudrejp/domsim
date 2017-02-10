__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class CardTestingPlayer(Player):
    def __init__(self, game, player_name, starting_cards, player_stats):
        super(CardTestingPlayer, self).__init__(game,  player_name, starting_cards, player_stats)


    def get_card_to_buy(self, money, buys, forced = False, gain_type = "Normal", potions = 0):
        supply = self.game.supply

        if gain_type == "Normal":
            ignore_debt = False
        else:
            ignore_debt = True


        if self.can_buy("Doctor", money, ignore_debt, potions) and cards_in_deck("Doctor", self) < 1 and self.turn_info.money >= 4:
            self.turn_info.set_overpay(1000)
            return "Doctor"
        if self.can_buy("Province", money, ignore_debt) and get_total_economy(self) > 11:
            return "Province"
        elif self.can_buy("Duchy", money, ignore_debt) and get_pile_size("Province", supply) <= 5:
            return "Duchy"
        elif self.can_buy("Gold", money, ignore_debt):
            return "Gold"
        elif self.can_buy("Explorer", money, ignore_debt):
            return "Explorer"
        elif self.can_buy("Warehouse", money, ignore_debt) and cards_in_deck("Warehouse", self) < 1:
            return "Warehouse"
        #elif self.can_buy("Village", money, ignore_debt) and cards_in_deck("Village", self) < 1:
        #    return "Village"
        #elif self.can_buy("Workshop", money, ignore_debt) and cards_in_deck("Workshop", self) < 1:
        #    return "Workshop"
        elif self.can_buy("Ironworks", money, ignore_debt) and cards_in_deck("Ironworks", self) < 1 and cards_in_deck("Silver", self) != 0:
            return "Ironworks"
        elif self.can_buy("Chariot Race", money, ignore_debt) and cards_in_deck("Silver", self) != 0:
            return "Chariot Race"
        elif self.can_buy("Herald", money, ignore_debt) and cards_in_deck("Silver", self) != 0:
            return "Herald"
        elif self.can_buy("Silver", money, ignore_debt):
            return "Silver"
        else:
            if forced and self.can_buy("Copper", money, ignore_debt):
                return "Copper"
            else:
                return None
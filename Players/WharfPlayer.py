__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class WharfPlayer(Player):
    def __init__(self, game, player_name, starting_cards, player_stats):
        super(WharfPlayer, self).__init__(game,  player_name, starting_cards, player_stats)


    def get_card_to_buy(self, money, buys, forced = False, gain_type = "Normal", potions = 0):
        supply = self.game.supply

        if gain_type == "Normal":
            ignore_debt = False
        else:
            ignore_debt = True

        if self.can_buy("Wharf", money, ignore_debt) and cards_in_deck("Wharf", self) < 3:
            return "Wharf"
        elif self.can_buy("Province", money, ignore_debt) and get_total_economy(self) >= 18:
            return "Province"
        elif self.can_buy("Duchy", money, ignore_debt) and get_pile_size("Province", supply) <= 5:
            return "Duchy"
        elif self.can_buy("Gold", money, ignore_debt):
            return "Gold"
        elif self.can_buy("Silver", money, ignore_debt):
            return "Silver"
        else:
            if forced and self.can_buy("Copper", money, ignore_debt):
                return "Copper"
            else:
                return None
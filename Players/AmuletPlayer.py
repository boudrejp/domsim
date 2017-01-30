__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class AmuletPlayer(Player):
    def __init__(self, game, player_name, starting_cards):
        super(AmuletPlayer, self).__init__(game,  player_name, starting_cards)


    def get_card_to_buy(self, money, buys, forced = False):
        supply = self.game.supply

        if self.can_buy("Amulet", money) and cards_in_deck("Amulet", self) < 2:
            return "Amulet"
        elif self.can_buy("Province", money) and get_total_economy(self) >= 18:
            return "Province"
        elif self.can_buy("Duchy", money) and get_pile_size("Province", supply) <= 5:
            return "Duchy"
        elif self.can_buy("Gold", money):
            return "Gold"
        elif self.can_buy("Silver", money):
            return "Silver"
        else:
            if forced and self.can_buy("Copper", money):
                return "Copper"
            else:
                return None
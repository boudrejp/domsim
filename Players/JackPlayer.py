__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class JackPlayer(Player):
    def __init__(self, game, player_name, starting_cards):
        super(JackPlayer, self).__init__(game,  player_name, starting_cards)


    def get_card_to_buy(self, money, buys, forced = False):
        supply = self.game.supply

        if self.can_buy("Jack of All Trades", money) and cards_in_deck("Jack of All Trades", self) < 2:
            return "Jack of All Trades"
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
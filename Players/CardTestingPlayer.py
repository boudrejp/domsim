__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class CardTestingPlayer(Player):
    def __init__(self, game, player_name, starting_cards):
        super(CardTestingPlayer, self).__init__(game,  player_name, starting_cards)


    def get_card_to_buy(self, money, buys, forced = False):
        supply = self.game.supply

        if self.can_buy("Junk Dealer", money) and cards_in_deck("Junk Dealer", self) < 10:
            return "Junk Dealer"
        elif self.can_buy("Province", money):
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
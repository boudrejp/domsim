__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class MoneyMan(Player):
    def __init__(self, game, player_name, starting_cards, player_stats, force_starting_hand):
        super(MoneyMan, self).__init__(game,  player_name, starting_cards, player_stats, force_starting_hand)


    def get_card_to_buy(self, money, buys, forced = False, gain_type = "Normal", potions = 0):
        supply = self.game.supply

        if gain_type == "Normal":
            ignore_debt = False
        else:
            ignore_debt = True


        big_money_card = get_best_bm_card(supply).get_name()

        if self.can_buy(big_money_card, money, ignore_debt) and cards_in_deck(big_money_card, self) < 1:
            return big_money_card
        elif self.can_buy("Province", money, ignore_debt) and get_total_economy(self) >= 18:
            return "Province"
        elif self.can_buy("Duchy", money, ignore_debt) and get_pile_size("Province", supply) <= 5:
            return "Duchy"
        elif self.can_buy("Gold", money, ignore_debt):
            return "Gold"
        elif self.can_buy(big_money_card, money, ignore_debt) and cards_in_deck(big_money_card, self) < 2:
            return big_money_card
        elif self.can_buy("Silver", money, ignore_debt):
            return "Silver"
        else:
            if forced and self.can_buy("Copper", money, ignore_debt):
                return "Copper"
            else:
                return None
__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class gsrNoSupportPlayer(Player):
    def __init__(self, game, player_name, starting_cards, player_stats, force_starting_hand):
        super(gsrNoSupportPlayer, self).__init__(game,  player_name, starting_cards, player_stats, force_starting_hand)


    def get_card_to_buy(self, money, buys, forced = False, gain_type = "Normal", potions = 0):
        supply = self.game.supply

        if gain_type == "Normal":
            ignore_debt = False
        else:
            ignore_debt = True

        silvers_wanted = 4

        if self.can_buy("Province", money, ignore_debt) and get_total_economy(self) >= 18:
            return "Province"
        elif self.can_buy("Gold", money, ignore_debt):
            return "Gold"
        elif self.can_buy("Silk Road", money, ignore_debt) and cards_in_deck("Silver", self) >= silvers_wanted:
            return "Silk Road"
        elif self.can_buy("Duchy", money, ignore_debt) and cards_in_deck("Silver", self) >= silvers_wanted:
            return "Duchy"
        elif self.can_buy("Gardens", money, ignore_debt) and cards_in_deck("Silver", self) >= silvers_wanted:
            return "Gardens"
        elif self.can_buy("Estate", money, ignore_debt) and get_pile_size("Province", supply) <= 2:
            return "Estate"
        elif self.can_buy("Estate", money, ignore_debt) and cards_in_deck("Silk Road", self) >= 4:
            return "Estate"
        elif self.can_buy("Silver", money, ignore_debt):
            return "Silver"
        elif self.can_buy("Estate", money, ignore_debt):
            return "Estate"
        elif self.can_buy("Copper", money, ignore_debt):
            return "Copper"
        else:
            if forced and self.can_buy("Copper", money, ignore_debt):
                return "Copper"
            else:
                return None

    def get_play_instruction(self, card):
        if card.get_name() == "Amulet":
            return "Money"
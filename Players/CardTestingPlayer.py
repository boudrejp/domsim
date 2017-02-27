__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *


class CardTestingPlayer(Player):
    def __init__(self, game, player_name, starting_cards, player_stats, force_starting_hand):
        super(CardTestingPlayer, self).__init__(game,  player_name, starting_cards, player_stats, force_starting_hand)


    def get_card_to_buy(self, money, buys, forced = False, gain_type = "Normal", potions = 0):
        supply = self.game.supply

        if gain_type == "Normal":
            ignore_debt = False
        else:
            ignore_debt = True

        if not ignore_debt:
            tokens_to_use = 0
            if money < 8 and money >= 6 and money + self.coin_tokens >= 8 and get_total_economy(self) >= 18:
                #For Province
                tokens_to_use = 8 - money
            if money < 8 and money + self.coin_tokens >= 8 and get_total_economy(self) >= 20:
                #For Province
                tokens_to_use = 8 - money
            elif money < 5 and money + self.coin_tokens >= 5 and get_pile_size("Province", supply) <= 5:
                #For Duchy
                tokens_to_use = 5 - money
            elif money == 4 and money + self.coin_tokens >= 5 and get_pile_size("Province", supply) >= 8:
                # For another Baker on early $4 hands
                tokens_to_use = 1

            self.use_coin_tokens(tokens_to_use)

            money = self.turn_info.money



        if self.can_buy("Province", money, ignore_debt) and get_total_economy(self) >= 18:
            return "Province"
        elif self.can_buy("Duchy", money, ignore_debt) and get_pile_size("Province", supply) <= 5:
            return "Duchy"
        elif self.can_buy("Estate", money, ignore_debt) and get_pile_size("Province", supply) <= 2:
            return "Estate"
        elif self.can_buy("Baker", money, ignore_debt) and cards_in_deck("Baker", self) < 1:
            return "Baker"
        elif self.can_buy("Gold", money, ignore_debt):
            return "Gold"
        elif self.can_buy("Baker", money, ignore_debt):
            return "Baker"
        elif self.can_buy("Silver", money, ignore_debt):
            return "Silver"
        else:
            if forced and self.can_buy("Copper", money, ignore_debt):
                return "Copper"
            else:
                return None

    def get_play_instruction(self, card):
        if card.get_name() == "Amulet":
            return "Money"
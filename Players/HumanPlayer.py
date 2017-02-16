__author__ = 'breppert'

from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *
from Util import *

class HumanPlayer(Player):
    def __init__(self, game, player_name, starting_cards, player_stats, force_starting_hand):
        super(HumanPlayer, self).__init__(game,  player_name, starting_cards, player_stats, force_starting_hand)


    def get_card_to_buy(self, money, buys, forced = False, gain_type = "Normal", potions = 0):
        supply = self.game.supply

        if gain_type == "Normal":
            ignore_debt = False
        else:
            ignore_debt = True

        valid_card_to_buy = False

        while not valid_card_to_buy:
            info_string = ""
            if forced or gain_type != "Normal":
                if forced:
                    info_string += "forced gain from %s" % gain_type
                else:
                    info_string += "non-forced gain from %s" % gain_type

            if potions != 0:
                info_string += ", %d Potions" % potions

            if self.turn_info.get_reduction([Card.ACTION]) > 0:
                info_string += ", Cards cost %d less" % self.turn_info.get_reduction([Card.ACTION])


            print "$%d, %d buys, %s" % (money, buys, info_string)
            card_to_buy = raw_input("Select card to buy: ").strip()

            if "supply" == card_to_buy.lower():
                supply.print_supply()
                continue

            if "score" == card_to_buy.lower():
                print "My VP: %d" % self.get_total_vp()
                print "Opponent's VP: %d" % self.opposing_player.get_total_vp()
                continue

            if "overpay" in card_to_buy.lower():
                overpay_amount = int(card_to_buy.split()[1])
                self.turn_info.set_overpay(overpay_amount)
                continue

            if "opp" in card_to_buy.lower() and "deck" in card_to_buy.lower():
                self.opposing_player.print_deck_contents()
                continue

            if "deck" in card_to_buy.lower():
                self.print_deck_contents()
                continue



            if card_to_buy == "":
                if not forced:
                    return None
                else:
                    print "You must select a card to gain because %s!" % gain_type
            else:
                if self.can_buy(card_to_buy, money, ignore_debt, potions):
                    return card_to_buy
                else:
                    print "You can not buy %s! Try again..." % (card_to_buy)


    def get_action_card_to_play_next(self):
        action_cards = PlayHelper.get_actions_that_can_be_played_usefully(self)

        cards_to_play_first = PlayHelper.get_cards_to_play_first(action_cards)
        doublers = PlayHelper.get_throne_variants(action_cards)
        villages = PlayHelper.get_villages(action_cards)
        cantrips = PlayHelper.get_cantrips(action_cards)
        non_terminal_draw = PlayHelper.get_non_terminal_draw(action_cards)
        terminal_draw = PlayHelper.get_terminal_draw(action_cards)
        terminal_payload = PlayHelper.get_terminal_payload(action_cards)
        sifters = PlayHelper.get_sifters(action_cards)
        gainers = PlayHelper.get_gainers(action_cards)
        from_deck_sifters = PlayHelper.get_from_deck_sifters(action_cards)
        nonterminal_actions = PlayHelper.get_nonterminal_actions(action_cards)

        #current basic play order:
        # 0) Sifters that sift the deck
        # 1) non-terminal draw
        # 2) villages
        # 3) terminal draw, if you have the actions for it to not be dead
        # 4) cantrips
        # 5) sifters (non-terminal)
        # 6) terminal payload
        # 7) dead terminal draw
        # 8) any other actions

        action_to_play = None
        if len(cards_to_play_first) >= 1:
            action_to_play = get_max_goodness(cards_to_play_first)
        elif len(doublers) >= 1:
            action_to_play = get_max_goodness(doublers)
        elif len(from_deck_sifters) >= 1:
            action_to_play = get_max_goodness(from_deck_sifters)
        elif len(non_terminal_draw) >= 1:
            action_to_play = get_max_goodness(non_terminal_draw)
        elif len(villages) >= 1:
            action_to_play = get_max_goodness(villages)
        elif len(cantrips) >= 1:
            action_to_play = get_max_goodness(cantrips)
        elif self.turn_info.actions >= 2 and len(terminal_draw) >= 1:
            action_to_play = get_max_goodness(terminal_draw)
        elif len(nonterminal_actions) >= 1:
            action_to_play = get_max_goodness(nonterminal_actions)
        elif len(sifters) >= 1:
            action_to_play = get_max_goodness(sifters)
        elif len(terminal_payload) >= 1:
            action_to_play = get_max_goodness(terminal_payload)
        elif len(gainers) >= 1:
            action_to_play = get_max_goodness(gainers)
        elif len(terminal_draw) >= 1:
            action_to_play = get_max_goodness(terminal_draw)
        elif len(action_cards) >= 1:
            action_to_play = get_max_goodness(action_cards)


        return action_to_play, "Engine"
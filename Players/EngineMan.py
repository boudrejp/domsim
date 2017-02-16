__author__ = 'breppert'
from Player import Player

from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *

class EngineMan(Player):
    def __init__(self, game, player_name, starting_cards, player_stats, force_starting_hand):
        super(EngineMan, self).__init__(game,  player_name, starting_cards, player_stats, force_starting_hand)


    def get_card_to_buy(self, money, buys, forced = False, gain_type = "Normal", potions = 0):
        supply = self.game.supply

        num_stop_cards = get_stop_cards(self)
        total_draw = get_total_draw(self)
        total_cards = len(self.get_all_cards())
        villages = get_villages(self)
        terminals = get_terminals(self)
        junk_cards = get_junk_cards(self)
        total_trashing = get_total_trashing(self)
        total_economy = get_total_economy(self)



        if DEEP_LOGGING:
            print "Total cards: ", total_cards
            print "Total draw: ", total_draw
            print "Stop cards: ", num_stop_cards
            print "Crap cards: ", junk_cards
            print "Villages: ", villages
            print "Terminals: ", terminals

        villages_priority = 0
        terminal_draw_priority = 0
        nonterminal_draw_priority = 0
        economy_priority = 0
        trashing_priority = 0
        cantrip_economy_priority = 0

        terminal_space = villages - terminals + 1

        if terminals >= 1 and terminal_space <= 1:
            villages_priority = (terminals - villages) * 10
        if total_cards - total_draw > 5:
            if terminal_space >= 1:
                terminal_draw_priority = (total_cards - total_draw) + 5
            nonterminal_draw_priority = (total_cards - total_draw) + 3

        trashing_priority = (junk_cards * 2) - (total_trashing * 4)


        #Only try to add economy/payload if over-drawing
        if total_cards - total_draw < 5:
            if total_cards - total_draw >= 0:
                economy_priority = (5 - (total_cards - total_draw)) * 4
            else:
                economy_priority = 20

        #Also, fine to add economy at the beginning of the game
        if total_economy <= 15:
            economy_priority = 22 - total_economy

        cantrip_economy_priority = economy_priority - 5


        if (DEEP_LOGGING):
            print "Village Priority: ", villages_priority
            print "Terminal Draw Priority: ", terminal_draw_priority
            print "Nonterminal Draw Priority: ", nonterminal_draw_priority
            print "Economy Priority: ", economy_priority
            print "Trashing Priority: ", trashing_priority


        #Generate card scores for all known buyable cards (TODO: Generalize this)
        buyable_cards = self.game.supply.supply_piles.keys()
        card_wantingness_scores = []
        for i, card in enumerate(buyable_cards):
            card_wantingness_scores.append(-1)
            if self.can_buy(card, money):
                card_obj = self.game.supply.supply_piles[card][0]
                categories = card_obj.get_categories()
                if Card.POINTS in categories:
                    if card == "Province":
                        card_wantingness_scores[i] = 27
                    elif card == "Duchy" and  get_pile_size("Province", supply) <= 5:
                        card_wantingness_scores[i] = 20 + (5 - get_pile_size("Province", supply))
                if Card.TERMINAL_DRAW in categories:
                    card_wantingness_scores[i] = terminal_draw_priority + (card_obj.card_goodness() * 1.5)
                if Card.NONTERMINAL_DRAW in categories:
                    card_wantingness_scores[i] = nonterminal_draw_priority + (card_obj.card_goodness() * 1.5)
                if Card.VILLAGE in categories:
                    card_wantingness_scores[i] = villages_priority + (card_obj.card_goodness() * 2.5)
                if Card.ECONOMY in categories:
                    card_wantingness_scores[i] = economy_priority + (card_obj.card_goodness() * 1.5)
                if Card.TRASHER in categories:
                    card_wantingness_scores[i] = trashing_priority + (card_obj.card_goodness() * 0.2)
                if card_obj.is_cantrip() and Card.ECONOMY in categories:
                    card_wantingness_scores[i] = cantrip_economy_priority + (card_obj.card_goodness() * 2)

        if DEEP_LOGGING:
            print buyable_cards
            print card_wantingness_scores

        card_wanted_most_score = max(card_wantingness_scores)
        if card_wanted_most_score == -1: #We don't want any of those cards
            return None
        else:
            card_wanted_most_position = card_wantingness_scores.index(card_wanted_most_score)
            card_wanted_most = buyable_cards[card_wanted_most_position]
            return card_wanted_most
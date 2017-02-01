__author__ = 'breppert'

from random import shuffle
from copy import deepcopy
from TurnInfo import TurnInfo
from Util import PlayHelper
from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *

class Player(object):
    '''
    Contains the deck, discard, hand, and (various) set aside cards for a player
    '''

    def __init__(self, game, player_name, starting_cards):
        self.game = game
        self.player_name = player_name
        self.deck = starting_cards
        shuffle(self.deck)
        self.discard = []
        self.hand = []
        self.play_area = []
        self.duration_area = []

        self.draw_starting_hand()
        self.turn_info = TurnInfo()

        self.opposing_player = None

    def add_opposing_player(self, opposing_player):
        self.opposing_player = opposing_player

    def play_turn(self):
        if LOGGING:
            print "Starting hand:", self.print_hand()


        self.play_action_phase()
        self.play_buy_phase()
        self.cleanup()

    def reveal_cards(self, num_to_reveal):
        """
        Returns the revealed cards. Expects the caller of this method to deal with all clean-up of the revealed cards
        """
        revealed_cards = []
        for i in range(num_to_reveal):
            if len(self.deck) == 0: #shuffle in discard
                self.deck = deepcopy(self.discard)
                shuffle(self.deck)
                self.discard = []
            if len(self.deck) >= 1: #already shuffled in discard
                revealed_cards.append(self.deck[0])
                self.deck = self.deck[1:]

                if LOGGING:
                    print "%s Revealing %s" % (self.player_name, revealed_cards[-1].get_name())
        return revealed_cards


    def play_durations(self):
        for card in self.duration_area:
            if LOGGING:
                print "Duration: %s" % card.get_name()
            card.duration_card(self.game, self, self.opposing_player)

    def play_action_phase(self):
        self.play_durations()

        while (self.turn_info.actions >= 1):
            action_cards = PlayHelper.get_actions(self.hand)
            if len(action_cards) == 0:
                return
            else:
                action_to_play = self.get_action_card_to_play_next()
                if action_to_play is not None:
                    self.play_card(action_to_play)


    def get_action_card_to_play_next(self):
        action_cards = PlayHelper.get_actions(self.hand)

        villages = PlayHelper.get_villages(self.hand)
        cantrips = PlayHelper.get_cantrips(self.hand)
        non_terminal_draw = PlayHelper.get_non_terminal_draw(self.hand)
        terminal_draw = PlayHelper.get_terminal_draw(self.hand)
        terminal_payload = PlayHelper.get_terminal_payload(self.hand)
        sifters = PlayHelper.get_sifters(self.hand)

        #current basic play order:
        # 1) non-terminal draw
        # 2) villages
        # 3) terminal draw, if you have the actions for it to not be dead
        # 4) cantrips
        # 5) sifters (non-terminal)
        # 6) terminal payload
        # 7) dead terminal draw
        # 8) any other actions

        action_to_play = None

        if len(non_terminal_draw) >= 1:
            action_to_play = non_terminal_draw[0]
        elif len(villages) >= 1:
            action_to_play = villages[0]
        elif self.turn_info.actions >= 2 and len(terminal_draw) >= 1:
            action_to_play = terminal_draw[0]
        elif len(cantrips) >= 1:
            action_to_play = cantrips[0]
        elif len(sifters) >= 1:
            action_to_play = sifters[0]
        elif len(terminal_payload) >= 1:
            action_to_play = terminal_payload[0]
        elif len(terminal_draw) >= 1:
            action_to_play = terminal_draw[0]
        elif len(action_cards) >= 1:
            action_to_play = action_cards[0]

        return action_to_play


    def play_buy_phase(self):
        # Play treasures
        treasures = PlayHelper.get_treasures(self.hand)
        for treasure in treasures:
            self.play_card(treasure)

        self.buy_cards()

    def buy_cards(self):
        supply = self.game.supply


        card_to_buy = ""
        if (LOGGING):
            print "{ $%d and %d buys }" % (self.turn_info.money, self.turn_info.buys)
        while (self.turn_info.buys >= 1 and card_to_buy is not None):
            card_to_buy = self.get_card_to_buy(self.turn_info.money, self.turn_info.buys)
            if card_to_buy is not None:
                self.buy_card(card_to_buy)





    def get_card_to_buy(self, money, buys, forced = False):
        supply = self.game.supply

        while (self.turn_info.buys >= 1):
            if self.can_buy("Province", money) and get_total_economy(self) >= 18:
                return "Province"
            elif self.can_buy("Duchy", money) and get_pile_size("Province", supply) <= 5:
                return "Duchy"
            elif self.can_buy("Gold", money):
                return "Gold"
            elif self.can_buy("Silver", money):
                return "Silver"
            else:
                if forced:
                    if self.can_buy("Copper", money):
                        return "Copper"
                    elif self.can_buy("Estate", money):
                        return "Estate"
                    elif self.can_buy("Curse", money):
                        return "Curse"
                else:
                    return None



    def can_buy(self, name, money):
        if name in self.game.supply.supply_piles.keys() and len(self.game.supply.supply_piles[name]) >= 1:
            card = self.game.supply.supply_piles[name][0]
            cost = card.get_cost(reduction=self.turn_info.get_reduction(card.get_types()))
            if money >= cost:
                return True
            else:
                return False
        else:
            return False



    def buy_card(self, card_name):
        purchased_card = self.game.supply.supply_piles[card_name][0]

        if (LOGGING):
            print "Buying: %s" % purchased_card.get_name()

        purchased_card.do_on_buy(self.game, self, self.opposing_player)

        self.gain_card(card_name)

        self.turn_info.buys -= 1
        self.turn_info.money -= purchased_card.get_cost(reduction=self.turn_info.get_reduction(purchased_card.get_types()))

    def topdeck_card(self, card):
        if LOGGING:
            print "%s Topdecking %s" % (self.player_name, card.get_name())
        self.deck = [card] + self.deck

    def gain_card(self, card_name, location = "discard"):
        if len(self.game.supply.supply_piles[card_name]) == 0:
            return
        else:
            gained_card = self.game.supply.supply_piles[card_name][0]

            card_was_gained_normally = gained_card.do_on_gain(self.game, self, self.opposing_player)
            if (card_was_gained_normally):
                if LOGGING:
                    print "%s Gaining: %s" % (self.player_name, gained_card.get_name())
                if location == "discard":
                    self.discard.append(gained_card)
                elif location == "topdeck":
                    self.topdeck_card(gained_card)
                elif location == "hand":
                    self.hand.append(gained_card)

            #Post-gain, remove the card from the supply
            self.game.supply.supply_piles[card_name] = self.game.supply.supply_piles[card_name][1:]


    def cleanup(self):
        self.print_all_areas()

        self.turn_info.reset()

        self.cleanup_durations()

        for card in self.play_area:
            card.discard_from_play_effects(self.game, self, self.opposing_player)

        while(len(self.play_area)) > 0:
            self.discard.append(self.play_area[0])
            self.play_area.remove(self.play_area[0])

        while len(self.hand) > 0:
            if DEEP_LOGGING:
                print "Cleanup discarding: %s" % self.hand[0].get_name()
            self.discard.append(self.hand[0])
            self.hand.remove(self.hand[0])

        self.draw_starting_hand()

    def cleanup_durations(self):
        cards_to_move_to_duration_area = []
        for card in self.play_area:
            if card.should_duration():
                cards_to_move_to_duration_area.append(card)

        cards_to_discard_from_duration = []
        for card in self.duration_area:
            if not card.should_duration():
                cards_to_discard_from_duration.append(card)

        for card in cards_to_move_to_duration_area:
            self.play_area.remove(card)
            self.duration_area.append(card)

        for card in cards_to_discard_from_duration:
            self.duration_area.remove(card)
            self.discard.append(card)

        if DEEP_LOGGING:
            print "Moving cards from play area to duration:", map(lambda x: x.get_name(), cards_to_move_to_duration_area)
            print "Discarding cards from duration area because they're done:", map(lambda x: x.get_name(), cards_to_discard_from_duration)


    def play_card(self, card):
        if LOGGING:
            print "Playing: %s " % card.get_name()
        self.hand.remove(card)
        card.play_card(self.game, self, self.opposing_player)
        self.play_area.append(card)

    def blocks_attacks(self):
        """
        TODO: Return True if Moat in hand (and revealed), or Champion down
        """
        if map(lambda x: x.get_name(), self.hand).count("Moat") >= 1:
            return True
        return False

    def print_hand(self):
        return map(lambda x: x.get_name(), self.hand)

    def print_all_areas(self):
        def map_names(x):
            return x.get_name()
        if DEEP_LOGGING:
            print "Hand: ", self.print_hand()
            print "Deck: ", map(map_names, self.deck)
            print "Discard: ", map(map_names, self.discard)
            print "Play Area: ", map(map_names, self.play_area)

    def draw_card(self, during_cleanup = False):
        if len(self.deck) == 0: #shuffle in discard
            self.deck = deepcopy(self.discard)
            shuffle(self.deck)
            self.discard = []
        if len(self.deck) >= 1: #already shuffled in discard
            self.hand.append(self.deck[0])
            self.deck = self.deck[1:]

            if not during_cleanup and LOGGING:
                print "%s Drawing %s" % (self.player_name, self.hand[-1].get_name())

            return True
        else:
            return False

    def draw_starting_hand(self):
        for i in range(5):
            self.draw_card(during_cleanup=True)


    def trash_card(self, card, location = "hand"):
        should_trash = card.on_trash(self.game, self, self.opposing_player)
        if should_trash:
            if LOGGING:
                print "%s Trashing %s" % (self.player_name, card.get_name())
            if location == "hand":
                self.hand.remove(card)
            elif location == "deck":
                ## This means it's a revealed card, and it is the responsibility of the caller to not put the card back anywhere
                pass

            self.game.trash.append(card)

    def discard_card(self, card, location = "hand"):
        should_discard = card.on_discard(self.game, self, self.opposing_player)
        if should_discard:
            if LOGGING:
                print "%s Discarding %s" % (self.player_name, card.get_name())
            if location == "hand":
                self.hand.remove(card)
            elif location == "deck":
                # It is a revealed card, and the responsibility of the caller to not perform shenanigans
                pass

            self.discard.append(card)


    def get_all_cards(self):
        return self.hand + self.deck + self.discard + self.play_area + self.duration_area


    def get_total_vp(self):
        all_cards = self.get_all_cards()
        vp_counter = 0
        for card in all_cards:
            vp_counter += card.get_victory_points(self, self.opposing_player)
        return vp_counter

    def get_cards_in_hand_by_name(self):
        return map(lambda x: x.get_name(), self.hand)

    def print_deck_contents(self):
        unique_cards = []
        for card in self.get_all_cards():
            if card.get_name() not in unique_cards:
                unique_cards.append(card.get_name())
        deck_card_names = map(lambda x: x.get_name(), self.get_all_cards())
        for card in unique_cards:
            card_count = deck_card_names.count(card)
            print "%s: %d" % (card, card_count)
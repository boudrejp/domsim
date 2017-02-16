__author__ = 'breppert'

from random import shuffle
from copy import deepcopy
from TurnInfo import TurnInfo
from Util import PlayHelper
from Config import *
from Util.SupplyAnalyzer import *
from Util.DeckAnalyzer import *
from Interactions.PlayerStateInteractions import *
from MetaSim import PlayerStats


from CardImpls.Base import *
from CardImpls.Seaside import *
from CardImpls.Adventures import * #Temporary hackery

class Player(object):
    '''
    Contains the deck, discard, hand, and (various) set aside cards for a player
    '''

    def __init__(self, game, player_name, starting_cards, player_stats, force_starting_hand = None):
        self.game = game
        self.player_name = player_name
        self.deck = starting_cards
        shuffle(self.deck)
        self.discard = []
        self.hand = []
        self.play_area = []
        self.duration_area = []
        self.set_aside_area = []

        self.victory_chips = 0
        self.debt = 0

        self.draw_starting_hand(force_starting_hand=force_starting_hand)
        self.turn_info = TurnInfo()

        self.opposing_player = None

        self.meta_stats = player_stats
        self.meta_stats.start_new_game()

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
        self.resolve_set_aside_area()
        self.play_durations()

        while (self.turn_info.actions >= 1):
            action_cards = PlayHelper.get_actions(self.hand)
            if len(action_cards) == 0:
                return
            else:
                action_to_play, play_instruction = self.get_action_card_to_play_next()
                if action_to_play is not None:
                    self.play_card(action_to_play, play_instruction)
                else:
                    break

    def resolve_set_aside_area(self):
        for card in self.set_aside_area:
            card.call_from_set_aside(self.game, self, self.opposing_player)

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


        return action_to_play, None


    def play_buy_phase(self):
        # Play treasures
        treasures = PlayHelper.get_treasures(self.hand)
        for treasure in treasures:
            if Card.ATTACK in treasure.get_types():
                self.react_opposing_hand("Attack")
            self.play_card(treasure, None)

        self.buy_cards()


    def buy_cards(self):
        card_to_buy = ""
        if LOGGING:
            print "{ $%d and %d buys }" % (self.turn_info.money, self.turn_info.buys)
        self.meta_stats.add_money_output(self.turn_info.money)
        while self.turn_info.buys >= 1 and card_to_buy is not None:
            self.pay_off_debt()
            card_to_buy = self.get_card_to_buy(self.turn_info.money, self.turn_info.buys, False, "Normal", self.turn_info.potions)
            if card_to_buy is not None:
                self.buy_card(card_to_buy)


    def pay_off_debt(self):
        debt_to_pay_off = 0
        if self.debt > 0:
            if self.turn_info.money > 0:
                if self.debt <= self.turn_info.money:
                    debt_to_pay_off = self.debt
                else:
                    debt_to_pay_off = self.turn_info.money
            else:
                return

        if LOGGING and debt_to_pay_off > 0:
            print "%s paying off %s debt (%d remaining)..." % (self.player_name, debt_to_pay_off, self.debt - debt_to_pay_off)

        self.debt -= debt_to_pay_off
        self.turn_info.money -= debt_to_pay_off


    def get_card_to_buy(self, money, buys, forced = False, gain_type = "Normal", potions = 0):
        '''
        Forced means that you have to buy something with the $ you've been given (i.e. Haggler or Workshop)
        gain_type can be passed in order to tell the recipient what type of logic to use, i.e. "Ironworks"
        '''
        supply = self.game.supply


        if gain_type == "Normal":
            ignore_debt = False
        else:
            ignore_debt = True


        while (self.turn_info.buys >= 1):
            if self.can_buy("Province", money, ignore_debt) and get_total_economy(self) >= 18:
                return "Province"
            elif self.can_buy("Duchy", money, ignore_debt) and get_pile_size("Province", supply) <= 5:
                return "Duchy"
            elif self.can_buy("Estate", money, ignore_debt) and get_pile_size("Province", supply) <= 2:
                return "Estate"
            elif self.can_buy("Gold", money, ignore_debt):
                return "Gold"
            elif self.can_buy("Silver", money, ignore_debt):
                return "Silver"
            else:
                if forced:
                    if self.can_buy("Copper", money, True):
                        return "Copper"
                    elif self.can_buy("Estate", money, True):
                        return "Estate"
                    elif self.can_buy("Curse", money, True):
                        return "Curse"
                    else:
                        return None
                else:
                    return None



    def can_buy(self, name, money, ignore_debt = False, potions = 0):
        if not ignore_debt and self.debt > 0:
            return False


        if name in self.game.supply.supply_piles.keys() and len(self.game.supply.supply_piles[name]) >= 1:
            card = self.game.supply.supply_piles[name][0]
            cost = card.get_cost(reduction=self.turn_info.get_reduction(card.get_types()))
            potion_cost = card.get_potion_cost()

            if ignore_debt: #Okay this is a lame assumption, but if the gain ignores debt, assume that it can't gain a card that has debt
                #Possible TODO is to decouple buy and gain logic more
                if card.get_debt() > 0:
                    return False

            if money >= cost and potions >= potion_cost:
                return True
            else:
                return False
        else:
            return False



    def buy_card(self, card_name):
        purchased_card = self.game.supply.supply_piles[card_name][0]

        if (LOGGING):
            print "Buying: %s" % purchased_card.get_name()
            if purchased_card.get_debt() > 0:
                print "Taking on %s debt...." % purchased_card.get_debt()
                self.debt += purchased_card.get_debt()
                self.pay_off_debt()

        purchased_card_cost = purchased_card.get_cost(reduction=self.turn_info.get_reduction(purchased_card.get_types()))

        overpay_amount = min([self.turn_info.get_overpay(), self.turn_info.money - purchased_card_cost])

        purchased_card.do_on_buy(self.game, self, self.opposing_player)
        if overpay_amount > 0:
            if LOGGING:
                print "Overpaying: $%d" % (overpay_amount)
            purchased_card.do_overpay(self, self.opposing_player, overpay_amount)

        self.do_on_buy_checks(purchased_card)

        if not purchased_card.is_event():
            self.gain_card(card_name)

        self.turn_info.buys -= 1
        self.turn_info.money -= purchased_card_cost
        self.turn_info.potions -= purchased_card.get_potion_cost()
        self.turn_info.set_overpay(0)

    def do_on_buy_checks(self, purchased_card):
        do_haggler(self, purchased_card)
        do_goons(self)


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
                elif location == "set aside":
                    pass

                self.do_on_gain_checks(gained_card)

            #Post-gain, remove the card from the supply
            self.game.supply.supply_piles[card_name] = self.game.supply.supply_piles[card_name][1:]

        return gained_card #If information about the gained card is needed, return it

    def do_on_gain_checks(self, purchased_card):
        do_groundskeeper(self, purchased_card)

    def react_opposing_hand(self, event_type):
        for card in self.opposing_player.hand:
            card.react_card(self.game, self.opposing_player, self, event_type)

    def cleanup(self):
        self.print_all_areas()

        self.turn_info.reset()

        self.meta_stats.add_attacks_in_play(get_attacks_in_play(self))

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


    def get_play_instruction(self, card):
        return None

    def play_card(self, card, play_instruction = None, play_location = "hand"):
        play_instruction = self.get_play_instruction(card)

        if LOGGING:
            print "Playing: %s " % card.get_name()
        if play_location == "hand":
            self.hand.remove(card)

        if play_location != "throned":
            self.play_area.append(card)
        card.play_card(self.game, self, self.opposing_player, play_instruction)


    def blocks_attacks(self):
        """
        TODO: Return True if Moat in hand (and revealed), or Champion down
        """
        if map(lambda x: x.get_name(), self.hand).count("Moat") >= 1:
            return True
        if map(lambda x: x.get_name(), self.duration_area).count("Lighthouse") >= 1:
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

    def draw_starting_hand(self, force_starting_hand = None):
        for i in range(5):
            self.draw_card(during_cleanup=True)

        if force_starting_hand is None:
            pass
        else:
            while (force_starting_hand != self.get_cards_in_hand_by_name().count("Copper")):
                self.deck += self.hand
                self.hand = []
                shuffle(self.deck)
                for i in range(5):
                    self.draw_card(during_cleanup=True)


    def trash_card(self, card, location = "hand"):
        should_trash = card.on_trash(self.game, self, self.opposing_player)
        if should_trash:
            self.meta_stats.increment_trashed_cards()
            if card.get_name() == "Copper":
                self.meta_stats.increment_trashed_coppers()
            elif card.get_name() == "Estate":
                self.meta_stats.increment_trashed_estates()


            if LOGGING:
                print "%s Trashing %s" % (self.player_name, card.get_name())
            if location == "hand":
                self.hand.remove(card)
            elif location == "deck":
                ## This means it's a revealed card, and it is the responsibility of the caller to not put the card back anywhere
                pass
            elif location == "play_area":
                self.play_area.remove(card)

            self.game.trash.append(card)
            return True
        return False

    def discard_card(self, card, location = "hand"):
        if LOGGING:
            print "%s Discarding %s" % (self.player_name, card.get_name())
        if location == "hand":
            self.hand.remove(card)
        elif location == "deck":
            # It is a revealed card, and the responsibility of the caller to not perform shenanigans
            pass

        card.on_discard(self.game, self, self.opposing_player)

        self.discard.append(card)




    def get_all_cards(self):
        return self.hand + self.deck + self.discard + self.play_area + self.duration_area


    def get_total_vp(self):
        all_cards = self.get_all_cards()
        vp_counter = 0
        for card in all_cards:
            vp_counter += card.get_victory_points(self, self.opposing_player)
        return vp_counter + self.victory_chips

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
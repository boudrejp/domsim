__author__ = 'breppert'

class Card (object):
    """
    Interface that can be called for all card interactions/information
    """
    TREASURE = "Treasure"
    ACTION = "Action"
    ATTACK = "Attack"
    REACTION = "Reaction"
    DURATION = "Duration"
    LOOTER = "Looter"
    VICTORY = "Victory"
    CURSE = "Curse"
    RUIN = "Ruin"


    ECONOMY = "Economy"
    VILLAGE = "Village"
    TERMINAL_DRAW = "Terminal Draw"
    NONTERMINAL_DRAW = "Non-terminal Draw"
    GAINER = "Gainer"
    TRASHER = "Trasher"
    POINTS = "Points"
    JUNK = "Junk"
    THRONE_VARIANT = "Throne Variant"
    BUYS = "Buys"
    SIFTER = "Sifter"
    TERMINAL_PAYLOAD_NONSTACKING = "Terminal Payload - Non-stacking"
    TERMINAL_PAYLOAD_STACKING = "Terminal Payload - Stacking"
    JUNKER = "Junker"



    def __init__(self):
        pass

    #### Functions for actual functional play of the cards
    def get_types(self):
        return []

    def get_name(self):
        return ""

    def get_cost(self):
        return 0

    def get_potion_cost(self):
        return 0

    def get_debt(self):
        return 0

    def is_event(self):
        return False

    def can_overpay(self):
        return False

    def do_overpay(self, player, opposing_player, overpay_amount):
        pass

    def get_victory_points(self, player, opposing_player):
        return 0

    def play_card(self, game, player, opposing_player, play_type=None):
        '''
        Once you've decided to play the card, actually plays the card with all play logic.
        You can specify play type for some cards, i.e. the "Engine" option for Sentry will trash more agressively than "Money"
        '''
        pass

    def duration_card(self, game, player, opposing_player):
        pass

    def should_duration(self):
        return False

    def react_card(self, game, player, opposing_player, event_type):
        pass

    def discard_from_play_effects(self, game, player, opposing_player):
        pass

    def do_on_buy(self, game, player, opposing_player):
        pass

    def do_on_gain(self, game, player, opposing_player):
        """
        Returns True if the gain should continue as normal, and False if the card was gained (or not gained)
        elsewhere due to some effects, and so the normal "gain" mechanic should not continue
        """
        return True

    def on_trash(self, game, player, opposing_player):
        ## Returns True if the trash should continue as normal, or False if there were special rules acted out
        return True

    def on_discard(self, game, player, opposing_player):
        ## Returns True if the trash should continue as normal, or False if there were special rules acted out
        return True

    def can_play_for_benefit(self, game, player, opposing_player):
        #Returns True if the card can be usefully played. I.e. Junk Dealer will return False if no junk in hand.
        #Still needs to be implemented on many cards

        #if Card.TERMINAL_DRAW in self.get_categories():
        #    if len(player.deck) + len(player.discard) == 0:
        #        return False

        return True

    def call_from_set_aside(self, game, player, opposing_player):
        pass

    #Some helper functions to help play order
    ####
    def is_terminal(self):
        return False

    def is_village(self):
        return False

    def is_cantrip(self):
        return False

    def is_sifter(self):
        return False

    def draws(self, hand = None):
        return False

    def draws_to_x(self):
        return False

    def junks(self, supply):
        return False

    def trashes_from_hand(self, player):
        return False

    def trashes_from_deck(self, player):
        return False

    def trashes(self):
        return False

    def sifts_from_deck(self):
        return False

    def is_compulsive_trasher(self):
        return False

    def economy(self):
        return 0

    def gains(self):
        return False

    def plus_buys(self):
        return 0

    def should_play_first(self):
        '''
        Cards that benefit from being played early on in turns
        '''
        return False

    def card_goodness(self):
        '''
        Arbitrary, scale of 0-10, not sure if this is actually useful
        '''
        return 0

    def get_categories(self):
        return [] #This is potentially redundant to the above functions, but, uh, it won't hurt.

    def trashes_estates(self):
        return True

    def trashes_coppers(self):
        return True
    ####
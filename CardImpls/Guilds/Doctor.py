__author__ = 'breppert'

from Card import Card
from Util.PlayHelper import *
from CardImpls.Helper.util import *
from Util.SupplyAnalyzer import *
from Config import *


class Doctor(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Doctor"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1

        #Assumes perfect deck tracking, because why not?
        known_cards = []

        def to_names(x):
            return x.get_name()

        if len(player.deck) >= 3:
            search_area = player.deck
        elif len(player.deck) + len(player.discard) <= 3:
            known_cards = map(to_names, player.deck + player.discard)
            search_area = []
        else: # len(player.deck) <= 3:
            known_cards = map(to_names, player.deck)
            search_area = player.discard
        cards_in_search_area_by_name = map(to_names, search_area)

        cards_to_trash = ["Curse", "Estate", "Copper"]
        if get_pile_size("Province", game.supply) <= 2:
            cards_to_trash.remove("Estate")
        parralel_average_trashes = []
        for i in range(len(cards_to_trash)):
            parralel_average_trashes.append(0)


        for i, card in enumerate(cards_to_trash):
            average_trashes = known_cards.count(card)
            if len(cards_in_search_area_by_name) > 0:
                average_trashes += float(cards_in_search_area_by_name.count(card)) / len(cards_in_search_area_by_name) * 3
            if card == "Copper":
                average_trashes *= 0.75 #De-prioritize Copper over other junk
                if get_total_economy(player) - average_trashes < 3: #Don't trash beneath $3
                    average_trashes *= 0

            parralel_average_trashes[i] = average_trashes

        max_average_trash = -1
        max_average_trash_position = 0
        for i, num in enumerate(parralel_average_trashes):
            if num > max_average_trash:
                max_average_trash = num
                max_average_trash_position = i


        card_to_name = cards_to_trash[max_average_trash_position]
        if LOGGING:
            print "%s Naming: %s" % (player.player_name, card_to_name)
        revealed_cards = player.reveal_cards(3)
        cards_to_trash = []
        cards_to_topdeck = []
        for card in revealed_cards:
            if card.get_name() == card_to_name:
                cards_to_trash.append(card)
            else:
                cards_to_topdeck.append(card)

        for card in cards_to_trash:
            player.trash_card(card, "deck")

        topdeck_cards(player, cards_to_topdeck)


    def can_overpay(self):
        return True

    def do_overpay(self, player, opposing_player, overpay_amount):
        for i in range(overpay_amount):
            top_of_deck = player.reveal_cards(1)
            if len(top_of_deck) == 1:
                top_card = top_of_deck[0]
                if want_to_trash_card(self, top_card, player):
                    player.trash_card(top_card, "deck")
                elif i == overpay_amount-1: #This is the last card we're looking at, so top-deck it
                    player.topdeck_card(top_card)
                else: #dig for more cards to trash
                    player.discard_card(top_card, "deck")



    def is_terminal(self):
        return True

    def card_goodness(self):
        return 2

    def get_categories(self):
        return [Card.TRASHER]

    def trashes_coppers(self):
        return True

    def trashes_estates(self):
        return True
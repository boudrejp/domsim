__author__ = 'breppert'

from Card import Card
from Util.HandHelper import *
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *


class JackOfAllTrades(Card):
    def __init__(self):
        pass

    JACK_PROVINCING = 18

    def get_name(self):
        return "Jack of All Trades"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player):
        player.turn_info.actions -= 1

        money_this_turn = get_treasures_dollars_in_hand(player.hand) + player.turn_info.money

        #Gain a silver
        player.gain_card("Silver", "discard")


        #Reveal the top card of your deck, discard or put it back
        cards_in_hand_by_name = map(lambda x: x.get_name(), player.hand)
        estates_in_hand = cards_in_hand_by_name.count("Estate")
        curses_in_hand = cards_in_hand_by_name.count("Estate")

        trashable_junk_in_hand = estates_in_hand + curses_in_hand

        revealed_cards = player.reveal_cards(1)
        if len(revealed_cards) >= 1:
            revealed_card = revealed_cards[0]

            #If nothing to trash in hand and revealed something to trash, keep it
            if trashable_junk_in_hand == 0 and (revealed_card.get_name() == "Estate" or revealed_card.get_name == "Curse"):
                player.topdeck_card(revealed_card)

            #If it's a copper and it helps you hit a price point, keep it.
            elif (revealed_card.get_name() == "Copper") and \
                    (money_this_turn == 7 and get_total_economy(player) >= JackOfAllTrades.JACK_PROVINCING or
                            money_this_turn == 4 and get_pile_size("Province", game.supply) <= 5):
                player.topdeck_card(revealed_card)

            #Otherwise discard unless it's a silver or better
            elif revealed_card.get_name() in ["Copper", "Estate", "Curse"] or Card.ACTION in revealed_card.get_types():
                player.discard_card(revealed_card, "deck")

            else:
                player.topdeck_card(revealed_card)

        #Draw until you have 5 cards in hand
        while (len(player.hand)) < 5:
            drew_a_card = player.draw_card()
            if not drew_a_card:
                break

        cards_in_hand_by_name = map(lambda x: x.get_name(), player.hand)

        #Trash a card from your hand
        for i in range(1):
            trash_target = None
            if "Curse" in cards_in_hand_by_name:
                trash_target = "Curse"
            elif "Estate" in cards_in_hand_by_name:
                trash_target = "Estate"

            for card in player.hand:
                if card.get_name() == trash_target:
                    player.trash_card(card, "hand")
                    break






    ### Subjective Information ###

    def card_goodness(self):
        return 7

    def get_categories(self):
        return [Card.TERMINAL_DRAW, Card.GAINER, Card.TRASHER]
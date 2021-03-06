__author__ = 'breppert'

from Card import Card
from Util.DeckAnalyzer import *
from Util.SupplyAnalyzer import *
from CardImpls.Helper import util


class Sentry(Card):
    TOSS_TERMINALS = False


    def __init__(self):
        pass

    def get_name(self):
        return "Sentry"

    def get_cost(self, reduction = 0):
        return max([0, 5 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type="Money"):
        player.draw_card()

        revealed_cards = player.reveal_cards(2)
        cards_to_put_back = []
        cards_to_discard = []
        for i, card in enumerate(revealed_cards):
            if card.get_name() == "Estate" or card.get_name() == "Curse":
                #In a money game, don't trash Estates any longer if the province pile is below 5
                if play_type == "Money" and card.get_name() == "Estate" and get_pile_size("Province", game.supply) <= 5:
                    cards_to_discard.append(card)
                else:
                    player.trash_card(card, "deck")
            elif card.get_name() == "Copper" and get_total_economy(player) > 4:
                player.trash_card(card, "deck")
            else:
                if Card.VICTORY in card.get_types() and Card.ACTION not in card.get_types():
                    cards_to_discard.append(card)
                else:
                    cards_to_put_back.append(card)

        for card in cards_to_discard:
            player.discard_card(card, "deck")

        util.topdeck_cards(player, cards_to_put_back)

    def sifts_from_deck(self):
        return True

    def draws(self, hand = None):
        return 1

    def is_terminal(self):
        return False

    def card_goodness(self):
        return 7

    def trashes_from_hand(self, player):
        return 0

    def trashes(self):
        return 1.5

    def trashes_from_deck(self, player):
        return 1.5 #TODO: Update this to be an estimate of cards this will trash

    def get_categories(self):
        return [Card.TRASHER, Card.SIFTER]

    def is_cantrip(self):
        return True

    def is_sifter(self):
        return True

    def trashes_estates(self):
        return True

    def trashes_coppers(self):
        return True

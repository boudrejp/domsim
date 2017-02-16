__author__ = 'breppert'

from Card import Card


class Golem(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Golem"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_potion_cost(self):
        return 1

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions -= 1

        cards_to_discard = []
        cards_to_play = []

        revealed_cards = player.reveal_cards(1)
        while len(revealed_cards) != 0 and len(cards_to_play) < 2:
            revealed_card = revealed_cards[0]
            if Card.ACTION in revealed_card.get_types() and revealed_card.get_name() != self.get_name():
                cards_to_play.append(revealed_card)
                if len(cards_to_play) == 2:
                    break
                revealed_cards = player.reveal_cards(1)
            else:
                cards_to_discard.append(revealed_card)
                revealed_cards = player.reveal_cards(1)

        for card in cards_to_discard:
            player.discard_card(card, "deck")

        for card in cards_to_play:
            player.turn_info.actions += 1 #Because I did actions kinda funny, ok?
            player.play_card(card, None, "deck")


    def draws(self, hand = None):
        return 2

    def is_village(self):
        return 1

    def card_goodness(self):
        return 7

    def get_categories(self):
        return [Card.VILLAGE, Card.NONTERMINAL_DRAW]
__author__ = 'breppert'

from Card import Card


class FarmingVillage(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Farming Village"

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        player.turn_info.actions += 1

        revealed_cards = player.reveal_cards(1)
        cards_to_discard = []
        while len(revealed_cards) != 0:
            revealed_card = revealed_cards[0]
            if Card.ACTION in revealed_card.get_types() or Card.TREASURE in revealed_card.get_types():
                player.hand.append(revealed_card)
                break
            else:
                cards_to_discard.append(revealed_card)
                revealed_cards = player.reveal_cards(1)

        for card in cards_to_discard:
            player.discard_card(card, "deck")


    def draws(self, hand = None):
        return 1

    def is_village(self):
        return 1

    def card_goodness(self):
        return 4

    def get_categories(self):
        return [Card.VILLAGE]
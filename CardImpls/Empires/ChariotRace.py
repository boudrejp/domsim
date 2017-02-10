__author__ = 'breppert'

from Card import Card


class ChariotRace(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Chariot Race"

    def get_cost(self, reduction = 0):
        return max([0, 3 - reduction])

    def get_types(self):
        return [Card.ACTION]

    def play_card(self, game, player, opposing_player, play_type = None):
        top_card = None
        opponent_top_card = None
        top_cards = player.reveal_cards(1)
        if len(top_cards) == 1:
            top_card = top_cards[0]

        opponent_top_cards = opposing_player.reveal_cards(1)
        if len(opponent_top_cards) == 1:
            opponent_top_card = opponent_top_cards[0]

        if top_card is not None and opponent_top_card is not None:
            if top_card.get_cost(reduction=player.turn_info.get_reduction(top_card.get_types())) > \
            opponent_top_card.get_cost(reduction=player.turn_info.get_reduction(top_card.get_types())):
                player.turn_info.add_money(1)
                player.victory_chips += 1

        if top_card is not None:
            player.hand.append(top_card)
        if opponent_top_card is not None:
            opposing_player.topdeck_card(opponent_top_card)

    def sifts_from_deck(self):
        return True #Hacky to set this to true, but forces the base bot to play it early

    def is_cantrip(self):
        return True

    def card_goodness(self):
        return 5

    def economy(self):
        return 0.6

    def get_categories(self):
        return [Card.ECONOMY, Card.POINTS]
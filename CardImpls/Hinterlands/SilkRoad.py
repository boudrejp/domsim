__author__ = 'breppert'

from Card import Card

class SilkRoad(Card):
    def __init__(self):
        pass

    def get_name(self):
        return "Silk Road"

    def get_types(self):
        return [Card.VICTORY]

    def get_cost(self, reduction = 0):
        return max([0, 4 - reduction])

    def get_victory_points(self, player, opposing_player):
        return int(self.get_total_victory_cards_in_deck(player) / 4)

    def get_total_victory_cards_in_deck(self, player):
        all_cards =  player.get_all_cards()
        victory_cards = []
        for card in all_cards:
            if Card.VICTORY in card.get_types():
                victory_cards.append(card)
        return len(victory_cards)


    def get_categories(self):
        return [Card.POINTS]
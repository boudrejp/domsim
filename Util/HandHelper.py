__author__ = 'breppert'

def get_treasures_dollars_in_hand(hand):
    '''
    TODO: Variable cost treasures
    '''
    total_money = 0
    for card in hand:
        if card.TREASURE in card.get_types():
            total_money += card.economy()
    return total_money

def is_card_in_hand(card_name, hand):
    '''
    TODO: Variable cost treasures
    '''
    card_names = map(lambda x: x.get_name(), hand)
    if card_name in card_names:
        return True
    return False


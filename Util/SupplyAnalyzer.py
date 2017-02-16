__author__ = 'breppert'

from DeckAnalyzer import *


def get_pile_size(card, supply):
    return len(supply.supply_piles[card])


def get_best_bm_card(supply):
    '''
    Returns the card to play monolithic BM with, will play with
    1) A junker
    2) Terminal draw BM (if it's 3 cards or more)
    3) The other best card on the board
    '''
    junkers = []
    terminal_3_drawers = []
    other_candidates = []

    for pile in supply.supply_piles.keys():
        if len(supply.supply_piles[pile]) >= 1:
            top_card = supply.supply_piles[pile][0]
            if top_card.get_potion_cost() > 0:
                continue

            if Card.JUNKER in top_card.get_categories():
                junkers.append(top_card)
            elif Card.TERMINAL_DRAW in top_card.get_categories() and top_card.draws() >= 3:
                terminal_3_drawers.append(top_card)
            elif Card.ACTION in top_card.get_types():
                other_candidates.append(top_card)

    if len(junkers) > 0:
        return get_max_goodness(junkers)
    elif len(terminal_3_drawers) > 0:
        return get_max_goodness(terminal_3_drawers)
    else:
        return get_max_goodness(other_candidates)
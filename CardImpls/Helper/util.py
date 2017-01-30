__author__ = 'breppert'

from Card import *

def discard_card_from_hand(player):
    '''
    discards cards from the hand
    '''
    if len(player.hand) == 0:
        return False

    cards_by_name = map(lambda x: x.get_name(), player.hand)

    estate_trashes_available = 0
    for card in player.hand:
        if card.trashes() >= 1 and card.trashes_estates() and card.trashes_from_hand(player) >= 1:
            estate_trashes_available = card.trashes()

    victory_card_hand_positions = []
    for i, card in enumerate(player.hand):
        if Card.VICTORY in card.get_types() and Card.ACTION not in card.get_types():
            if "Estate" != card.get_name(): #  Estate logic handled differently
                victory_card_hand_positions.append(i)

    #Discard order:
    # 1) Estate (if no trasher in hand)
    # 2) Other green cards
    # 3) Copper
    # 4) Estate (even if trasher in hand)
    # 5) Silver
    # 6) Random (TODO: discard by card goodness level, terminal availability, etc.)

    if "Estate" in cards_by_name and cards_by_name.count("Estate") > estate_trashes_available:
        discard_position = cards_by_name.index("Estate")
    elif len(victory_card_hand_positions) >= 1:
        discard_position = victory_card_hand_positions[0]
    elif "Copper" in cards_by_name:
        discard_position = cards_by_name.index("Copper")
    elif "Estate" in cards_by_name:
        discard_position = cards_by_name.index("Estate")
    elif "Silver" in cards_by_name:
        discard_position = cards_by_name.index("Silver")
    else:
        discard_position = 0

    player.discard_card(player.hand[discard_position], "hand")

    return True
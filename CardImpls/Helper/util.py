__author__ = 'breppert'

from Card import *

#TODO: Support ruins in these utility functions

def discard_card_from_hand(player):
    '''
    discards cards from the hand
    '''
    if len(player.hand) == 0:
        return False

    cards_by_name = map(lambda x: x.get_name(), player.hand)

    non_treasure_trashes_available = 0
    for card in player.hand:
        if card.trashes() >= 1 and card.trashes_estates() and card.trashes_from_hand(player) >= 1:
            non_treasure_trashes_available += card.trashes()

    non_treasures_in_hand_to_trash = cards_by_name.count("Curse") + cards_by_name.count("Estate")

    victory_card_hand_positions = []
    for i, card in enumerate(player.hand):
        if Card.VICTORY in card.get_types() and Card.ACTION not in card.get_types():
            if "Estate" != card.get_name(): #  Estate logic handled differently
                victory_card_hand_positions.append(i)

    #Discard order:
    # 1) Curse (if no trasher in hand)
    # 2) Estate (if no trasher in hand)
    # 3) Other green cards
    # 4) Copper
    # 5) Estate (even if trasher in hand)
    # 6) Silver
    # 7) Random (TODO: discard by card goodness level, terminal availability, etc.)


    if "Curse" in cards_by_name and non_treasures_in_hand_to_trash > non_treasure_trashes_available:
        discard_position = cards_by_name.index("Curse")
    elif "Estate" in cards_by_name and non_treasures_in_hand_to_trash > non_treasure_trashes_available:
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


def trash_card_from_hand(player, is_forced=False):
    '''
    discards cards from the hand
    '''
    if len(player.hand) == 0:
        return False

    cards_by_name = map(lambda x: x.get_name(), player.hand)

    #Trash order:
    # 1) Curse
    # 2) Estate
    # 3) Copper
    # 4) Silver (only if forced)
    # 5) Random (only if forced) (TODO: trash by card goodness level, terminal availability, etc.)

    trash_position = None

    if "Curse" in cards_by_name:
        trash_position = cards_by_name.index("Estate")
    elif "Estate" in cards_by_name:
        trash_position = cards_by_name.index("Estate")
    elif "Copper" in cards_by_name:
        trash_position = cards_by_name.index("Copper")
    elif "Silver" in cards_by_name and is_forced:
        trash_position = cards_by_name.index("Silver")
    elif is_forced:
        trash_position = 0

    player.trash_card(player.hand[trash_position], "hand")

    return True
__author__ = 'breppert'

from Card import *
from Util.DeckAnalyzer import *

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

    treasure_hand_positions = []
    for i, card in enumerate(player.hand):
        if Card.TREASURE in card.get_types() and Card.ACTION not in card.get_types():
            treasure_hand_positions.append(i)

    village_hand_positions = []
    for i, card in enumerate(player.hand):
        if Card.VILLAGE in card.get_categories():
            village_hand_positions.append(i)


    terminal_draw_hand_positions = []
    for i, card in enumerate(player.hand):
        if Card.TERMINAL_DRAW in card.get_categories():
            terminal_draw_hand_positions.append(i)

    nonterminal_draw_hand_positions = []
    for i, card in enumerate(player.hand):
        if Card.NONTERMINAL_DRAW in card.get_categories():
            nonterminal_draw_hand_positions.append(i)

    stop_card_hand_positions = []
    for i, card in enumerate(player.hand):
        if Card.NONTERMINAL_DRAW not in card.get_categories() and Card.TERMINAL_DRAW not in card.get_categories() and Card.VILLAGE not in card.get_categories() and not card.is_cantrip():
            stop_card_hand_positions.append(i)

    cantrip_card_hand_positions = []
    for i, card in enumerate(player.hand):
        if card.is_cantrip() and Card.NONTERMINAL_DRAW not in card.get_categories():
            cantrip_card_hand_positions.append(i)

    action_card_position_to_discard = None


    #Pitch stop cards, then cantrips
    if len(stop_card_hand_positions) > 0:
        action_card_position_to_discard = stop_card_hand_positions[0]
    elif len(cantrip_card_hand_positions) > 0:
        action_card_position_to_discard = cantrip_card_hand_positions[0]
    # Don't pitch away your last village or draw card, but if you have to, pitch the draw card instead of the village.
    elif len(village_hand_positions) == 1 and len(terminal_draw_hand_positions) > 0:
        action_card_position_to_discard = terminal_draw_hand_positions[0]
    elif len(terminal_draw_hand_positions) == 1 and len(village_hand_positions) > 0:
        action_card_position_to_discard = village_hand_positions[0]
    #If you have more than 1 of each, pitch the draw card
    elif len(village_hand_positions) >= 2 and len(terminal_draw_hand_positions) >= 2:
        action_card_position_to_discard = terminal_draw_hand_positions[0]


    #Discard order:
    # 0) Special interactions (at this point: Tunnel)
    # 1) Curse (if no trasher in hand)
    # 2) Estate (if no trasher in hand)
    # 3) Other green cards
    # 4) Copper
    # 5) Estate (even if trasher in hand)
    # 6) Silver
    # 7) Random Treasure
    # 8) If discarding actions, try to hand on to stuff that will kick off turn (TODO: discard by card goodness level, terminal availability, etc.)

    if "Tunnel" in cards_by_name:
        discard_position = cards_by_name.index("Tunnel")
    elif "Curse" in cards_by_name and non_treasures_in_hand_to_trash > non_treasure_trashes_available:
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
    elif len(treasure_hand_positions) >= 1:
        discard_position = treasure_hand_positions[0]
    elif action_card_position_to_discard is not None:
        discard_position = action_card_position_to_discard
    else:
        discard_position = 0

    player.discard_card(player.hand[discard_position], "hand")

    return True


def trash_card_from_hand(trashing_card, player, is_forced=False):
    '''
    trashes cards from the hand
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

    junk_cards_wanted_to_trash = []
    copper_cards_wanted_to_trash = []
    trasher_cards_wanted_to_trash = []
    if_forced_to_trash_then_trash = None

    for card in player.hand:
        if want_to_trash_card(trashing_card, card, player):
            if Card.TRASHER not in card.get_categories() and "Copper" != card.get_name():
                junk_cards_wanted_to_trash.append(card)
            elif card.get_name() == "Copper":
                copper_cards_wanted_to_trash.append(card)
            else:
                trasher_cards_wanted_to_trash.append(card)


    if "Silver" in cards_by_name and is_forced:
        if_forced_to_trash_then_trash = player.hand[cards_by_name.index("Silver")]
    elif is_forced:
        if_forced_to_trash_then_trash = player.hand[0]

    card_to_trash = None
    if len(junk_cards_wanted_to_trash) > 0:
        card_to_trash = junk_cards_wanted_to_trash[0]
    elif len(copper_cards_wanted_to_trash) > 0 and get_total_economy(player) > 4:
        card_to_trash = copper_cards_wanted_to_trash[0]
    elif len(trasher_cards_wanted_to_trash) > 0:
        card_to_trash = trasher_cards_wanted_to_trash[0]
    elif is_forced:
        card_to_trash = if_forced_to_trash_then_trash

    if card_to_trash is not None:
        player.trash_card(card_to_trash, "hand")
    else:
        return False

    return True


def get_total_cards_wanted_to_trash_from_hand(trashing_card, player):
    hand = player.hand
    cards_to_trash = 0
    for card in hand:
        if want_to_trash_card(trashing_card, card, player):
            cards_to_trash += 1
    return cards_to_trash


def want_to_trash_card(trashing_card, card, player):
    '''
    helper function to determine if you want to trash X card or not
    '''

    if trashing_card.trashes_estates() and (card.JUNK in card.get_types() or "Estate" == card.get_name()):
        return True

    if card.trashes_coppers() and "Copper" == card.get_name() and get_total_economy(player) > 4:
        return True

    if should_trash_trashers(player):
        if trashing_card != card and Card.TRASHER in card.get_categories() and card.get_name() != "Sentry":
            return True

    return False

def should_trash_trashers(player):
    '''
    Given sufficient thin-ness, determines if you should trash your trasher (i.e. 2 Junk Dealers down to 1)
    '''
    total_junk = get_junk_cards(player)
    if total_junk <= 2:
        return True
    else:
        return False

def topdeck_cards(player, cards_to_topdeck):
    if len(cards_to_topdeck) == 0:
        return

    villages_to_topdeck = []
    nonterminal_draw_to_topdeck = []
    cantrips_to_topdeck = []
    terminal_draw_to_topdeck = []
    actions_to_topdeck = []
    treasures_to_topdeck = []
    other_to_dopdeck = []

    for card in cards_to_topdeck:
        if Card.VILLAGE in card.get_categories():
            villages_to_topdeck.append(card)
        elif Card.NONTERMINAL_DRAW in card.get_categories():
            nonterminal_draw_to_topdeck.append(card)
        elif card.is_cantrip():
            cantrips_to_topdeck.append(card)
        elif Card.TERMINAL_DRAW in card.get_categories():
            terminal_draw_to_topdeck.append(card)
        elif Card.ACTION in card.get_categories():
            actions_to_topdeck.append(card)
        elif Card.TREASURE in card.get_categories():
            treasures_to_topdeck.append(card)
        else:
            other_to_dopdeck.append(card)

    topdecking_priorities = [villages_to_topdeck, nonterminal_draw_to_topdeck, cantrips_to_topdeck, terminal_draw_to_topdeck, actions_to_topdeck,
                             treasures_to_topdeck, other_to_dopdeck]

    topdecking_priorities.reverse() # Because of how top-decking works

    for topdeck_list in topdecking_priorities:
        for card in topdeck_list:
            player.topdeck_card(card)
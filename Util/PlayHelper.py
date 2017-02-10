__author__ = 'breppert'

from Card import Card

"""
"hand" in these functions can really mean any set of cards, it will work regardless
"""


def get_actions(hand):
    cards = []
    for card in hand:
        if Card.ACTION in card.get_types():
            cards.append(card)
    return cards

def get_actions_that_can_be_played_usefully(player):
    cards = []
    for card in player.hand:
        if Card.ACTION in card.get_types():
            #  Cards that can't be meaningfully played should not be played
            if not card.can_play_for_benefit(player.game, player, player.opposing_player):
                continue
        cards.append(card)
    return cards


def get_treasures(hand):
    cards = []
    for card in hand:
        if Card.TREASURE in card.get_types():
            cards.append(card)
    return cards

def get_cantrips(hand):
    cantrips = []
    for card in hand:
        if card.is_cantrip():
            cantrips.append(card)
    return cantrips

def get_villages(hand):
    villages = []
    for card in hand:
        if Card.VILLAGE in card.get_categories():
            villages.append(card)
    return villages


def get_max_goodness(cards):
    '''
    Helper for returning the most subjectively good card out of a list of cards.
    This is used to make decisions that are otherwise categorically the same.
    '''
    max_goodness_card = None
    max_goodness_level = -10000
    for card in cards:
        if card.card_goodness() > max_goodness_level:
            max_goodness_card = card
            max_goodness_level = card.card_goodness()
    return max_goodness_card

def get_non_terminal_draw(hand):
    cards = []
    for card in hand:
        if Card.NONTERMINAL_DRAW in card.get_categories():
            cards.append(card)
    return cards

def get_terminal_draw(hand):
    cards = []
    for card in hand:
        if Card.TERMINAL_DRAW in card.get_categories():
            cards.append(card)
    return cards

def get_throne_variants(hand):
    cards = []
    for card in hand:
        if Card.THRONE_VARIANT in card.get_categories():
            cards.append(card)
    return cards

def get_terminal_payload(hand):
    cards = []
    for card in hand:
        if Card.TERMINAL_PAYLOAD_NONSTACKING in card.get_categories() or Card.TERMINAL_PAYLOAD_STACKING in card.get_categories():
            cards.append(card)
    return cards

def get_sifters(hand):
    cards = []
    for card in hand:
        if Card.SIFTER in card.get_categories():
            cards.append(card)
    return cards

def get_gainers(hand):
    cards = []
    for card in hand:
        if Card.GAINER in card.get_categories():
            cards.append(card)
    return cards


def get_from_deck_sifters(hand):
    cards = []
    for card in hand:
        if card.sifts_from_deck():
            cards.append(card)
    return cards
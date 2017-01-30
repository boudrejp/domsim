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
        if card.is_village():
            villages.append(card)
    return villages

def get_non_terminal_draw(hand):
    cards = []
    for card in hand:
        if not card.is_terminal() and card.draws() >= 2:
            cards.append(card)
    return cards

def get_terminal_draw(hand):
    cards = []
    for card in hand:
        if card.is_terminal() and card.draws() and card.draws() >= 1:
            cards.append(card)
    return cards

def get_throne_variants(hand):
    cards = []
    for card in hand:
        if card.is_throne_variant():
            cards.append(card)
    return cards

def get_terminal_payload(hand):
    cards = []
    for card in hand:
        if card.is_terminal() and not card.draws():
            cards.append(card)
    return cards

def get_sifters(hand):
    cards = []
    for card in hand:
        if card.is_sifter():
            cards.append(card)
    return cards
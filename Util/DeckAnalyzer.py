__author__ = 'breppert'

from Card import Card
from PlayHelper import *

def cards_in_deck(name, player):
    return map(lambda x: x.get_name(), player.get_all_cards()).count(name)

def get_total_cards(player):
    return len(player.get_all_cards())

def get_stop_cards(player):
    all_cards = player.get_all_cards()
    def is_stop_card(x):
        if Card.ACTION not in x.get_types():
            return True
        elif not x.is_cantrip() and not x.draws() >= 2 and not x.is_village():
            return True
        else:
            return False

    return sum(map(is_stop_card, all_cards))

def get_junk_cards(player):
    all_cards = player.get_all_cards()
    def is_crap_card(x):
        if Card.RUIN in x.get_types() or Card.CURSE in x.get_types():
            return True
        elif x.get_name() == "Estate" or x.get_name() == "Copper":
            return True
        else:
            return False

    return sum(map(is_crap_card, all_cards))


def get_plus_buy(player):
    all_cards = player.get_all_cards()
    def plus_buy(x):
        return x.plus_buys()

    return sum(map(plus_buy, all_cards))

def get_total_trashing(player):
    all_cards = player.get_all_cards()
    def trashes(x):
        return x.trashes()

    return sum(map(trashes, all_cards))

def get_total_economy(player):
    all_cards = player.get_all_cards()
    def economy(x):
        return x.economy()

    return sum(map(economy, all_cards))


def get_attacks_in_play(player):
    attacks_in_play = 0
    for card in player.play_area:
        if Card.ATTACK in card.get_types():
            attacks_in_play += 1
    return attacks_in_play


def get_total_draw(player):
    ### Does not support draw-to-x, includes how many cards the deck draws in total
    all_cards = player.get_all_cards()
    def get_cards_drawn(x):
        if not x.draws_to_x():
            return x.draws()

    return sum(map(get_cards_drawn, all_cards))

def get_villages(player):
    ### Does not support draw-to-x, includes how many cards the deck draws in total
    all_cards = player.get_all_cards()
    def get_villages(x):
        return x.is_village()

    return sum(map(get_villages, all_cards))

def get_terminals(player):
    ### Does not support draw-to-x, includes how many cards the deck draws in total
    all_cards = player.get_all_cards()
    def get_terminal(x):
        return x.is_terminal()

    return sum(map(get_terminal, all_cards))
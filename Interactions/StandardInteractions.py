__author__ = 'breppert'

def discard_to_block_mountebank(player):
    """
    Will discard a curse from hand in order to block the Mountebank attack
    """
    card_names =  map(lambda x: x.get_name(), player.hand)
    if "Curse" in card_names:
        player.discard_card(player.hand[card_names.index("Curse")])
        return True
    else:
        return False
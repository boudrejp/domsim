
__author__ = 'breppert'


from CardImpls.Generics import *
from CardImpls.Base import *
from CardImpls.Seaside import *
from CardImpls.Prosperity import *
from CardImpls.DarkAges import *
from CardImpls.Adventures import *
from CardImpls.Hinterlands import *
from CardImpls.Intrigue import *
from CardImpls.Empires import *


class State:
    def __init__(self):
        pass

    def get_cards(self):
        all_cards = []


        for i in range(2):
            all_cards.append(Moat.Moat())
        for i in range(1):
            all_cards.append(Silver.Silver())
        for i in range(1):
            all_cards.append(Goons.Goons())


        return all_cards
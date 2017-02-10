
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
            all_cards.append(Curse.Curse())
        for i in range(7):
            all_cards.append(Copper.Copper())
        for i in range(2):
            all_cards.append(Mountebank.Mountebank())
        for i in range(1):
            all_cards.append(Gold.Gold())
        for i in range(2):
            all_cards.append(Silver.Silver())
        for i in range(5):
            all_cards.append(Smithy.Smithy())
        for i in range(6):
            all_cards.append(Festival.Festival())
        for i in range(2):
            all_cards.append(Market.Market())
        for i in range(5):
            all_cards.append(Cartographer.Cartographer())


        return all_cards
__author__ = 'breppert'

from CardImpls.Generics import *
from CardImpls.Base import *
from CardImpls.Seaside import *
from CardImpls.Prosperity import *
from CardImpls.DarkAges import *
from CardImpls.Adventures import *
from CardImpls.Hinterlands import *
from CardImpls.Intrigue import *

class Supply:
    def __init__(self):
        self.supply_piles = {}
        self.__setup_always__()
        self.__setup_kingdom_piles__()

    def __setup_always__(self):
        self._create_pile(8, Estate.Estate())
        self._create_pile(8, Duchy.Duchy())
        self._create_pile(8, Province.Province())

        self._create_pile(30, Gold.Gold())
        self._create_pile(40, Silver.Silver())
        self._create_pile(46, Copper.Copper())

        self._create_pile(10, Curse.Curse())


    def _create_pile(self, number, object):
        self.supply_piles[object.get_name()] = []
        for i in range(number):
            self.supply_piles[object.get_name()].append(object)

    def __setup_kingdom_piles__(self):
        self._create_pile(10, Smithy.Smithy())
        self._create_pile(10, Laboratory.Laboratory())
        self._create_pile(10, Village.Village())
        self._create_pile(10, Chapel.Chapel())
        self._create_pile(10, Market.Market())
        self._create_pile(10, Warehouse.Warehouse())
        self._create_pile(10, Militia.Militia())
        self._create_pile(10, Workshop.Workshop())
        self._create_pile(10, Sentry.Sentry())
        self._create_pile(10, Mountebank.Mountebank())
        self._create_pile(10, Moat.Moat())
        self._create_pile(10, Quarry.Quarry())
        self._create_pile(10, Poacher.Poacher())
        self._create_pile(10, Cellar.Cellar())
        self._create_pile(10, JunkDealer.JunkDealer())
        self._create_pile(10, Amulet.Amulet())
        self._create_pile(10, JackOfAllTrades.JackOfAllTrades())
        self._create_pile(10, Merchant.Merchant())
        self._create_pile(10, Wharf.Wharf())
        self._create_pile(10, Bridge.Bridge())
        self._create_pile(10, FishingVillage.FishingVillage())
        self._create_pile(10, Caravan.Caravan())
        self._create_pile(10, Dungeon.Dungeon())

    def get_non_empty_pile_names(self):
        non_empty_pile_names = []
        for pile_key in self.supply_piles.keys():
            if len(self.supply_piles[pile_key]) >= 1:
                non_empty_pile_names.append(self.supply_piles[pile_key][0].get_name())
        return non_empty_pile_names

    def get_num_empty_piles(self):
        empty_piles = 0
        for pile in self.supply_piles:
            if len(self.supply_piles[pile]) == 0:
                empty_piles += 1
        return empty_piles

    def provinces_or_colonies_empty(self):
        if "Colony" in self.supply_piles.keys():
            if len(self.supply_piles["Colony"]) == 0:
                return True
        if len(self.supply_piles["Province"]) == 0:
            return True
        return False
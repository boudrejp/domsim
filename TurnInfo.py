__author__ = 'breppert'

from Card import Card

class TurnInfo:
    def __init__(self):
        '''
        Contains information like actions, buys, and $'s for this turn
        '''
        self.reset()

    def reset(self):
        self.actions = 1
        self.buys = 1
        self.money = 0
        self.potions = 0

        self.cost_reductions = 0
        self.action_only_cost_reductions = 0

        self.overpay = 0 #Hacky way to handle over-pay where it's state driven
        # I do it this way to avoid cluttering the buying interface

        self.first_silver_played = False

    def add_money(self, amount):
        self.money += amount

    def get_reduction(self, card_types):
        if Card.ACTION in card_types:
            return self.action_only_cost_reductions + self.cost_reductions
        else:
            return self.cost_reductions

    def set_overpay(self, overpay_amount):
        self.overpay = overpay_amount

    def get_overpay(self):
        return self.overpay

    def reset_overpay(self):
        self.overpay = 0
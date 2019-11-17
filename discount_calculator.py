# -*- coding: UTF-8 -*-

from discounts import *

class Discount_calculator(object):

    def calculate(self, budget):

        discount = Discount_per_five_items(
            Discount_per_more_then_five_hundred_reais(
                Without_discount()
                )
            ).Calculate(budget)

        return discount

if __name__ == '__main__':

    from budget import Budget, Item

    budget = Budget()
    budget.add_item(Item('Item - 1', 50))
    budget.add_item(Item('Item - 2', 100))
    budget.add_item(Item('Item - 3', 500))

    print('Value without discount',budget.value)

    calculator = Discount_calculator()
    discount = calculator.calculate(budget)
    final_value = budget.value - discount

    print('Value with discount: ', discount)

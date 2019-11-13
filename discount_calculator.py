# -*- coding: UTF-8 -*-

class Discount_calculator(object):

    def calculate(budget):
        if budget.total_items > 5:
            return budget.value * 0.1
        elif budget.value > 500:
            return budget.value * 0.07

if __name__ == '__main__':

    from budget import Budget, Item

    budget = Budget()
    budget.add_item(Item('Item - 1', 50))
    budget.add_item(Item('Item - 2', 100))
    budget.add_item(Item('Item - 3', 500))

    print(budget.value)

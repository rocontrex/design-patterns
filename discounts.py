# -*- coding: UTF-8 -*-

class Discount_per_five_items(object):
    
    def __init__(self, next_discount):
        self.__next_discount = next_discount
    
    def Calculate(self, budget):
        if budget.total_items >= 5:
            return budget.value * 0.1
        else:
            return self.__next_discount.Calculate(budget)

class Discount_per_more_then_five_hundred_reais(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def Calculate(self, budget):
        if budget.value >= 500:
            return budget.value * 0.07
        else:
            return self.__next_discount.Calculate(budget)

class Without_discount(object):
    def Calculate(self, budget):
        return 0
# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

class TaxC(object):
    
    __metaclass__ = ABCMeta

    def __init__(self, other_tax = None):
        self.__other_tax = other_tax

    def calculate_other_tax(self, budget):
        if self.__other_tax is None:
            return 0
        else:
            return self.__other_tax.calculate(budget)
    
    @abstractmethod
    def calculate(self, budget):
        pass

class Template_of_tax_conditional(TaxC):
    
    __metaclass__ = ABCMeta

    def calculate(self, budget):
        if self.could_use_max_tax(budget):
            return self.max_tax(budget) + self.calculate_other_tax(budget)
        else:
            return self.min_tax(budget) + self.calculate_other_tax(budget)

    @abstractmethod
    def could_use_max_tax(self, budget):
        pass

    @abstractmethod
    def max_tax(self, budget):
        pass

    @abstractmethod
    def min_tax(self, budget):
        pass

class ISS(TaxC):

    def calculate(self, budget):

        return budget.value * 0.1 + self.calculate_other_tax(budget)

class ICMS(TaxC):

    def calculate(self, budget):

        return budget.value * 0.06 + self.calculate_other_tax(budget)

class ICPP(Template_of_tax_conditional):

    def could_use_max_tax(self, budget):
        
        return budget.value > 500
            
    def max_tax(self, budget):
        return budget.value * 0.07

    def min_tax(self, budget):
        return budget.value * 0.05

class IKCV(Template_of_tax_conditional):

    def __has_item_greater_then_hundred_reais(self, budget):

        for item in budget.get_items():
            if item.value > 100:
                return True
        
        return False

    def could_use_max_tax(self, budget):
        
        return budget.value > 500 and self.__has_item_greater_then_hundred_reais(budget)
            
    def max_tax(self, budget):
        
        return budget.value * 0.1

    def min_tax(self, budget):
        
        return budget.value * 0.06

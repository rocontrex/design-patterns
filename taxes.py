# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

class Template_of_tax_conditional(object):
    
    __metaclass__ = ABCMeta

    def calculate(self, budget):
        if self.could_use_max_tax(budget):
            return self.max_tax(budget)
        else:
            return self.min_tax(budget)

    @abstractmethod
    def could_use_max_tax(self, budget):
        pass

    @abstractmethod
    def max_tax(self, budget):
        pass

    @abstractmethod
    def min_tax(self, budget):
        pass

class ISS(object):

    def calculate(self, budget):

        return budget.value * 0.1

class ICMS(object):

    def calculate(self, budget):

        return budget.value * 0.06

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

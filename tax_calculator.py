# -*- coding: UTF-8 -*-
from taxes import *

class Tax_calculator(object):
    def performs_calculation(self, budget, tax):
        calculated_tax = tax.calculate(budget)
        print( calculated_tax )

if __name__ == '__main__':
    from budget import Budget, Item
    
    calculator = Tax_calculator()

    budget = Budget()
    budget.add_item(Item('Item 1 - ', 50))
    budget.add_item(Item('Item 1 - ', 200))
    budget.add_item(Item('Item 1 - ', 250))

    print('ISS and ICMS')
    calculator.performs_calculation(budget, ICMS())
    calculator.performs_calculation(budget, ISS())

    
    print('ICPP and IKCV')
    calculator.performs_calculation(budget, ICPP())
    calculator.performs_calculation(budget, IKCV())
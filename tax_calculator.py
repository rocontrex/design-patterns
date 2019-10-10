from taxes import calculate_ICMS, calculate_ISS

class Tax_calculator(object):

    def performs_calculation(self, budget, tax):
        calculated_tax = tax(budget)
        print( calculated_tax )


if __name__ == '__main__':
    
    from budget import Budget

    calculator = Tax_calculator()

    budget = Budget(500)

    calculator.performs_calculation(budget, calculate_ICMS)
    calculator.performs_calculation(budget, calculate_ISS)
class Tax_calculator(object):

    def performs_calculation(self, budget, tax):
        if tax == 'ISS':
            calculated_tax = budget.value * 0.1
        if tax == 'ICMS':
            calculated_tax = budget.value * 0.6
        print( calculated_tax )


if __name__ == '__main__':
    
    from budget import Budget

    calculator = Tax_calculator()

    budget = Budget(500)

    calculator.performs_calculation(budget, 'ISS')
    calculator.performs_calculation(budget, 'ICMS')
from taxes import calculate_ICMS, calculate_ISS

class Tax_calculator(object):

    def performs_calculation(self, budget, tax):
        if tax == 'ISS':
            calculated_tax = calculate_ISS(budget)
        if tax == 'ICMS':
            calculated_tax = calculate_ICMS(budget)
        print( calculated_tax )


if __name__ == '__main__':
    
    from budget import Budget

    calculator = Tax_calculator()

    budget = Budget(500)

    calculator.performs_calculation(budget, 'ISS')
    calculator.performs_calculation(budget, 'ICMS')
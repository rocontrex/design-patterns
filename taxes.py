# -*- coding: UTF-8 -*-
class ISS(object):

    def calculate(self, budget):

        return budget.value * 0.1

class ICMS(object):

    def calculate(self, budget):

        return budget.value * 0.06
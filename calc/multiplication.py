"""this is the addition calculation that is being inherits the
value A and value B from the calculation class"""

from calc.calculation import Calculation

class Multiplication(Calculation):
    def getresult(self):
        return self.value_a * self.value_b

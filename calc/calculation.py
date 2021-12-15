"""This is our calculation base class / Abstract Class"""
class Calculation:

    def __init__(self,value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b
    # class factory method
    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a,value_b)
    @classmethod
    def print(cls, self):
        print(self.value_a)
        print(self.value_b)
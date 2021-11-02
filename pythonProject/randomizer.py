from numpy import random
from shape import *

# -----------------------------------------
class Randomizer(Shape):
    def __init__(self):
        self.count = 0
    # Handle random input case.
    def Function(self):
        # Creating random number of function.
        self.count = random.randint(1, 10001)
        stroke = ""
        k = 0
        while k < self.count:
            k += 1
            current_number = random.randint(1, 4)
            stroke += str(current_number) + "\n"
            count_string = random.randint(5, 46)
            s = 0
            while s < count_string:
                stroke += chr(random.randint(32, 123))
                s += 1
            stroke += "\n"
        strArray = stroke.split("\n")
        return strArray

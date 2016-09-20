from music21 import *


# todo use the built in float type
# with .numerator and .denominator attributes
class rational:
    def __init__(self):
        self.numerator = 0
        self.denominator = -1

    def getFloat(self):
        return float(self.numerator)/float(self.denominator)

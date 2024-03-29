""" MODULE BORROWED 
https://github.com/Supreme-Sector/Python-Perlin-Noise 
With some minor changes made"""

import random

class Perlin:
    """gradients: random values that are assigned at specific internvals
    frequency: indicates how many values are assigned from 0-100 (evenly spaced)

    """
    def __init__(self, frequency):
        if frequency < 2:
            print("Frequency has to be at least 2")
            return
        self.gradients = []
        self.frequency = frequency
        self.lowerBound = 0
        self.interval_size = 200 / (self.frequency-1)
        self.gradients = [random.uniform(-1, 1) for i in range(frequency)]

    """ Bulk of the algorithm"""
    def valueAt(self, t):
        if t < self.lowerBound:
            print("Error: Input parameter is out of bounds!")
            return

        discarded = int(self.lowerBound / self.interval_size)

        while t >= (len(self.gradients)-1+discarded)*self.interval_size:
            self.gradients.append(random.uniform(-1, 1))

        numOfintervals = int(t / self.interval_size)
        a1 = self.gradients[numOfintervals-discarded]
        a2 = self.gradients[numOfintervals+1-discarded]

        amt = self.__ease((t-numOfintervals*self.interval_size) / self.interval_size)

        return self.__lerp(a1,a2,amt)

    """Discard deletes unneccesasry elements from gradient list and moves upper bound"""
    def discard(self, amount):
        toDiscard = int((amount+self.lowerBound%self.interval_size)/self.interval_size)
        self.gradients = self.gradients[toDiscard:]
        self.lowerBound += amount


    def __ease(self, x):
        return 6*x**5-15*x**4+10*x**3


    """ Linear interpolation here""" 
    def __lerp(self, start, stop, amt):
        return amt*(stop-start)+start
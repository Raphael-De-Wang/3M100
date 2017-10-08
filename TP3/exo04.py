#!/usr/bin/env python

from exo03 import Heron
from exo02 import V

class Poly2(Heron):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.racines = []
        self.alpha   = self.delta(a,b,c)
        self.suite_lst = [self.alpha/2.]

    def delta(self, a, b, c):
        return b**2 - 4 * a * c
        
    def get_racines(self,n):
        a = self.a
        b = self.b
        c = self.c
        if self.alpha < 0 :
            return []
        elif self.alpha == 0 :
            return [ -b / (a * 2.)]
        else :
            alpha = super(V, self).get(n)
            return [ ( -b + alpha ) / (a * 2.), ( -b - alpha ) / (a * 2.)]


# poly2 = Poly2(1,-3,2)
# print poly2.get_racines(10)
# print poly2.suite_lst
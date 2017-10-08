#!/usr/bin/env python

from exo01 import Suite
from exo02 import V

# Algo de Heron
class Heron(V) :
    def __init__(self, alpha):
        self.alpha = alpha
        self.suite_lst = [alpha/2.]

    def next(self,xn): 
        return (xn + self.alpha/xn)/2.

    def get(self,n):
        return super(V, self).get(n)

# heron = Heron(2)
# print heron.get(10)
# print heron.suite_lst

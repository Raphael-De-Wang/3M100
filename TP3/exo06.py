#!/usr/bin/env python

# PGCD
# algorithme d’Euclide

import numpy as np


class PGCD(object):
    def __init__(self, N1, N2):
        self.N1 = N1
        self.N2 = N2
        self.pgcd = self.euclide(N1,N2)

    def euclide(self, N1, N2):
        if N1 < N2 :
            (N1, N2) = (N2, N1)
        if N1 % N2 == 0:
            return N2
        else :
            return self.euclide(N2, N1%N2)



pgcd = PGCD(15,25)
print pgcd.pgcd

#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from population import Population

class Attracteur(object) :
    def __init__(self,L,m,n) :
        self.L = L
        self.m = m
        self.n = n

    def evol(self, mu, x0 = None, m = None, n = None):
        if x0 is None :
            x0 = np.random.rand()
        if m is None :
            m = self.m
        if n is None :
            n = self.n

        p = Population(mu,x0,n)
        em = p.evol()[m:]
        return zip(em[:-1],em[1:])

    def plot_evol(self, mu, x0 = None, m = None, n = None):
        if x0 is None :
            x0 = np.random.rand()
        if m is None :
            m = self.m
        if n is None :
            n = self.n

        em = self.evol(mu,x0,m,n)
        em = np.array(em)
        plt.plot(em[:,0],em[:,1])
        plt.show()

    def plot_evol_marche(self, L, x0 = None, m = None, n = None):
        pass

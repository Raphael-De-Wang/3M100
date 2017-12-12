#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from population import Draw

class Simulation(Draw):
    def __init__(self, pplt, ft = 1):
        self.p = pplt
        self.ft= ft
    
    def draw(self, p=None):
        if p is None :
            p = self.p

        X = np.arange(p.N)
        Y = np.array(p.evol())

        fig = plt.figure(self.ft)
        plt.plot(X,Y,'b',label="x1 = f(x0, mu=" + str(p.mu) + ")")
        plt.xlim(0,p.N)
        plt.ylim(0,1)
        plt.xlabel("Time")
        plt.ylabel("Population")
        return fig
        
class Simulation2(object):

    def evlt(self, x0, mu, N, M):
        Y = [x0]
        for t in range(1,N):
            Y = Y + [self.f(Y[-1],mu)]
        return Y[M-1:]
        
    def draw_evlt(self, ft, x0, mu, N, M):
        Y = np.array(self.evlt(x0,mu,N,M))
        X = np.arange(len(Y)) + M - 1
        fig = plt.figure(ft)
        plt.plot(X,Y,'b',label="x1 = f(x0, mu=" + str(mu) + ")")
        plt.xlim(M-1,N)
        plt.ylim(0,1)
        plt.xlabel("Time")
        plt.ylabel("Population")
        return fig


#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


class Population(object) :
    
    def __init__(self,mu,x0,N):
        if mu >= 0 and mu <= 4 :
            self.mu = mu
        else :
            raise ValueError('The parameter mu should be defined in [0, 4]')
        if x0 >= 0 and x0 <= 1:
            self.x0 = x0
        else :
            raise ValueError('The inital population should be defined in [0, 1] ')
        if N > 0 :
            self.N = N
        else :
            raise ValueError('The time is discrete, should be a positive integer')

    # application logistique
    def f(self, x, mu=None):
        if mu is None :
            mu = self.mu
        return mu * x * (1 - x)

    # evolution
    def evlt(self, x0 = None, mu = None, N = None, M = 0):
        if mu is None :
            mu = self.mu
        if x0 is None :
            x0 = self.x0
        if N is None :
            N = self.N
        
        Y = [x0]
        for t in range(1,N):
            Y = Y + [self.f(Y[-1],mu)]
        return Y[M:]

    def draw_f(self, ft = 1, mu=None, x0 = None, N = None):
        if mu is None :
            mu = self.mu
        if x0 is None :
            x0 = self.x0
        if N is None :
            N = self.N
            
        X = np.linspace(0,1,N)
        Y = self.evlt(x0,mu,N)
        fig = plt.figure(ft)
        plt.plot(X,Y,'bx',X,Y,'b')
        return fig
        
    def plot_f(self, ft = 1, mu=None, x0 = None, N = 20):
        fig = self.draw_f(ft,mu,x0,N)
        fig.show()

            



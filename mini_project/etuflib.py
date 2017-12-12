#!/usr/bin/env python
import numpy as np
from poplib import Draw
import matplotlib.pyplot as plt

class Etu_f(Draw):
    def draw(self, p = None):
        if p is None :
            p = self.p
        X = np.linspace(0,1,p.N)
        Y = np.array([ p.f(x,p.mu) for x in X ])
        fig = plt.figure(self.ft)
        plt.plot(X,Y,'b',label="x1 = f(x0, mu=" + str(p.mu) + ")")
        plt.xlim(0,1)
        plt.ylim(0,1)
        plt.xlabel("x0")
        plt.ylabel("x1")
        plt.title("Function f")
        plt.legend()
        return fig
        

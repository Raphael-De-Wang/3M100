#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from population import Population

# evolution
def evlt(self, x0, mu, N, M):
    Y = [x0]
    for t in range(1,N):
        Y = Y + [self.f(Y[-1],mu)]
    return Y[M-1:]
        
def draw_evlt(self, ft, x0, mu, N):
    Y = np.array(evlt(x0,mu,N,M))
    X = np.arange(len(Y)) + M - 1
    fig = plt.figure(ft)
    plt.plot(X,Y,'bx',X,Y,'b')
    return fig


#!/usr/bin/env python
import abc
import matplotlib.pyplot as plt

class PPlt(object) :
    def __init__(self,x0,mu,N,f=lambda x,mu:mu*x*(1.-x)):
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
        self.f = f
            
    # evolution
    def evol(self, x0 = None, mu=None, N = None):
        if x0 is None :
            x0 = self.x0
        if mu is None :
            mu = self.mu
        if N is None :
            N = self.N
            
        Y = [x0]
        for t in range(1,N):
            Y = Y + [self.f(Y[-1],mu)]
        return Y

        
class Draw(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, pplt, ft = 1):
            self.p = pplt
            self.ft = ft

    def plot(self):
        fig = plt.figure(self.ft)
        fig.show()
            
    @abc.abstractmethod
    def draw(self, p = None):
        return
            

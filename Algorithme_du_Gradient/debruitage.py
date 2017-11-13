#!/usr/bin/env python

import numpy

# private ref
from donnees import fake_donnee
from gradient import Gradient

class TV(Gradient):
    def __init__(self, donnee = None):
        if donnee is None:
            self.donnee = fake_donnee()
        else:
            self.donnee = donnee
        
    #  norme TV lissee 
    def tv_lissee(self, X = None, delta=10**-5):
        if X is None :
            X = self.donnee.signal_noisy
        X = numpy.array(X)
        X_TV_delta = numpy.sum(((X[1:] - X[:-1])**2 + delta)**0.5)
        return X_TV_delta
        
    #  gradient TV lissee
    def tv_lissee_gradient(self, X = None, delta=10**-5):
        if X is None :
            X = self.donnee.signal_noisy
        X = numpy.array(X)
        n = len(X)
        __tv_lissee_dp = lambda x1,x2,delta: (x1 - x2) / ((delta + (x1 - x2)**2) ** 0.5)
        X_TV_delta_D = [ __tv_lissee_dp(X[0],X[1],delta) if i == 0 
                           else __tv_lissee_dp(X[n-1],X[n-2],delta) if i == n - 1 
                           else __tv_lissee_dp(X[i],X[i+1],delta)
                                + __tv_lissee_dp(X[i],X[i-1],delta)
                         for i in range(n) ]
        return X_TV_delta_D
    

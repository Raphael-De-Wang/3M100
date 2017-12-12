#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from population import Population

class Bifurcation(object):

    def __init__(self,L,m,n):
        self.L = L
        self.m = m
        self.n = n

    def build_bif_pop_list(self,L,x0=None,N=None):
        if x0 is None :
            x0 = np.random.rand()
        if N is None :
            N = self.n
            
        return [ Population(mu, x0, N) for mu in L ]
    
    def build_bif_mu_x_list(self, pplt_lst, m = None):
        if m is None :
            m = self.m
            
        return [ (pplt.mu, x) for pplt in pplt_lst for x in pplt.evol()[m:] ]

    def plot_bif(self, L = None):
        if L is None :
            L = self.L
            
        pplt_lst = self.build_bif_pop_list(L)
        mu_x = self.build_bif_mu_x_list(pplt_lst)
        mu_x = np.array(mu_x)
        plt.scatter(mu_x[:,0],mu_x[:,1],s=1,edgecolor='none',c=mu_x[:,0])
        plt.show()


        

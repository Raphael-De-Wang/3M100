#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from simulation import Simulation

class Araignee(Simulation) :
    
    def araignee(self, x0 = None, mu = None, N = None):
        if x0 is None :
            x0 = self.x0
        if mu is None :
            mu = self.mu
        if N is None :
            N = self.N
            
        plt_vlt = self.evol(x0,mu,N)
        cord = [(plt_vlt[0],0)]
        for n in range(1, N):
                cord = cord + [(plt_vlt[n-1],plt_vlt[n])]
                cord = cord + [(plt_vlt[n],plt_vlt[n])]
        return cord

    def draw_agn(self, ft = 1, x0 = None, mu = None, N = None):
        if x0 is None :
            x0 = self.x0
        if mu is None :
            mu = self.mu
        if N is None :
            N = self.N
            
        fig = plt.figure(ft)
        cord = self.araignee(x0,mu,N)
        cord = np.array(cord)
        plt.plot(cord[:,0],cord[:,1],'r')
        return fig

    def draw_fi(self, ft = 1):
        fig = plt.figure(ft)
        plt.plot(np.linspace(0,1,11),np.linspace(0,1,11),'g')
        return fig

    def draw_diag_agn(self, ft = 1, x0 = None, mu = None, N = None):
        if x0 is None :
            x0 = self.x0
        if mu is None :
            mu = self.mu
        if N is None :
            N = self.N
            
        fig = plt.figure(ft)
        self.draw_agn(ft,x0,mu,N)
        self.draw_fi(ft)
        self.draw_f(ft,x0,mu,N)
        return fig


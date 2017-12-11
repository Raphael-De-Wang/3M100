#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from population import Population

class Araignee(object) :
    
    def __init__(self, pplt):
        self.pplt = pplt

    def araignee(self, pplt = None, n_steps = 20):
        if pplt is None :
            pplt = self.pplt
            
        plt_vlt = pplt.evol()
        cord = [(plt_vlt[0],0)]
        for n in range(1, n_steps):
            if (plt_vlt[n-1],plt_vlt[n]) not in cord :
                cord = cord + [(plt_vlt[n-1],plt_vlt[n])]
            else :
                break
            if (plt_vlt[n],plt_vlt[n]) not in cord :
                cord = cord + [(plt_vlt[n],plt_vlt[n])]
            else :
                break
        return cord
    

    def draw_agn(self, ft = 1, pplt = None, n_steps = 20):
        fig = plt.figure(ft)
        cord = self.araignee(pplt,n_steps)
        cord = np.array(cord)
        plt.plot(cord[:,0],cord[:,1],'r')

    def draw_fi(self, ft = 1):
        fig = plt.figure(ft)
        plt.plot(np.linspace(0,1,11),np.linspace(0,1,11),'g')

    def plot_agn(self, ft = 1, pplt = None, n_steps = 20):
        if pplt is None :
            pplt = self.pplt
        fig = plt.figure(ft)
        self.draw_agn(ft, pplt, n_steps)
        self.draw_fi(ft)
        pplt.draw_f(ft)
        fig.show()


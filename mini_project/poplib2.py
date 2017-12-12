#!/usr/bin/env python
import abc
import numpy as np
import matplotlib.pyplot as plt


class PPlt(object) :
    def __init__(self,x0,mu,N,M=1,f=lambda x,mu:mu*x*(1.-x)):
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
        self.M = M
        self.L = []
            
    # evolution
    def evol(self, x0 = None, mu = None, N = None):
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

    def setL(self, L):
        self.L = L
        
        
class Draw(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, pplt, ft = 1):
            self.p = pplt
            self.ft = ft

    def show(self):
        fig = plt.figure(self.ft)
        fig.show()
            
    @abc.abstractmethod
    def draw(self, p = None):
        return

        
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
        
class Sim(Draw):
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

        
class Sim2(Draw):
    def evlt(self, M, p):
        return p.evol()[M-1:]
        
    def draw(self, p = None):
        if p is None :
            p = self.p
        if hasattr(p, 'M'):
            M = p.M
        else :
            M = 1
        Y = np.array(self.evlt(M,p))
        X = np.arange(len(Y)) + M - 1
        fig = plt.figure(self.ft)
        plt.plot(X,Y,'b',label="x1 = f(x0, mu=" + str(p.mu) + ")")
        plt.xlim(M-1,p.N)
        plt.ylim(0,1)
        plt.xlabel("Time")
        plt.ylabel("Population")
        return fig

        
class Araignee(Etu_f) :
    def araignee(self, p):
        plt_vlt = p.evol()
        cord = [(plt_vlt[0],0)]
        for n in range(1, p.N):
                cord = cord + [(plt_vlt[n-1],plt_vlt[n])]
                cord = cord + [(plt_vlt[n],plt_vlt[n])]
        return cord

    def draw_agn(self, p = None):
        if p is None :
            p = self.p
        fig = plt.figure(self.ft)
        cord = self.araignee(p)
        cord = np.array(cord)
        plt.plot(cord[:,0],cord[:,1],'r')
        return fig

    def draw_fi(self, p = None):
        fig = plt.figure(self.ft)
        plt.plot(np.linspace(0,1,11),np.linspace(0,1,11),'g')
        return fig

    def draw(self, p = None):
        fig = plt.figure(self.ft)
        self.draw_agn(p)
        self.draw_fi(p)
        super(Araignee,self).draw()
        return fig

        
class Bifurcation(Draw):
    def build_bif_pop_list(self,p):
        self.pplt_lst = [ PPlt(p.x0, mu, p.N, p.M ) for mu in p.L ]
        return self.pplt_lst
    
    def build_bif_mu_x_list(self, pplt_lst=None):
        if pplt_lst is None :
            pplt_lst = self.pplt_lst
        return [ (p.mu,x) for p in pplt_lst for x in p.evol()[p.M-1:] ]

    def draw(self, pplt_lst = None):
        if pplt_lst is None :
            pplt_lst = self.p
        if type(pplt_lst) is not list : 
            self.build_bif_pop_list(pplt_lst)
        mu_x = np.array(self.build_bif_mu_x_list())
        fig = plt.figure(self.ft)
        plt.scatter(mu_x[:,0],mu_x[:,1],s=1,edgecolor='none',c=mu_x[:,0])
        return fig


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

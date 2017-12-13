#!/usr/bin/env python
import abc
import numpy as np
import matplotlib.pyplot as plt


class PPlt(object) :
    def __init__(self,x0,mu,N,M=1):
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
        self.f = lambda x,mu:mu*x*(1.-x)
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
    def setX(self, x):
        self.x0 = x
    def setMu(self, mu):
        self.mu = mu
    def setN(self, N) :
        self.N = N
    def setM(self, M) :
        self.M = M
    def setF(self, f):
        self.f = f
        
        
class Draw(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, pplt, ft = 1):
            self.p = pplt
            self.ft = ft

    @abc.abstractmethod
    def draw(self, p = None):
        return

    def show(self, save = False, draw = None,):
        if draw is None :
            draw = [ self.draw ]
        if type(draw) is not list :
            draw = [ draw ]
        fig = plt.figure(self.ft)
        for d in draw :
            d(self.p)
        if save is not False :
            fig.savefig(save)
        else: 
            fig.show()
            
        
class Etu_f(Draw):
    def draw(self, p = None):
        if p is None :
            p = self.p
        X = np.linspace(0,1,p.N)
        Y = np.array([ p.f(x,p.mu) for x in X ])
        fig = plt.figure(self.ft)
        plt.plot(X,Y,label="x1 = f(x0, mu=" + str(p.mu) + ")")
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
        plt.plot(X,Y,label="x0="+str(p.x0)+", mu=" + str(p.mu))
        plt.xlim(0,p.N)
        plt.ylim(0,1)
        plt.xlabel("Time")
        plt.ylabel("Population")
        plt.title("Simulaton d'Evolution")
        plt.legend()
        return fig

        
class Sim2(Draw):
    def evlt(self, p):
        return p.evol()[p.M-1:]
        
    def draw(self, p = None):
        if p is None :
            p = self.p
        Y = np.array(self.evlt(p))
        X = np.arange(len(Y)) + p.M - 1
        fig = plt.figure(self.ft)
        plt.plot(X,Y,label="x0="+str(p.x0)+", mu=" + str(p.mu))
        plt.xlim(p.M-1,p.N)
        plt.ylim(0,1)
        plt.xlabel("Time")
        plt.ylabel("Population")
        plt.title("Simulaton d'Evolution")
        plt.legend()
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
        plt.xlim(0,1)
        plt.ylim(0,1)
        plt.title("Diagramme Araignee")
        return fig

    def draw_fi(self, p = None):
        fig = plt.figure(self.ft)
        plt.plot(np.linspace(0,1,11),np.linspace(0,1,11),'g')
        return fig

    def draw(self, p = None):
        fig = plt.figure(self.ft)
        super(Araignee,self).draw()
        self.draw_fi(p)
        self.draw_agn(p)
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
        plt.xlim(0,4)
        plt.ylim(0,1)
        plt.xlabel('$\mu$')
        plt.ylabel("Population")
        plt.title("Diagramme de Bifurcation")
        return fig


class Attr(Draw) :
    def evol(self, p):
        em = p.evol()[p.M-1:]
        return zip(em[:-1],em[1:])

    def draw(self, p = None):
        if p is None :
            p = self.p
        em = self.evol(p)
        em = np.array(em)
        if p.mu > 0 and p.mu < 3 :
            plt.plot(em[:,0],em[:,1],"-x",label="mu="+str(p.mu))
        else:
            plt.plot(em[:,0],em[:,1],label="mu="+str(p.mu))            
        plt.xlim(0,1)
        plt.ylim(0,1)
        plt.title("Attracteur")
        plt.legend()
        
class AttrRand(Attr) :
    def evol(self, p):
        X0 = np.random.rand(p.N)
        return zip(X0,p.f(X0,p.mu))


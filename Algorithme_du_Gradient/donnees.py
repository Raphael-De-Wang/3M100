#!/usr/bin/env python

import numpy
import numpy.random as rd
import matplotlib.pyplot as plt

class fake_donnee(object) :
    def __init__(self, n_jumps = 5, n_pts = 100, noise_level = 0.01):
        # On fixe la graine du generateur pseudo-aleatoire
        # (comme ca, je sais quel X vous avez)
        rd.seed(5000) 
        # Nombre de sauts : n_jumps = 5
        self.n_jumps = n_jumps
        # Nombre de points: n_pts   = 100
        self.n_pts   = n_pts
        # Noise Level : 0.01
        self.noise_level = noise_level 

    def signal_no_noise(self, n_jumps = None, n_pts = None):
        if n_jumps is None:
            n_jumps = self.n_jumps
        if n_pts is None:
            n_pts = self.n_pts
        jumps = rd.rand(n_jumps) # Localisation des sauts au hasard
        jumps = numpy.sort(jumps)
        jumps = numpy.insert(jumps, 0, 0.0)
        jumps = numpy.insert(jumps, n_jumps + 1, 1.0)
        t = numpy.linspace(0, 1-1.0/n_pts, n_pts) # Localisations des points
        self.signal_no_noise = numpy.zeros(n_pts) # Le vecteur X
        for i in range(n_jumps + 1):
            # Valeur de x en les points t_k,k = 0,..,n-1
            self.signal_no_noise[(t >= jumps[i]) & (t < jumps[i + 1])] = 0.5*(1 + rd.rand()) 
        return self.signal_no_noise
    
    def signal_noisy(self, signal_no_noise = None, noise_level = None, n_pts = None):
        if signal_no_noise is None :
            signal_no_noise = self.signal_no_noise
        if noise_level is None :
            noise_level = self.noise_level
        if n_pts is None :
            n_pts = self.n_pts
        # Signal bruite
        self.signal_noisy = self.signal_no_noise + noise_level * rd.randn(n_pts) 
        return self.signal_noisy

    def show(self,signal_no_noise = None, signal_noisy = None):
        if signal_no_noise is None:
            signal_no_noise = self.signal_no_noise
        if signal_noisy is None :
            signal_noisy = self.signal_noisy
        ## Affichage graphique
        plt.figure() # Creer un graphique
        # En bleu, la valeur de x
        plt.plot(t, signal_no_noise, 'b', label="Signal sans bruit")
        # En vert, la valeur de y
        plt.plot(t, signal_noisy, 'g', label=r"Signal avec bruit")
        # Ajouter une legende au graphique
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                   ncol=2, mode="expand", borderaxespad=0.)
        plt.show() # Afficher le graphique
        

#!/usr/bin/env python

import numpy as np

from population import Population
from araignee import Araignee
from bifurcation import Bifurcation
from attracteur import Attracteur
# p = Population(3.5,0.8,200)
# argn = Araignee(p)
# argn.plot_agn()

# bif = Bifurcation(np.linspace(0,4,1000),10,20)
# bif.plot_bif()

att = Attracteur([3.9], 200, 1000)
att.plot_evol_marche_mu(3.9)

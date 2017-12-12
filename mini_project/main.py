#!/usr/bin/env python
from poplib2 import *

p = PPlt(0.1,3.2,50)
e = Etu_f(p)
# e.draw()
# e.show()

s = Sim(p)
# s.draw()
# s.show()

s2 = Sim2(p)
# p.setM(20)
# s2.draw()
# s2.show()

argn = Araignee(p)
# argn.draw()
# argn.show()

p = PPlt(0.1,3.2,50,20)
p.setL(np.linspace(0,4,100))
bif = Bifurcation(p)
bif.draw()
bif.show()

# att = Attracteur([3.9], 200, 400)
# att.plot_evol_marche_mu(3.9)

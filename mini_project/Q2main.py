#!/usr/bin/env python
from chaolib import *

# Question 2 : Definition de la fonction
p = PPlt(0.1,3.2,50)
e = Etu_f(p,1)
e.show()
# e.show(save="f_mu.jpg")

for mu in np.linspace(0,4,6) :
    p.mu = mu
    e = Etu_f(p,2)
    e.show()
    # e.show(save="f_mu_cmp.jpg")

p.mu = 4.5
e = Etu_f(p,3)
e.show(save="f_mu_invalid.jpg")

# argn = Araignee(p,4)
# argn.show()

# p = PPlt(0.1,3.2,50,20)
# p.setL(np.linspace(0,4,1000))
# bif = Bifurcation(p,5)
# bif.show()

# att = Attr(p,6)
# att.show()

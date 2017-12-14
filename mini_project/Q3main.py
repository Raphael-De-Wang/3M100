#!/usr/bin/env python
from chaolib import *

p = PPlt(0.1,3.2,50,20)

# Q1. 
s = Sim(p,1)
s.show(save="sim1.jpg")
# s.show()

# Q2.
s2 = Sim2(p,2)
s2.show(save="sim2.jpg")
# s2.show()

# Q3.
for x in np.linspace(0.1,0.9,3) :
    for mu in [1., 2.5, 3.5, 3.8] :
        p.setX(x) 
        p.setMu(mu)
        s = Sim(p,3)
        s.show(save="mu_evol_cmp.pdf")
        # s.show()

# Q4.
for x in np.linspace(0.1,0.9,3) :
    for mu in [1., 2.5, 3.5, 3.8] :
        p.setX(x) 
        p.setMu(mu)
        s = Sim(p,x*100)
        s.show(save="mu_evol_cmp[x0="+str(x)+"].pdf")
        # s.show()

for mu in [1., 2.5, 3.5, 3.8] :
    for x in np.linspace(0.1,0.9,3) :
        p.setX(x) 
        p.setMu(mu)
        s = Sim(p,mu*100)
        s.show(save="x0_evol_cmp[mu="+str(mu)+"].pdf")
        # s.show()


for mu in [3.8, 3.9, 3.99] :
    p.setMu(mu)
    s = Sim(p)
    s.show(save="evol_mu4.pdf")
        
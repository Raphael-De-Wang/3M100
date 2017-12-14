#!/usr/bin/env python
from chaolib import *

p = PPlt(0.1,3.2,50)

# Q1.
argn = Araignee(p,1)
# argn.show()
argn.show("araignee.jpg", argn.draw_agn)

# Q2.
# argn.show()
argn.show(save="diag_mu.jpg")

# Q3.
for mu in [0.8,1.5,2.5,3.2,3.5,3.8] :
    p.setMu(mu)
    argn = Araignee(p,mu*10)
    # argn.show()
    argn.show(save="diag_cmp_mu["+str(mu)+"].jpg")
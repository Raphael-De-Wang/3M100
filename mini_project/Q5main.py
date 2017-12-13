#!/usr/bin/env python
from chaolib import *

p = PPlt(0.1,3.2,50,20)

# Q1. Line 163 - 170

# Q2.
p.setL(np.linspace(0,4,1000))
bif = Bifurcation(p,5)
# bif.show()
bif.show("bif.jpg")

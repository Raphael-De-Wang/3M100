#!/usr/bin/env python
from chaolib import *

p = PPlt(0.1,3.2,50,20)

# Q1. Line 164 - 170

# Q2.
p.setL(np.linspace(0,4,1000))
bif = Bifurcation(p,5)
# bif.show()
fig = plt.figure(5)
plt.plot(np.ones(10)*3.545, np.linspace(0,1,10))
plt.plot(np.ones(10)*3.6, np.linspace(0,1,10))
bif.show()

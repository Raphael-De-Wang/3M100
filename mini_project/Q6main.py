#!/usr/bin/env python
from chaolib import *

p = PPlt(0.1,3.2,50,20)

# Q1.
att = Attr(p)
# att.show()
att.show("att.jpg")

# Q2.
p.setM(100)
p.setN(1000)
for mu in [3.8,3.5,3.2,2.5] :
    p.setMu(mu)
    att = Attr(p,6)
    # att.show()
    att.show("att_cmp.jpg")

# Q3.
for mu in [3.8,3.5,3.2,2.5,1.5] :
    p.setMu(mu)
    attR = AttrRand(p,8)
    # attR.show()
    # attR.show("att_rand_cmp.jpg")


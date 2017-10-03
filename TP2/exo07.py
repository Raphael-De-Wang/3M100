#!/usr/bin/env python

liste1=['a','b','c']
liste2=range(1,len(liste1)+1)

L1=[k*s for k in liste2 for s in liste1]
L2=[k*s for s in liste1 for k in liste2]
L3=[k*s for (k,s) in zip(liste2,liste1)]

L4 = [ (i+1) * elt for i,elt in zip(liste2-1,liste1) ]
L4.reverse()
print L4

L5 = [ (i+1) * liste1[i] for i in range(len(liste1)-1,-1,-1) ]
print L5

#!/usr/bin/env python

# exo 1
a=7
b=4
print type(a)
print type(b)
print a,b,a+b,a-b,a*b,a**b
print a/b, a%b
a=7.0;b=4
print type(a), type(b)
print a,b,a+b,a-b,a*b,a**b
print a/b, type(a/b)
a,b=2,3.75
print type(a), type(b)
c=int(b)
d=a+0.
print type(c), type(d)

# exo 2
L=range(12)
print L[0:7]
print L[:8]
print L[5:]
print L[0:7:2]
print L[0::2]
print L[-7:-2]

# exo 3
L=[1, 'deux', 33, False,'trois']
print len(L)
print L[0], L[1], L[0:3]
L[1]='two'
print L
L.append('z')
print L
L.extend(['y',7])
print L
L.pop()
print L
L.remove(33)
print L
L[2]=[56, 'abc']
print L

# exo 4 
a=range(5);b=a;a[1]=-1
a=range(2,9);b=a;a[1]=b[0]
a=range(5);b=a[:];a[0]=-1

# exo 5 
a=1
while not(a==0):
    b,a=a,.5*a
print a,b

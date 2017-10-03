#!/usr/bin/env python

# exo 01
a, b = 3,6

u, v = a < b, a >= b

# non u
not u

# non v
not v

# u et v
u and v

# u ou v
u or v

# u ou non v
u or not v

# non u ou u
not u or u 

# exo 02
a=1./3
b=2./3
print a,b

a=10**(-320);b=10**(-330)
print a, b

c,d=1.e308,2.e308
print c, d

print 12+b == 12


# exo 03
print (1)==(1,)
print (1,2)==(1,2,)
# print (1,2)==1,2
print False
a=1,2
b=(1,2)
print a==b

# exo 04
liste1=['saut','course']
liste2=['escrime','equitation']
liste3=['judo','boxe']
fusion=[liste1,liste2,liste3]
for i in range(len(fusion)):
    for j in range(len(fusion[i])):
        print i,j,fusion[i][j]

fusion = liste1 + liste2 + liste3
for i in range(len(fusion)):
    for j in range(len(fusion[i])):
        print i,j,fusion[i][j]

#!/usr/bin/env python

from exo01 import Suite


class V(Suite) :
    def __init__(self,n0,K):
        self.v0 = n0
        self.K  = K
        self.suite_lst = [self.v0]

    def next(self,vk) :
        if vk%2 is 1 : # vk impair
            return 3*vk+1
        elif vk%2 is 0 : # vk pair
            return vk/2
        else : 
            raise ValueError("vk is not an integer !")

    def u_ext(self, n) : # lazy strategy
        if type(n) is int and n > 1 :
            while len(self.suite_lst) <= n :
                un_tmp = self.next(self.suite_lst[-1])
                self.suite_lst.append(un_tmp)

    def get(self,n):
        if n >= self.K :
            print "n should not bigger than {0} !".format(str(self.K))
            return
        else :
            return super(V,self).get(n)

# test
# v = V(1,100)
# print v.get(10)
# v.show()


